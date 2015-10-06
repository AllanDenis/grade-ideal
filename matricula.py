#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Otimização de grade de disciplinas, visando maximizar o número de aulas por semana
# ou juntar as folgas no mesmo dia

import dados, disciplina, view
import time, math
from itertools import combinations
import numpy as np
from scipy import linalg, sparse
import algoritmo_genetico 

agora = time.time
deps = dados.dependencias
historico = dados.historico

somaReq = deps.sum(axis=0)

# Lista de disciplinas que o aluno pode cursar.
cursaveis = historico.dot(deps)
cursaveis = cursaveis - historico

# Para evitar erro de div. por zero na disciplina nula e não permitir como cursável após divisão inteira
somaReq[0] = -2 # Qualquer valor < -1
for i in range(cursaveis.shape[1] - 1):
	cursaveis[0,i] //= somaReq[i]
somaReq[0] = 0

# Transforma em lista
cursaveis = list(cursaveis.getA()[0])

# Se o vetor de aprovação for inconsistente (disciplinas cumpridas sem todos os requisitos),
# o vetor de cursáveis terá valores negativos.
cursaveis = map(lambda x: 0 if x < 0 else x, cursaveis)
	
print "Vetor de requisitos (SC):\t", "".join(map(str, somaReq))
print "Vetor de aprovação (AP):\t", "".join(map(str, historico.toarray()[0]))
print "Vetor de cursáveis (DC):\t",		"".join(map(str, cursaveis))
print "Calculando as melhores grades para você. Aguarde..."

# Obtém os IDs das disciplinas cursáveis
cursaveis = set([x for x in xrange(len(cursaveis)) if cursaveis[x] == 1])
cursaveis = sorted(list(cursaveis - dados.disc_inativas))


def grade_valida(g):
	'''Retorna True se a grade não possuir conflitos.'''
	assert len(g.flat) > 0, "A grade deve ter ao menos uma disciplina."
	return max(g.flat) == 1 # no máximo uma disciplina por aula

# Transforma um horário linear em uma matriz semanal, para impressão amigável
def formata_horario(h):
	return h.reshape(dados.dias_por_semana, dados.aulas_por_dia).T

def grade_pontuacao(g):
	periodo_max = 8
	aulas = aulas_da_grade(g, dados.horario)
	dias_vazios = formata_horario(aulas)
	dias_vazios = dias_vazios.sum(axis=0)
	dias_vazios = list(dias_vazios).count(0)
	pontos = list(aulas).count(1) # número de aulas
	bonus = 0 # % sobre os pontos
	bonus += 10e-2 * dias_vazios	# Privilegia dias de folga
	bonus += 2e-2 * (periodo_max - (np.mean(g)) / 10) # Privilegia as primeiras disciplinas
	bonus -= 1e-2 * (np.std(g)/np.mean(g)) # Penaliza o espalhamento de disciplinas
	pontos *= 1 + bonus
	return 0 if math.isnan(pontos) else pontos

# Retorna uma matriz contendo o horário semanal das disciplinas da grade g
def aulas_da_grade(g, horario):
	assert len(g) == len(set(g)), "A lista de disciplinas não pode conter elementos repetidos."
	une_disciplinas = lambda a, b: a + b
	horario_disciplinas = map(lambda d: dados.horario[d], g)
	if len(horario_disciplinas) == 0: return horario[0]
	return reduce(une_disciplinas, horario_disciplinas)

def binario_para_indices(binario, iteravel):
	'''Transforma as posições dos elementos 1 de uma lista binária em índices de um iterável.'''
	assert False not in [x in (0,1) for x in binario], "A lista binária deve conter apenas zeros e uns. %s" % binario
	assert len(binario) == len(iteravel), "As listas devem ter o mesmo tamanho. %d != %d" % (len(binario), len(iteravel)) 
	lista = []
	for i in range(len(binario)):
		if binario[i] == 1:
			lista.append(iteravel[i])
	return lista

# Busca exaustiva (todas as combinações possíveis)
def busca_exaustiva(cursaveis, lim_grades):
	grades = []
	for i in xrange(1, len(cursaveis) + 1):
		print "Buscando grades com %d disciplina%s..." % (i, ("s" if i > 1 else ""))
		discs_tmp = []	# Lista de disciplinas para cada tamanho de grade
		inicio_tmp = agora()
		for grade in combinations(cursaveis, i):
			horario = dados.horario[0].copy()
			horario = map(lambda d: dados.horario[d], grade)
			horario = reduce(lambda a, b: a + b, horario)
			# for disc in grade:
				# horario = horario + dados.disciplinas[disc]
			if grade_valida(horario):
				# discs_tmp.append((horario, sorted(grade), grade_pontuacao(horario)))
				discs_tmp.append(sorted(grade))
		if len(discs_tmp) > 0:
			print "%d encontradas em %.3f segundos." % (len(discs_tmp), (agora() - inicio_tmp))
			grades.extend(discs_tmp)
		else:
			print "Nenhuma encontrada em %.3f segundos." % (agora() - inicio_tmp)
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

def busca_genetica(cursaveis):
	'''Evolui para uma boa grade (possivelmente a melhor) usando algoritmo genético.'''
	g = algoritmo_genetico.Genetico()
	tam_genoma = len(cursaveis)
	tam_populacao = 50
	perc_corte = 80
	mutacao = 20
	geracoes = 500
	populacao = g.populacao_inicial(tam_populacao, tam_genoma)
	i, melhor, pior = 1, -1, 1
	avalia_pontuacao = lambda x: grade_pontuacao(binario_para_indices(x, cursaveis))

	while i < geracoes:
		i += 1
		# pior = avalia_pontuacao(populacao[-1])
		desvio = np.std(map(avalia_pontuacao, populacao))
		# media = np.mean(map(avalia_pontuacao, populacao))
		melhor = avalia_pontuacao(populacao[0])
		print "Geração %d:\tDesvio:%.2f pts\t\tMelhor: %.2f pts\tDiscs.:\t" % (i, desvio, melhor), binario_para_indices(populacao[0], cursaveis)
		populacao = g.selecao(populacao, avalia_pontuacao, perc_corte)
		populacao = g.procriar(populacao, tam_populacao - len(populacao), mutacao)
	return populacao[0]

inicio = agora()
#==========================================================
grade = busca_genetica(cursaveis)
grade = binario_para_indices(grade, cursaveis)
print grade
print "\n(%d)\t%.2fpts\t" % (1, grade_pontuacao(grade)), "%.2f" % grade_pontuacao(grade)
print formata_horario(aulas_da_grade(grade, dados.horario))
#==========================================================
'''		
# grades = busca_gulosa(cursaveis)
grades = busca_exaustiva(cursaveis, 5)

print "\vBusca feita em %-.3fs." % (agora() - inicio)
print "Total de grades:\t%d" % len(grades)
print "Ordenando as grades..."
inicio = agora()
# Ordena as grades por quantidade de disciplinas e seus períodos
grades.sort(key=grade_pontuacao, reverse=True)
print "Ordenação feita em %.3f segundos." % (agora() - inicio)

for i in enumerate(grades[:]):#[:(5 if len(grades) > 5 else -1)]:
	print "\n(%d)\t%.2fpts\t" % (i[0] + 1, grade_pontuacao(i[1])), i[1]
	print formata_horario(aulas_da_grade(i[1], dados.horario))
'''


# v = view.View()
# v.dados = {}
# v.dados["tamanhos"] = map(lambda g: len(g), grades)
# v.dados["pontos"] = map(lambda g: grade_pontuacao(g), grades)
# v.dados["popularidade"] = []

# for g in grades:
	# for i in g:
		# v.dados["popularidade"].append(i)

# v.exibir()