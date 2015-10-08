#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bintrees import BinaryTree as bt

# Árvore binária para implementação do algoritmo branch-and-cut

class Arvore():
	def __init__(self):
		self.filhos = {}
		self.pai = None
		self.dado = None
	
	def test(self):
		print self 

