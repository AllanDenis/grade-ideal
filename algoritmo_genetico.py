#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
# from matricula import grade_pontuacao, grade_valida

class Genetico():
	'''Implementação das funçẽos de algoritmo genético.'''
	taxa_mutacao = 5 #%
	populacao = 200
	
	def populacao_inicial(self, num_individuos, tam_genoma):
		'''Retorna uma populacao com genomas aleatórios.'''
		assert num_individuos > 0, "O tamanho da população deve ser maior que zero."
		assert tam_genoma > 0, "O tamanho do genoma deve ser maior que zero."
		int_aleatorio = lambda x: randint(0,1)
		for i in range(num_individuos):
			yield map(int_aleatorio, range(tam_genoma))
		
	def fitness(self, genoma):
		'''Função que mede a adequação do genoma ao meio.'''
		assert set(genoma) == set([0,1]), "O genoma deve ser binário."
		if grade_valida(genoma):
			return grade_pontuacao(genoma)
		return 0
	
	def crossover(self, pai1, pai2): 
		'''Cruza dois genomas em um ponto aleatório, segundo a taxa de mutação definida.'''
		assert len(pai1) == len(pai2), "Os pais devem ter o mesmo tamanho."
		assert len(pai1) > 0 and len(pai2) > 0, "Os genomas não podem ser nulos."
		assert set(pai1) == set(pai2) == set([0,1]), "Os genomas dos pais devem ser binários."
		ponto_de_corte = randint(0, len(pai1))
		filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:] #Crossover
		filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:]
		filho1 = self.mutacao(filho1, self.taxa_mutacao)
		filho2 = self.mutacao(filho2, self.taxa_mutacao)
		return filho1, filho2

	def mutacao(self, genoma, taxa_mutacao):
		'''Altera o genoma segundo a taxa de mutação informada'''
		assert len(genoma) > 0, "O genoma não pode ser nulo."
		assert taxa_mutacao >= 0, "A taxa de mutação não pode ser negativa."
		altera_genes = lambda x: x if randint(0, 100) > taxa_mutacao else not x
		return map(altera_genes, genoma)
	
	def selecao(self, populacao, func_fitness, perc_corte):
		'''Retorna os melhores membros da população segundo a
		função fitness, limitado ao percentual de corte.'''
		assert len(populacao) > 0, "O tamanho da população deve ser maior que zero."
		assert perc_corte > 0, "O percentual de corte não pode ser negativo."
		limite = int(len(populacao) * (1 - perc_corte/100.))
		print limite
		for i in xrange(limite):
			yield sorted(populacao, key=func_fitness, reverse=True)[i]

	def procriar(self, populacao, num_individuos):
		'''Preenche a população com o número de indivíduos desejado.'''
		assert len(populacao) > 0, "O tamanho da população deve ser maior que zero."
		