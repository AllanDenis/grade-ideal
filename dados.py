#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.sparse import *
from scipy import linalg
import disciplina

# Para melhor legibilidade
aulas_por_dia = 4
dias_por_semana = 5
qtd_disciplinas = 44
seg, ter, qua, qui, sex = range(dias_por_semana)
aula1, aula2, aula3, aula4 = range(aulas_por_dia)

# Matriz de dependências (MD), incluindo a disciplina nula (se o elemento a_ij == 1,
# então a disciplina i depende da disciplina j,
# caso contrário, a_ij == 0).

#TODO: escolher o formato de matriz esparsa (http://docs.scipy.org/doc/scipy/reference/sparse.html#sparse-matrix-classes). 
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

# MD = csr_matrix(MD)

# Grade semanal de aulas (4 aulas x 5 dias). 
G = np.zeros((aulas_por_dia, dias_por_semana), dtype="int")

# Matriz de aprovação (MA): lista de disciplinas em que o aluno foi aprovado
MA = csr_matrix(np.array(map(int, "111111111111111111011111110110000001000000011")))
# MA = csr_matrix(np.array(map(int, "100000000000000000000000000000000000000000000")))
MA = csr_matrix(np.array(map(int, "101101011110110001001000000000000000000000011")))

disciplinas = []
disc_inativas = set([0, 36, 41, 42])
 
# Lista de disciplinas + 1 disciplina nula
for i in range(qtd_disciplinas + 1): disciplinas.append(disciplina.Disciplina())

disciplinas[1] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (seg,seg,ter,ter))), shape=(aulas_por_dia, dias_por_semana))	#ORGE
disciplinas[2] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (ter,ter,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#ALGO
disciplinas[3] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (qua,qua,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#INGL
disciplinas[4] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (qui,qui,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#CALC
disciplinas[5] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (seg,seg,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#PRSI
disciplinas[6] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (ter,ter,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#ESTD
disciplinas[7] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (qua,qua,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#ESTA
disciplinas[8] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (sex,sex,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#ARQC
disciplinas[9] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (seg,seg,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#SOPE
disciplinas[10] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (seg,seg,ter,ter))), shape=(aulas_por_dia, dias_por_semana))	#FNBD
disciplinas[11] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (ter,ter,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#PROO
disciplinas[12] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (ter,ter,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#RECO
disciplinas[13] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (seg,seg,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#APBD
disciplinas[14] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (qua,qua,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#IALI
disciplinas[15] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (seg,seg,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#FPIN
disciplinas[16] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (ter,ter,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#APRS
disciplinas[17] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (seg,seg,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#RHFI
disciplinas[18] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (seg,seg,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#PAVI
disciplinas[19] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (ter,ter,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#MEPC
disciplinas[20] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (qui,qui,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#LMMD
disciplinas[21] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (seg,seg,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#PJIN1
disciplinas[22] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (ter,ter,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#INHC
disciplinas[23] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (seg,seg,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#GEPJ
disciplinas[24] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (qua,qua,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#TABD
disciplinas[25] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (ter,ter,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#GESINF
disciplinas[26] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (ter,ter,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#GDSW
disciplinas[27] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (ter,ter,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#INCO
disciplinas[28] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (seg,seg,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#PRMK
disciplinas[29] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (qua,qua,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#SIGE
disciplinas[30] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (seg,seg,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#LSOR
disciplinas[31] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula1,aula2), (ter,ter,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#FILO
disciplinas[32] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (seg,seg,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#PJIN2
disciplinas[33] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (seg,seg,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#SIAD
disciplinas[34] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (qua,qua,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#TESI1
disciplinas[35] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (qui,qui,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#INAR
# disciplinas[36] = None	#COGR
disciplinas[37] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula1,aula2), (ter,ter,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#SOCI
disciplinas[38] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (seg,seg,qua,qua))), shape=(aulas_por_dia, dias_por_semana))	#EMPR
disciplinas[39] = csr_matrix(((1,1,1,1), ((aula3,aula4,aula3,aula4), (seg,seg,qui,qui))), shape=(aulas_por_dia, dias_por_semana))	#TESI2
disciplinas[40] = csr_matrix(((1,1,1,1), ((aula1,aula2,aula3,aula4), (qui,qui,sex,sex))), shape=(aulas_por_dia, dias_por_semana))	#GOTI
# disciplinas[41] = None	#TCC
# disciplinas[42] = None	#ETIC
disciplinas[43] = csr_matrix(((1,1		), ((aula1,aula2				), (ter,ter				))), shape=(aulas_por_dia, dias_por_semana))	#DIRL
disciplinas[44] = csr_matrix(((1,1		), ((aula3,aula4				), (ter,ter				))), shape=(aulas_por_dia, dias_por_semana))	#LIBR