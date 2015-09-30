#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.sparse import csr_matrix
import numpy as np

aulas_por_dia = 4
dias_por_semana = 5
qtd_disciplinas = 44
seg, ter, qua, qui, sex = range(dias_por_semana)
aula1, aula2, aula3, aula4 = range(aulas_por_dia)

# Disciplinas pertencentes a um curso
class Disciplina():
	# Para melhor legibilidade
	def __init__(self, id, nome, sigla, periodo, horario):
		self.id = id
		self.nome = nome
		self.sigla = sigla
		self.periodo = periodo
		self.horario = horario
		# self.ativa = True
		
