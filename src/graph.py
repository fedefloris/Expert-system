# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/07/26 16:47:40 by dhojt            ###   ########.fr        #
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
		self.trueif.append = condition

	def add_false(self, condition):
		self.falseif.append = condition

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


# Dear Federico. The below is proof of concept LOL :D.
#
# Create array of 26 and stores facts in the array (A: array[0] to Z: array[25]
# If it is initially true, it is set to true.
# I then (cheat a little) and suggest that the only rules are:
#         A => L
#         E => L
# I then effectively backward chain by one position, and check if E and A are true.
# If E or A are true, I make L true.
# Of course it will be prettier (Obviously) What do you think?
#
# Lots of Hugs
#
# Dav. <3

def graph(config):
	array = [None] * 26
	for line in config.lines:
		for char in line.data:
			if char in config.facts and not array[ord(char) - 65]:
				array[ord(char) - 65] = Fact(char)
			if char in config.facts and line.type == 3:
				array[ord(char) - 65].force_true()
	array[ord("L") - 65].trueif.append("E")
	array[ord("L") - 65].trueif.append("A")
	for fact in array:
		if fact:
			fact.display()
	print("\n\n\n")
	for fact in array:
		if fact:
			for condition in fact.trueif:
				if array[ord(condition) - 65].true == 1:
					fact.make_true()
					print(condition, "makes", fact.fact, "true")
	for fact in array:
		if fact:
			fact.display()
