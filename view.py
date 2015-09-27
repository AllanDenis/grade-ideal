#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from bokeh.charts import Histogram
from bokeh.charts import defaults, vplot, hplot, show, output_file

# Visualização dos dados gerados
class View():
	def __init__(self):
		self.dados = None
	
	def exibir(self):
		print "Inicio: exibir()"
		for i in self.dados.keys():
			if len(self.dados[i]) > 0: continue
			else: return
		defaults.width, defaults.height = 400, 300
		# prepare some data
		# input options
		hist_pontuacao = Histogram(self.dados["pontos"],
						title="Grades por pontuação",
						xlabel="Pontuação",
						ylabel="Número de grades",
						responsive=True,
						bins=30)

		hist_tamanho = Histogram(self.dados["tamanhos"],
						title="Grades por quantidade de disciplinas",
						xlabel="Número de disciplinas",
						ylabel="Número de grades",
						responsive=True,
						bins=8)
		
		hist_pop = Histogram(self.dados["popularidade"],
						title="Ocorrências da disciplina x",
						xlabel="Disciplina",
						ylabel="Ocorrências nas grades",
						responsive=True,
						bins=46)
		
		output_file("html/histograms.html")

		show(hplot(	hist_pontuacao,
					hist_tamanho,
					hist_pop
		))
		
		print "Fim: exibir()"
		

