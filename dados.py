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
# MA = csr_matrix(np.array(map(int,	"100000000000000000000000000000000000000000000")))
# MA = csr_matrix(np.array(map(int, "111111111111111111011111110110000001000000011")))	# Allan Denis
# MA = csr_matrix(np.array(map(int, "111111111111111111111000000000000000000000000"))) # Arthur Novaes, Leilton
# MA = csr_matrix(np.array(map(int, "111111111111111111101111110000100000010000011"))) # Hercílio
# MA = csr_matrix(np.array(map(int, "111111111101101111111011000000000010000000000"))) # Ernande
# MA = csr_matrix(np.array(map(int, "111111111101101111111011000000000010000000000"))) # Bruno Antonelly
MA = csr_matrix(np.array(map(int, "101101111111110101001011100110100001000000000"))) # Lucas
# MA = csr_matrix(np.array(map(int, "111101111111111111111111100000100000000000011"))) # Denis Vieira
# MA = csr_matrix(np.array(map(int, "111101111111110110101011100000100000000000010"))) # Kyo




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

'''
Colunas: disciplinas
Linhas: aulas em ordem cronológica (seg1-4,ter1-4, etc.)
Elementos: {
	0: sem aula da disciplina nesse dia
	1: com aula da disciplina nesse dia
	2: disciplina inativa ou não ofertada 
}
'''
horario = np.array([
	map(int, "200001000100000101000100000010000100201002200"),
	map(int, "200001000100000101000100000010000100201002200"),
	map(int, "210000000010010000100001000000101000200102200"),
	map(int, "210000000010010000100001000000101000200102200"),
	map(int, "201000100001000000010000011000010000200002210"),
	map(int, "201000100001000000010000011000010000200002210"),
	map(int, "210000000010100010000010000100000000210002201"),
	map(int, "210000000010100010000010000100000000210002201"),
	map(int, "200100000100001010000001000001010010200002200"),
	map(int, "200100000100001010000001000001010010200002200"),
	map(int, "200001010000000100010000100000100010201002200"),
	map(int, "200001010000000100010000100000100010201002200"),
	map(int, "201000100001000001000110000010001000200012200"),
	map(int, "201000100001000001000110000010001000200012200"),
	map(int, "200010010000001000001000001000000001200102200"),
	map(int, "200010010000001000001000001000000001200102200"),
	map(int, "200010001000010000001000010001000001210002200"),
	map(int, "200010001000010000001000010001000001210002200"),
	map(int, "200100001000100000100000100100000100200012200"),
	map(int, "200100001000100000100000100100000100200012200")
]).T

# help(horario)



