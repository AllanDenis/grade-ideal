#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import linalg, sparse

aulas_por_dia = 4
dias_por_semana = 5
qtd_disciplinas = 44

# Matriz de dependências (MD), incluindo a disciplina nula (se o elemento a_ij == 1,
# então a disciplina i depende da disciplina j,
# caso contrário, a_ij == 0).
MD = np.array([
	map(int, "011111011100001001011010000010011011111000111"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000100010000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000010000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000001000100000000000100000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000100000000000000000100000000000000"),
	map(int, "000000000000010000000000100000000000000000000"),
	map(int, "000000000000000010000101000000000000000000000"),
	map(int, "000000000000000000000000000000100000000000000"),
	map(int, "000000000000000000000000100000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000100000000000000000000000000"),
	map(int, "000000000000000000000100000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000001000"),
	map(int, "000000000000000000000000001000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000001000000000000010000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000001000000000000000"),
	map(int, "000000000000000000000000000000000100000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000100000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000"),
	map(int, "000000000000000000000000000000000000000000000")
])

# Grade semanal de aulas (4 aulas x 5 dias). 
G = np.zeros((aulas_por_dia, dias_por_semana), dtype="int")

# Matriz de aprovação (MA): lista de disciplinas em que o aluno foi aprovado
MA = np.array(map(int, "111111111111111111011111110110000001000000011"))

# Para melhor legibilidade
seg, ter, qua, qui, sex = range(dias_por_semana)
aula1, aula2, aula3, aula4 = range(aulas_por_dia)


# Lista de disciplinas + 1 disciplina nula
disciplinas = [
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#ORGE
		map(int, "00000"),
		map(int, "00000"),
		map(int, "11000"),
		map(int, "11000")
	]),
	np.array([	#ALGO
		map(int, "01010"),
		map(int, "01010"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#INGL
		map(int, "00100"),
		map(int, "00100"),
		map(int, "00001"),
		map(int, "00001")
	]),
	np.array([	#CALC
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	np.array([	#NULA
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000"),
		map(int, "00000")
	]),
	
]
