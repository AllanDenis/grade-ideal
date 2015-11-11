#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.sparse import csr_matrix
import numpy as np
import modelo

aulas_por_dia = 4
dias_por_semana = 5
qtd_disciplinas = 44

class Disciplina():
	'''Disciplinas pertencentes a um curso'''
	def __init__(self):
		self.id			=	modelo.Disciplina.select().id
		self.nome		=	d.nome
		self.sigla		=	d.sigla
		self.periodo	=	d.periodo
		self.ativa		=	d.ativa
		self.horario = None


	def __str__():
		string = self.id
		string += ": %s" % self.sigla
		string += " (%s," % self.nome
		string += " %sº período)" % self.sigla
		return string
