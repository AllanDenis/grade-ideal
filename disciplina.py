#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.sparse import csr_matrix
import numpy as np

aulas_por_dia = 4
dias_por_semana = 5
qtd_disciplinas = 44

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
		
	def __str__():
		pass