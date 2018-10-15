# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/08/06 19:03:53 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from LineLexer import LineLexer
from Expr import Expr
from Fact import Fact

class Graph:
	def __init__(self, config):
		self.config = config
		self._create_nodes()
		self._clean_unused_nodes()
		self._add_tokens()

	def _create_nodes(self):
		self.data = {x:None for x in self.config.facts}
		self.config.graph = self.data
		for line in self.config.lines:
			self._create_node(line)

	def _create_node(self, line):
		for char in line.data:
			if char in self.config.facts:
				if not self.data[char]:
					self.data[char] = Fact(char)
				elif line.type == LineLexer.FACT_TYPE:
					self.data[char].make_true()

	def _clean_unused_nodes(self):
		for key in list(self.data.keys()):
			if not self.data[key]:
				del self.data[key]

	def _add_tokens(self):
		for line in self.config.lines:
			if line.type == LineLexer.RULE_TYPE:
				char = line.data.split(self.config.implies_sub)[1]
				self.data[char].add_true(line.token)

	def solve(self):
		# Print before
		self._tmp_display()

		# Algo. Currently only checks once, but should check until satisfactory.
		for key, fact in self.data.items():
			print("\x1b[38;2;255;125;0mINVESTIGATE: %s\x1b[0m" % fact.name)
			fact.contradiction()
			fact.check(self.config)
			fact.display()
			print("")

		# Print after
		self._tmp_display()

		self._display()

	def _tmp_display(self):	 							#TEMPORARY - DELETE
		for key, fact in self.data.items():				#TEMPORARY - DELETE
			fact.display()								#TEMPORARY - DELETE
		print("\n")										#TEMPORARY - DELETE

	# Displays original input, but prints facts in correct colour.
	def _display(self):
		for line in self.config.lines:
			comment = 0
			for char in line.string:
				if char == "#":
					comment = 1
				if char in self.config.facts and not comment:
					print(self.config.graph[char].letter(), end="")
				else:
					print(char, end ="")
			print()
