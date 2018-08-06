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

# Parent class of all expressions
class Condition:
	def __init__(self, name):
		self.name = name

		self.true = 0
		self.ambig = 0

		self.trueif = []

	def add_true(self, condition):
		self.trueif.append(condition)



# Facts can be true, false, ambiguous or contradictory (true and false).
# Ambiguous is overridden by true or false.
class Fact(Condition):
	def __init__(self, name):
		Condition.__init__(self, name)
		self.false = 0

		self.falseif = []

	def add_false(self, condition):
		self.falseif.append(condition)

	def make_true(self):
		self.true = 1
		self.contradiction()

	def make_false(self):
		self.false = 1
		self.contradiction()

	def make_ambig(self):
		self.ambig = 1

	def contradiction(self):
		if self.true and self.false:
			print("%s is a contradiction" % self.name)
			exit(1)
			
	def check(self, config):
		for condition in self.trueif:
			condition.check(config)
			if condition.valid:
				print(condition.name, "makes", self.name, "true")
				self.make_true()
			if condition.ambig:
				print(condition.name, "makes", self.name, "ambig")
				self.make_ambig()
		for condition in self.falseif:
			condition.check(config)
			if condition.valid:
				print(condition.name, "makes", self.name, "false")
				self.make_false()

	# Displays string to declare sstate of fact.
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

	# self.check for And inherrits from this.
	def check(self, config):
		true = 1
		ambig = 0
		for condition in self.trueif:
			condition.check(config)
			if condition.valid:
				print(condition.name, "is valid inside", self.name)
			elif not condition.valid and not condition.ambig:
				print(condition.name, "is invalid inside", self.name)
				true = 0
				break
			if condition.ambig:
				true = 0
				ambig = 1
		if true:
			self.make_true()
		elif ambig:
			self.make_ambig()
		else:
			self.make_false()
	
	def make_true(self):
		self.true = 1
		self.ambig = 0
		print("Evaluated", self.name, "as TRUE", type(self))
		if not self.negative:
			print(self.name, "is Valid")
			self.valid = 1
		else:
			print(self.name, "is Invalid")
			self.valid = 0

	def make_false(self):
		print("Evaluated", self.name, "as FALSE", type(self))
		self.true = 0
		self.ambig = 0
		if self.negative:
			print(self.name, "is Valid")
			self.valid = 1
		else:
			print(self.name, "is Invalid")
			self.valid = 0

	def make_ambig(self):
		print("Evaluated", self.name, "as AMBIGUOUS", type(self))
		self.true = 0
		self.ambig = 1
		self.valid = 0
		print(self.name, "is Invalid")



class Bracket(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)



class And(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)



class Or(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)

	def check(self, config):
		true = 0
		ambig = 0
		for condition in self.trueif:
			condition.check(config)
			if condition.valid:
				self.make_true()
				true = 1
				print(condition.name, "is valid inside", self.name)
				break
			else:
				print(condition.name, "is invalid inside", self.name)
			if condition.ambig:
				ambig = 1
		if ambig:
			self.make_ambig()
		elif not true:
			self.make_false()
			


class Xor(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)

	def check(self, config):
		valid_count = 0
		for condition in self.trueif:
			condition.check(config)
			if condition.valid:
				valid_count += 1
				if valid_count > 1:
					break
			elif condition.ambig:
				self.make_ambig()
				break
		if valid_count == 1 and not self.ambig:
			self.make_true()
		if not valid_count == 1 and not self.ambig:
			self.make_false()



# Base is the lowest level of expression. It's trueif list contains one
# element which is a character string (Fact Letter).
# It does not search recursively.
class Base(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)

	def check(self, config):
		if config.graph[self.trueif[0]].true:
			self.make_true()
		elif config.graph[self.trueif[0]].ambig and not config.graph[self.trueif[0]].false:
			self.make_ambig()
		else:
			self.make_false()



def graph(config):
	def tmp_display(config): 							#TEMPORARY - DELETE
		for key, fact in config.graph.items():			#TEMPORARY - DELETE
			fact.display()								#TEMPORARY - DELETE
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

	"""
	def expand_expr(config):
		for key, fact in config.graph.items():
			for condition in fact.trueif:
				condition.brackets(config)
			for condition in fact.falseif:
				condition.brackets(config)
	"""


	create_graph(config)
	add_expr(config)
	#expand_expr(config)

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

	config.graph["C"].trueif[0].add_true(c)
	config.graph["F"].trueif[0].add_true(f)
	config.graph["I"].trueif[0].add_true(i)
	config.graph["L"].trueif[0].add_true(l)

	# Print before
	tmp_display(config)

	# Algo. Currently only checks once, but should check until satisfactory.
	for key, fact in config.graph.items():
		print("\x1b[38;2;255;125;0mINVESTIGATE: %s\x1b[0m" % fact.name)
		fact.contradiction()
		fact.check(config)
		fact.display()
		print("")

	# Print after
	tmp_display(config)

	config.display()
