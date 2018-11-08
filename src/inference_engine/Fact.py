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

	def make_true(self, config):
		self.true = 1
		self.contradiction(config)

	def make_false(self, config):
		self.false = 1
		self.contradiction(config)

	def make_ambig(self):
		self.ambig = 1

	def contradiction(self, config):
		if self.true and self.false:
			config.debug(f"{self.name} is a contradiction")
			exit(1)

	def check(self, config):
		for condition in self.trueif:
			condition.check(config)
			if condition.valid:
				config.debug(f"{condition.name} makes {self.name} true")
				self.make_true(config)
			if condition.ambig:
				config.debug(f"{condition.name} makes {self.name} ambig")
				self.make_ambig(config)
		for condition in self.falseif:
			condition.check(config)
			if condition.valid:
				config.debug(f"{condition.name} makes {self.name} false")
				self.make_false(config)

	# Returns fact's letter appropriately coloured.
	def get_letter(self):
		if self.true:
			return (f"\x1b[32m{self.name}\x1b[0m")
		elif self.ambig and not self.false:
			return (f"\x1b[33m{self.name}\x1b[0m")
		return (f"\x1b[31m{self.name}\x1b[0m")

	# Displays string to declare state of fact.
	def display(self, config):
		if self.true:
			config.debug(f"{self.get_letter()} is true")
		elif self.ambig and not self.false:
			config.debug(f"{self.get_letter()} is ambiguous")
		else:
			config.debug(f"{self.get_letter()} is false")
