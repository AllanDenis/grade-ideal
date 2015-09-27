#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Otimização de grade de disciplinas, visando maximizar o número de aulas por semana
# ou juntar as folgas no mesmo dia

import time
agora = time.time
inicio = agora()

from scipy import linalg, sparse
from itertools import combinations
import numpy as np
import dados, disciplina, view

deps = dados.MD
aprovadas = dados.MA

somaReq = deps.sum(axis=0)

# Lista de disciplinas que o aluno pode cursar.
cursaveis = aprovadas.dot(deps)
cursaveis = cursaveis - aprovadas

# Para evitar erro de div. por zero na disciplina nula e não permitir como cursável após divisão inteira
somaReq[0] = -2 # Qualquer valor < -1
for i in range(cursaveis.shape[1] - 1):
	cursaveis[0,i] //= somaReq[i]
somaReq[0] = 0

# Transforma em lista
cursaveis = list(cursaveis.getA()[0])

# Se o vetor de aprovação for inconsistente (disciplinas cumpridas sem todos os requisitos),
# o vetor de cursáveis terá valores negativos.
for i in cursaveis:
	if i < 0: 
		exit("Vetor de aprovação inválido. Verifique as dependências.")
	
print "Vetor de requisitos (SC):\t", "".join(map(str, somaReq))
print "Vetor de aprovação (AP):\t", "".join(map(str, aprovadas.toarray()[0]))
print "Vetor de cursáveis (DC):\t",		"".join(map(str, cursaveis))
print "Calculando as melhores grades para você. Aguarde..."

# Obtém os IDs das disciplinas cursáveis
cursaveis = set([x for x in xrange(len(cursaveis)) if cursaveis[x] == 1])
cursaveis = list(cursaveis - dados.disc_inativas)

# Retorna True se a grade não possuir conflitos
def grade_valida(g):
	return g.data.max() <= 1 # no máximo uma disciplina por aula

def grade_pontuacao(g):
	periodo_max = 8
	aulas = aulas_da_grade(g)
	pontos = aulas.nnz # número de aulas
	bonus = 0 # % sobre os pontos
	dias_vazios = aulas.sum(axis=0).getA()[0] # Aulas por dia
	dias_vazios = list(dias_vazios).count(0)	# Dias sem aula
	bonus += 10e-2 * dias_vazios	# Privilegia dias de folga
	bonus += 2e-2 * (periodo_max - (np.mean(g)) / 5) # Privilegia as primeiras disciplinas
	bonus -= 1e-2 * (np.std(g)/np.mean(g)) # Penaliza o espalhamento de disciplinas
	pontos *= 1 + bonus
	return pontos

# Retorna uma matriz contendo o horário semanal das disciplinas da grade g
def aulas_da_grade(g):
	une_disciplinas = lambda a, b: a + b
	horario_disciplinas = map(lambda d: dados.disciplinas[d], g)
	return reduce(une_disciplinas,	horario_disciplinas)
	
grades = []
# Busca exaustiva (todas as combinações possíveis)
for i in xrange(1, 7):#len(cursaveis) + 1):
	print "Buscando grades com %d disciplina%s..." % (i, ("s" if i > 1 else ""))
	discs_tmp = []	# Lista de disciplinas para cada tamanho de grade
	inicio_tmp = agora()
	for grade in combinations(cursaveis, i):
		horario = dados.disciplinas[0].horario.copy()
		horario = reduce(lambda a, b: a + b, map(lambda d: dados.disciplinas[d], grade))
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

print "Total de grades:\t%d" % len(grades)
print "Ordenando as grades..."
inicio_tmp = agora()
# Ordena as grades por quantidade de disciplinas e seus períodos
grades.sort(key=grade_pontuacao, reverse=True)
print "Ordenação feita em %.3f segundos." % (agora() - inicio_tmp)

# '''		
for i in enumerate(grades[:3]):#[:(5 if len(grades) > 5 else -1)]:
	print "\n(%d)\t%.2fpts\t" % (i[0] + 1, grade_pontuacao(i[1])), i[1]
	print aulas_da_grade(i[1]).todense()

# '''
print "\vTudo feito em %-.3fs." % (agora() - inicio)

v = view.View()
v.dados = {}
v.dados["tamanhos"] = map(lambda g: len(g), grades)
v.dados["pontos"] = map(lambda g: grade_pontuacao(g), grades)
v.dados["popularidade"] = []

for g in grades:
	for i in g:
		v.dados["popularidade"].append(i)

v.exibir()
