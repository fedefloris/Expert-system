# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    InferenceEngine.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/08/06 19:03:53 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Fact import Fact
from LineLexer import LineLexer

class InferenceEngine:
	def __init__(self, config):
		# Enable debug output only after evaluating the graph
		self.debug_output = False
		config.debug = self.debug
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
			self.data[fact].make_true(self.config)

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
		# Algorithm runs until there are no changes
		changed = True
		while changed:
			changed = self._traverse_graph()
		# Traverse one more time if debug output is enabled
		self.debug_output = self.config.verbose
		queries = self._get_queries();
		if self.debug_output:
			self._traverse_queries(queries)
		self.debug_output = True
		if self.config.origin_input:
			self._display()
		else:
			self._display_facts(queries)

	def _traverse_graph(self):
		changed = False
		for key, fact in self.data.items():
			fact_status = fact.true + fact.false + fact.ambig
			fact.contradiction(self.config)
			fact.check(self.config)
			if fact_status != fact.true + fact.false + fact.ambig:
				changed = True
		return (changed)

	def _get_queries(self):
		queries_set = set()
		queries = []
		for line in self.config.lines:
			if line.type == LineLexer.QUERY_TYPE:
				self._add_queries(line, queries, queries_set)
		return (queries)

	def _add_queries(self, line, queries, queries_set):
		for query in line.data:
			if query not in queries_set:
				queries_set.add(query)
				queries.append(query)

	def _traverse_queries(self, queries):
		for query in queries:
			fact = self.data[query];
			self.debug(f"\x1b[38;2;255;125;0mINVESTIGATE: {fact.name}\x1b[0m")
			fact.contradiction(self.config)
			fact.check(self.config)
			fact.display(self.config)
			self.debug("")

	# Displays original input, but prints facts in correct colour
	def _display(self):
		for line in self.config.lines:
			comment = 0
			for char in line.string:
				if char == "#":
					comment = 1
				if char in self.config.facts and not comment:
					print(self.config.graph[char].get_letter(), end="")
				else:
					print(char, end ="")
			print()

	# Displays facts in correct colour
	def _display_facts(self, queries):
		for query in queries:
			fact = self.data[query];
			fact.display(self.config)

	def debug(self, string, end="\n"):
		if self.debug_output:
			print(string, end=end)
