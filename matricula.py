#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Otimização de grade de disciplinas, visando maximizar o número de aulas por semana
# ou juntar as folgas no mesmo dia

from scipy import linalg, sparse
from itertools import combinations
import numpy as np
import dados

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
print "Número de grades possíveis:\t",	2 ** cursaveis.count(1) - 1

# Obtém os IDs das disciplinas cursáveis
cursaveis = set([x for x in xrange(len(cursaveis)) if cursaveis[x] == 1])
cursaveis -= dados.disc_inativas

# Retorna True se a grade não possuir conflitos
def grade_valida(g):
	if len(g.data) > 0:
		return g.data.max() <= 1 # no máximo uma disciplina por aula

# 0		= grade vazia
# 100	= grade perfeita
def grade_pontuacao(g):
	pontos = 100 * (float(g.nnz) / (g.shape[0] * g.shape[1]))
	dias_vazios = list(g.sum(axis=0).getA()[0])
	# help(dias_vazios)
	pontos *= 1 + (.05 * dias_vazios.count(0))
	return pontos

grades = []

print cursaveis

for i in range(7)[::-1]:
	for grade in combinations(cursaveis, i):
		tmp = dados.disciplinas[0].copy()
		for disc in grade:
			tmp = tmp + dados.disciplinas[disc]
		if grade_valida(tmp):
			horario = tmp.copy()
			grades.append((tmp.copy(), sorted(grade), grade_pontuacao(tmp)))
			# if tmp.nnz == 20: print tmp.todense(), sorted(grade), "[PERFEITA]\n"
for i in grades: print i[0].todense(), i[1], i[2], "\n"