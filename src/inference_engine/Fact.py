# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Fact.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Condition import Condition

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

	# Returns fact's letter appropriately coloured.
	def get_letter(self):
		if self.true:
			return ("\x1b[32m%s\x1b[0m" % self.name)
		elif self.ambig and not self.false:
			return ("\x1b[33m%s\x1b[0m" % self.name)
		return ("\x1b[31m%s\x1b[0m" % self.name)

	# Displays string to declare state of fact.
	def display(self):
		if self.true:
			print("%s is true" % self.get_letter())
		elif self.ambig and not self.false:
			print("%s is ambiguous" % self.get_letter())
		else:
			print("%s is false" % self.get_letter())
