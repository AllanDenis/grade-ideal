#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from matricula import grade_pontuacao, grade_valida

class Genetico():
	'''Implementação das funçẽos de algoritmo genético.'''
	taxa_mutacao = 5 #%
	populacao = 200
	
	def populacao_inicial(self, num_individuos, tam_genoma):
		'''Retorna uma populacao com genomas aleatórios.'''
		int_aleatorio = lambda x: randint(0,1)
		for i in range(num_individuos):
			yield map(int_aleatorio, range(tam_genoma))
		
	def fitness(self, genoma):
		'''Função que mede a adequação do genoma ao meio.'''
		if grade_valida(genoma):
			return grade_pontuacao(genoma)
		return 0
	
	def crossover(self, pai1, pai2): 
		'''Cruza dois genomas em um ponto aleatório, segundo a taxa de mutação definida.'''
		if len(pai1) != len(pai2):	return None
		ponto_de_corte = randint(0, len(pai1))
		filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:] #Crossover
		filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:]
		filho1 = self.mutacao(filho1, self.taxa_mutacao)
		filho2 = self.mutacao(filho2, self.taxa_mutacao)
		return filho1, filho2

	def mutacao(self, genoma, taxa_mutacao):
		'''Altera o genoma segundo a taxa de mutação informada'''
		altera_genes = lambda x: x if randint(0, 100) > taxa_mutacao else 1 - x
		return map(altera_genes, genoma)
	
	def selecao(self, populacao, func_fitness, perc_corte):
		'''Retorna os melhores membros da população segundo a
		função fitness, limitado ao percentual de corte.'''
		limite = int(len(populacao) * (1 - perc_corte/100.))
		print limite
		for i in xrange(limite):
			yield sorted(populacao, key=func_fitness, reverse=True)[i]

help(g)