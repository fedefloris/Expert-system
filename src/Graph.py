# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/08/03 00:30:53 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Condition:
	def __init__(self, name):
		self.name = name

		self.true = 0
		self.ambig = 0

		self.trueif = []

	def add_true(self, condition):
		self.trueif.append(condition)

	def make_ambig(self):
		self.ambig = 1

################################################

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

		# Iterates truif conditions recursively.
		for condition in self.trueif:

			# Exit case for recursion (if lowest fact is true)
			if type(condition) is str and self.evaluate(condition, config):
				self.make_true()

			# Recursive call
			if not type(condition) is str:
				condition.investigate(config)
				if condition.valid:
					print(condition.name, "makes", self.name, "true")
			self.make_true()


class Fact(Condition):
	def __init__(self, name):
		Condition.__init__(self, name)
		self.false = 0

		self.falseif = []

	def add_false(self, condition):
		self.falseif.append(condition)

	# Checks that a fact is not contradictory
	def check_valid(self):
		if self.true and self.false:
			print("%s is a contradiction" % self.name)
			exit(1)

	def make_true(self):
		self.true = 1
		self.check_valid()

	def make_false(self):
		self.false = 1
		self.check_valid()

	# Displays 'final' string to declare sstate of facts.
	def display(self):
		if self.true:
			print("%s is true" % self.letter())
		elif self.ambig and not self.false:
			print("%s is ambiguous" % self.letter())
		else:
			print("%s is false" % self.letter())

	# Returns fact's letter appropriately coloured.
	def letter(self):
		if self.true:
			return ("\x1b[32m%s\x1b[0m" % self.name)
		elif self.ambig and not self.false:
			return ("\x1b[33m%s\x1b[0m" % self.name)
		else:
			return ("\x1b[31m%s\x1b[0m" % self.name)


class Expr(Condition):
	def __init__(self, name):
		Condition.__init__(self, name)
		self.negative = 0;
		self.valid = 0

	def make_negative(self):
		self.negative = 1


class And(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)
	
	def check_valid(self):
		valid = 1
		for condition in self.trueif:
			if not condition.valid:
				valid = 0
		if valid:
			self.valid = 1
			


class Or(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)


class Xor(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)


class Base(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)

	def make_true(self):
		if self.trueif[0]:
			self.true = 1
		self.check_valid()

	def check_valid(self):
		print("Checking validity", self.name)
		if not self.negative and self.true:
			self.valid = 1
			print(self.name, "is valid")


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
					config.graph[char].make_true()
		keys = list(config.graph.keys())
		for key in keys:
			if not config.graph[key]:
				del config.graph[key]

	def add_expr(config):
		for line in config.lines:
			if line.type == 2:
				char = line.data.split(config.implies_sub)[1]
				data = line.data.split(config.implies_sub)[0]
				if not char.count(config.op_neg):
					config.graph[char].add_true(Expr(data))
				else:
					config.graph[char.split(config.op_neg)[1]].add_false(Expr(data))

	create_graph(config)
	add_expr(config)

	# Simulate Ands inside Expr.
	c = And("A+B")
	f = And("D+E")
	i = And("G+H")
	l = And("J+K")

	c_a = Base("A")
	c_b = Base("B")
	f_d = Base("D")
	f_e = Base("E")
	i_g = Base("G")
	i_h = Base("H")
	l_j = Base("J")
	l_k = Base("K")

	c_a.add_true("A")
	c_b.add_true("B")
	f_d.add_true("D")
	f_e.add_true("E")
	i_g.add_true("G")
	i_h.add_true("H")
	l_j.add_true("J")
	l_k.add_true("K")

	c.add_true(c_a)
	c.add_true(c_b)
	f.add_true(f_d)
	f.add_true(f_e)
	i.add_true(i_g)
	i.add_true(i_h)
	l.add_true(l_j)
	l.add_true(l_k)

	config.graph["C"].add_true(c)
	config.graph["F"].add_true(f)
	config.graph["I"].add_true(i)
	config.graph["L"].add_true(l)

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
