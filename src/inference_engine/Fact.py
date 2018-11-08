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
			print(f"{self.name} is a contradiction")
			exit(1)

	def check(self, config):
		for condition in self.trueif:
			condition.check(config)
			if condition.valid:
				print(f"{condition.name} makes {self.name} true")
				self.make_true()
			if condition.ambig:
				print(f"{condition.name} makes {self.name} ambig")
				self.make_ambig()
		for condition in self.falseif:
			condition.check(config)
			if condition.valid:
				print(f"{condition.name} makes {self.name} false")
				self.make_false()

	# Returns fact's letter appropriately coloured.
	def get_letter(self):
		if self.true:
			return (f"\x1b[32m{self.name}\x1b[0m")
		elif self.ambig and not self.false:
			return (f"\x1b[33m{self.name}\x1b[0m")
		return (f"\x1b[31m{self.name}\x1b[0m")

	# Displays string to declare state of fact.
	def display(self):
		if self.true:
			print(f"{self.get_letter()} is true")
		elif self.ambig and not self.false:
			print(f"{self.get_letter()} is ambiguous")
		else:
			print(f"{self.get_letter()} is false")
