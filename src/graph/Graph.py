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
		self._add_tokens()

	def _create_nodes(self):
		self.data = {x:Fact(x) for x in self.config.facts}
		for line in self.config.lines:
			if line.type == LineLexer.FACT_TYPE:
				self._make_nodes_true(line)
		self.config.graph = self.data

	def _make_nodes_true(self, line):
		for fact in line.data:
			self.data[fact].make_true()

	def _add_tokens(self):
		for line in self.config.lines:
			if line.type == LineLexer.RULE_TYPE:
				conclusion = line.data.split(self.config.implies_sub)[1]
				self._add_token(line, conclusion)

	def _add_token(self, line, conclusion):
		facts = conclusion.split(self.config.op_and)
		for fact in facts:
			self.data[fact].add_true(line.token)

	def induce(self):
		# Print before
		self._tmp_display()

		# Algo runs until there no changes
		changed = True
		while changed:
			changed = False
			for key, fact in self.data.items():
				fact_status = fact.true + 2 * fact.false + 3 * fact.ambig
				print("\x1b[38;2;255;125;0mINVESTIGATE: %s\x1b[0m" % fact.name)
				fact.contradiction()
				fact.check(self.config)
				fact.display()
				print("")
				if fact_status != fact.true + 2 * fact.false + 3 * fact.ambig:
					changed = True

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
