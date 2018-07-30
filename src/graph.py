# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/07/30 02:35:27 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Expr:
	def __init__(self, name):
		self.name = name
		self.true = 0
		self.false = 0

		# Array of conditions
		self.trueif = []
		self.falseif = []

	def make_true(self):
		self.true = 1
		self.contradicts()

	def make_false(self):
		self.false = 1
		self.contradicts()

	def add_true(self, condition):
		self.trueif.append(condition)

	def add_false(self, condition):
		self.falseif.append(condition)

	# Checks that a fact is not contradictory
	def contradicts(self):
		if self.true and self.false:
			print("%s is a contradiction" % self.name)
			exit(1)

	# Evaluates lowest condition (string) to see if it is valid.
	def evaluate(self, condition, config):
		if config.graph[condition].true:
			print("Evaluated", condition, "as TRUE")
			return (1)
		else:
			print("Evaluated", condition, "as NOT TRUE")
			return (0)

	# Checks conditions of each fact recursively..
	##  Need to make one for falseif once this is concrete.
	def investigate(self, config):

		# Only tries to make_true if it is not already true.
		if not self.true:

			# Iterates truif conditions recursively.
			for condition in self.trueif:

				# Exit case for recursion (if lowest fact is true)
				if type(condition) is str and self.evaluate(condition, config):
					print(condition, "makes", self.name, "true")
					self.make_true()
					break

				# Recursive call
				if type(condition) is Fact:
					condition.investigate(config)
					if condition.true:
						print(condition.name, "makes", self.name, "true")
						self.make_true()
						break


class Fact(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)
		self.init_false = 1
		self.ambig = 0

	def force_true(self):
		init_false = 0
		self.true = 1
		self.contradicts()

	def make_ambig(self):
		self.ambig = 1

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
			return ("\x1b[32m%s\x1b[0m" % self.name)
		elif self.false:
			return ("\x1b[31m%s\x1b[0m" % self.name)
		elif self.ambig:
			return ("\x1b[33m%s\x1b[0m" % self.name)
		elif self.init_false:
			return ("\x1b[31m%s\x1b[0m" % self.name)



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

	# Simulate conditions inside facts.
	config.graph["L"].add_true("E")
	config.graph["L"].add_true("A")
	config.graph["L"].add_true("B")
	config.graph["L"].add_false("E")
	config.graph["G"].add_true("A")
	config.graph["E"].add_true("C")

	# Simulates 'or' statement in a bracket.
	bracket_2 = Fact("Lower bracket")
	bracket_2.add_true("C")
	bracket_2.add_true("B")

	# Simmulates above bracket inside a higher 'or' bracket.
	bracket = Fact("Upper bracket")
	bracket.add_true("F")
	bracket.add_true(bracket_2)

	# Puts the above upper bracket (with bracket_2 inside) inside K.
	config.graph["K"].add_true(bracket)

	# Print before
	tmp_display(config)

	# Algo. Currently only checks once, but should check until satisfactory.
	for key, fact in config.graph.items():
		print("\x1b[38;2;255;125;0mINVESTIGATE: %s\x1b[0m" % fact.name)
		fact.investigate(config)
		fact.display()
		print("")

	# Print after
	tmp_display(config)
