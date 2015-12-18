#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Otimização de grade de disciplinas, visando maximizar o número de aulas por semana
# ou juntar as folgas no mesmo dia

from sys import stdout
import numpy as np
from numpy import mean, std
from time import time
from math import isnan
from itertools import combinations, compress
from functools import reduce
import dados, disciplina, algoritmo_genetico

agora = time
deps = dados.dependencias
historico = dados.historico
horario = dados.horario	

somaReq = deps.sum(axis=0)

def cursaveis(historico, dependencias, historico_binario=True):
	'''Lista de disciplinas que o aluno pode cursar.'''
	if not historico_binario:
		print("Histórico não binário: ", historico)
		hist_bin = list()
		historico.append(0) #Disciplina nula
		for i in range(len(dados.historico)):
			hist_bin.append(0)
		for i in historico:
			if 0 <= i < len(dados.historico):
				hist_bin[i] = 1
		historico = np.array(hist_bin).T
	discs_cursaveis = historico.dot(dependencias)
	discs_cursaveis = discs_cursaveis - historico

	# Para evitar erro de div. por zero na disciplina nula e não permitir como cursável após divisão inteira
	somaReq[0] = -2 # Qualquer valor < -1
	discs_cursaveis //= somaReq
	somaReq[0] = 0

	# Se o vetor de aprovação for inconsistente (disciplinas cumpridas sem todos os requisitos),
	# o vetor de cursáveis terá valores negativos.
	discs_cursaveis = map(lambda x: 0 if x < 0 else x, discs_cursaveis)
	discs_cursaveis = list(discs_cursaveis)
	# Obtém os IDs das disciplinas cursáveis
	discs_cursaveis = compress(range(len(discs_cursaveis)), discs_cursaveis)
	discs_cursaveis = list(set(discs_cursaveis) - dados.disc_inativas)
	discs_cursaveis.sort()
	return discs_cursaveis

print("Requisitos:\t%s" % "".join(map(str, somaReq)))
print("Histórico:\t%s" % "".join(map(str, historico)))
print("Cursáveis:\t%s" % "".join(map(str, cursaveis(historico, deps))))
print("Calculando as melhores grades para você. Aguarde...")

def grade_valida(g):
	__doc__ = '''Retorna True se a grade não possuir conflitos.'''
	assert len(g) > 0, "A grade deve ter ao menos uma disciplina."
	return max(g) == 1 # no máximo uma disciplina por aula

def formata_horario(h):
	'''Transforma um horário linear em uma matriz semanal, para impressão amigável'''
	return h.reshape((dados.dias_por_semana, dados.aulas_por_dia)).T

def grade_pontuacao(g):
	periodo_max = 8
	aulas = aulas_da_grade(g, dados.horario)
	dias_vazios = formata_horario(aulas)
	dias_vazios = dias_vazios.sum(axis=0)
	dias_vazios = list(dias_vazios).count(0)
	pontos = list(aulas).count(1) # número de aulas
	bonus = 0 # % sobre os pontos
	bonus += 10e-2 * dias_vazios	# Privilegia dias de folga
	bonus += 2e-2 * (periodo_max - (mean(g)) / 10) # Privilegia as primeiras disciplinas
	bonus -= 1e-2 * (std(g)/mean(g)) # Penaliza o espalhamento de disciplinas
	pontos *= 1 + bonus
	return 0 if isnan(pontos) else pontos

def aulas_da_grade(g, horario):
	'''Retorna uma matriz contendo o horário semanal das disciplinas da grade g'''
	assert len(g) == len(set(g)), "A lista de disciplinas não pode conter elementos repetidos."
	aulas = horario[0]
	for disciplina in g:
		aulas = aulas + horario[disciplina]
	return aulas

def binario_para_indices(binario, iteravel):
	'''Transforma as posições dos elementos 1 de uma lista binária em índices de um iterável.'''
	assert all([x in (0,1) for x in binario]), "A lista binária deve conter apenas zeros e uns. %s" % binario
	assert len(binario) == len(iteravel), "As listas devem ter o mesmo tamanho. %d != %d" % (len(binario), len(iteravel))
	if len(binario) > 0:
		return list(compress(iteravel, binario))
	else:
		return []

# Busca exaustiva (todas as combinações possíveis)
def busca_exaustiva(cursaveis, lim_grades, max_disciplinas=0):
	grades = []
	limite_disciplinas = len(cursaveis) + 1 if max_disciplinas == 0 else max_disciplinas
	for i in range(1, limite_disciplinas + 1):
		print("Buscando grades com %d disciplina%s..." % (i, ("s" if i > 1 else "")))
		discs_tmp = []	# Lista de disciplinas para cada tamanho de grade
		inicio_tmp = agora()
		for grade in combinations(cursaveis, i):
			horario = [dados.horario[d] for d in grade]
			horario = reduce(lambda a, b: a + b, horario)
			if grade_valida(horario):
				discs_tmp.append(grade)
		if len(discs_tmp) > 0:
			map(sorted, discs_tmp)
			print("%d encontradas em %.3f segundos." % (len(discs_tmp), (agora() - inicio_tmp)))
			grades.extend(discs_tmp)
		else:
			print("Nenhuma encontrada em %.3f segundos." % (agora() - inicio_tmp))
			break
	return grades

def busca_gulosa(cursaveis, lim_grades):
	grades = []
	cursaveis.sort()
	for i in range(len(cursaveis)):
		g = []
		for d in cursaveis:
			if grade_valida(aulas_da_grade(g + [d], dados.horario)):
				g.append(d)
		grades.append(g)
		cursaveis = cursaveis[1:] + cursaveis[0:1]
	return grades


# def busca_genetica(genotipo, geracoes):
# 	'''Evolui para uma boa grade (possivelmente a melhor) usando algoritmo genético.'''
# 	g = algoritmo_genetico.Genetico()
# 	tam_genoma = len(genotipo)
# 	tam_populacao = 50
# 	perc_corte = 80
# 	mutacao = 30
# 	populacao = g.populacao_inicial(tam_populacao, tam_genoma)
# 	i, melhor, pior = 0, -1, 1
# 	avalia_pontuacao = lambda x: grade_pontuacao(list(compress(genotipo, x)))
#
# 	while i < geracoes:
# 		i += 1
# 		# pior = avalia_pontuacao(populacao[-1])
# 		desvio = std(list(map(avalia_pontuacao, populacao)))
# 		# media = mean(map(avalia_pontuacao, populacao))
# 		melhor = avalia_pontuacao(populacao[0])
# 		print("Geração %d:\tDesvio:%.2f pts\t\tMelhor: %.2f pts\tDiscs.:\t%s" % (i, desvio, melhor, list(compress(genotipo, populacao[0]))))
# 		populacao = g.selecao(populacao, avalia_pontuacao, perc_corte)
# 		populacao = g.procriar(populacao, tam_populacao - len(list(populacao)), mutacao)
# 	return populacao[0]


def grade_ideal(historico, lim_grades=5, max_disciplinas=0):
	inicio = agora()
	grades = busca_exaustiva(cursaveis(historico, deps, False), lim_grades, max_disciplinas)

	#==========================================================
	#print("\nTotal de %d grades encontradas em %-.3fs." % (len(grades), agora() - inicio))
	#stdout.write("Ordenando as grades...")
	#inicio = agora()
	# Ordena as grades por quantidade de disciplinas e seus períodos
	grades.sort(key=grade_pontuacao, reverse=True)
	#print("Ordenação feita em %.3f segundos." % (agora() - inicio))

	for i in enumerate(grades[:lim_grades]):#[:(5 if len(grades) > 5 else -1)]:
		print("\n(%d)\t%.2fpts\t" % (i[0] + 1, grade_pontuacao(i[1])) + str(i[1]))
		print(formata_horario(aulas_da_grade(i[1], dados.horario)))

	return grades[:lim_grades]

max_grades = 5
max_disciplinas = 6
meu_historico = [1,2,3,4,6,7,8,9,11,12,13,14,15,19,31,33,40]
# print(grade_ideal(meu_historico, max_grades, max_disciplinas))
