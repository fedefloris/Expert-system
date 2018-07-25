# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/07/25 18:25:20 by dhojt            ###   ########.fr        #
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
	
	def make_true(self):
		self.true = 1

	def make_false(self):
		self.false = 1

	def make_ambig(self):
		self.ambig = 1

	def contradict(self):
		if self.true and self.false:
			return 1
		else:
			return 0
	
	def display(self):
		if self.contradict():
			print("%s is a contradiction" % self.fact)
		elif self.true:	
			print("%s is true" % self.letter())
		elif self.false:
			print("%s is false" % self.letter())
		elif self.ambig:
			print("%s is ambiguous" % self.letter())
		elif self.init_false:
			print("%s is false" % self.letter())

	def letter(self):
		if self.true:	
			return ("\x1b[32m%s\x1b[0m" % self.fact)
		elif self.false:
			return ("\x1b[31m%s\x1b[0m" % self.fact)
		elif self.ambig:
			return ("\x1b[33m%s\x1b[0m" % self.fact)
		elif self.init_false:
			return ("\x1b[31m%s\x1b[0m" % self.fact)
		

a = Fact("A")
a.display()
a.letter()
a.make_ambig()
a.display()
a.letter()
a.force_true()
a.display()
a.letter()
