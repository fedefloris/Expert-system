# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/07/27 14:04:12 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Fact:
	def __init__(self, fact):
		self.fact = fact
		self.init_false = 1
		self.true = 0
		self.false = 0
		self.ambig = 0

		# Array of conditions
		self.trueif = []
		self.falseif = []

	def force_true(self):
		init_false = 0
		self.true = 1
		self.contradicts()

	def make_true(self):
		self.true = 1
		self.contradicts()

	def make_false(self):
		self.false = 1
		self.contradicts()

	def make_ambig(self):
		self.ambig = 1

	def add_true(self, condition):
		self.trueif.append(condition)

	def add_false(self, condition):
		self.falseif.append(condition)

	# Checks that a fact is not contradictory
	def contradicts(self):
		if self.true and self.false:
			print("%s is a contradiction" % self.fact)
			exit(1)

	# Displays 'final' string to declare sstate of facts.
	def display(self):
		if self.true:
			print("%s is true" % self.letter())
		elif self.false:
			print("%s is false" % self.letter())
		elif self.ambig:
			print("%s is ambiguous" % self.letter())
		elif self.init_false:
			print("%s is false" % self.letter())

	# Returns fact's letter appropriately coloured.
	def letter(self):
		if self.true:
			return ("\x1b[32m%s\x1b[0m" % self.fact)
		elif self.false:
			return ("\x1b[31m%s\x1b[0m" % self.fact)
		elif self.ambig:
			return ("\x1b[33m%s\x1b[0m" % self.fact)
		elif self.init_false:
			return ("\x1b[31m%s\x1b[0m" % self.fact)

	def evaluate(self, condition, config):
		if config.graph[condition].true:
			print("Evaluated", condition, "as TRUE")
			return (1)
		else:
			print("Evaluated", condition, "as FALSE")
			return (0)

	def investigate(self, config):
		if not self.true:
			for condition in self.trueif:
				if type(condition) is str and self.evaluate(condition, config):
					print(condition, "makes", self.fact, "true")
					self.make_true()
				if type(condition) is Fact:
					condition.investigate(config)
					if condition.true:
						print(condition.fact, "makes", self.fact, "true")
						self.make_true()


def graph(config):
	def tmp_display(config): 							#TEMPORARY - DELETE
		for key, fact in config.graph.items():			#TEMPORARY - DELETE
			if fact:									#TEMPORARY - DELETE
				fact.display()							#TEMPORARY - DELETE
		print("\n")										#TEMPORARY - DELETE

	def create_graph(config):
		for line in config.lines:
			for char in line.data:
				if char in config.facts and not config.graph[char]:
					config.graph[char] = Fact(char)
				if char in config.facts and line.type == 3:
					config.graph[char].force_true()
		keys = list(config.graph.keys())
		for key in keys:
			if not config.graph[key]:
				del config.graph[key]


	create_graph(config)

	config.graph["L"].add_true("E")
	config.graph["L"].add_true("A")
	config.graph["L"].add_false("E")
	config.graph["G"].add_true("A")

	bracket = Fact("(Bracket inside K)")
	bracket.add_true("C")
	bracket.add_true("B")
	config.graph["K"].add_true(bracket)

	tmp_display(config) #

	for key, fact in config.graph.items():
		fact.investigate(config)

	tmp_display(config) #
