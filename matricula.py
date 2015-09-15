#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Otimização de grade de disciplinas, visando maximizar o número de aulas por semana
# ou juntar as folgas no mesmo dia

from scipy import linalg, sparse
from scipy.misc import comb
import numpy as np
import dados

deps = dados.MD
aprovadas = dados.MA

deps = np.array([																	#teste
		map(int, "010000"),
		map(int, "001100"),
		map(int, "000010"),	#teste
		map(int, "000001"),
		map(int, "000001"),
		map(int, "000000")])	#teste							

# aprovadas = np.array(map(int, "110100")) #teste
aprovadas = np.array(map(int, raw_input("Digite seu vetor de aprovação (1" + ("x" * (len(deps)-1) )+ "): "))) #teste
 
# Soma dos requisitos de cada disciplina (soma das colunas)
somaReq = deps.sum(axis=0)

# Lista de disciplinas que o aluno pode cursar.
cursaveis = aprovadas.dot(deps)
cursaveis -= aprovadas

# Para evitar erro de div. por zero na disciplina nula e não permitir como cursável após divisão inteira
somaReq[0] = -2 # Qualquer valor < -1
cursaveis //= somaReq
somaReq[0] = 0

# Se o vetor de aprovação for inconsistente (disciplinas cumpridas sem todos os requisitos),
# o vetor de cursáveis terá valores negativos.
for i in cursaveis:
	if i < 0: 
		exit("Vetor de aprovação inválido. Verifique as dependências.")

print "Vetor de requisitos (SC):\t",			"".join(map(str, somaReq))
print "Vetor de aprovação (AP):\t",			"".join(map(str, aprovadas))
print "Vetor de cursáveis (DC):\t",			"".join(map(str, cursaveis))
print "Número de grades possíveis:\t",	2 ** cursaveis.sum() - 1
# print "# de grades possíveis:\t",		comb(cursaveis.sum(), 5, exact=True)
print dados.disciplinas[0]