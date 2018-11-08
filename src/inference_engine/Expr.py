# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Expr.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/10/22 20:43:10 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Condition import Condition

class Expr(Condition):
	def __init__(self, name):
		Condition.__init__(self, name)
		self.valid = 0

	def make_true(self, config):
		self.true = 1
		self.ambig = 0
		config.debug(f"{self.name} is TRUE", end='')
		if not self.negative:
			config.debug("")
			self.valid = 1
		else:
			config.debug(" when it should be false")
			self.valid = 0

	def make_false(self, config):
		config.debug(f"{self.name} is FALSE", end='')
		self.true = 0
		self.ambig = 0
		if self.negative:
			config.debug("")
			self.valid = 1
		else:
			self.valid = 0
			config.debug(" when it should be true")
			self.valid = 0

	def make_ambig(self, config):
		config.debug(f"Evaluated {self.name} as AMBIGUOUS {type(self)}")
		self.true = 0
		self.ambig = 1
		self.valid = 0
		config.debug(f"{self.name} is Invalid")

	def check(self, config):
		true = 1
		ambig = 0
		for condition in self.trueif:
			condition.check(config)
			if not condition.valid and not condition.ambig:
				true = 0
				break
			if condition.ambig:
				true = 0
				ambig = 1
		if true:
			self.make_true(config)
		elif ambig:
			self.make_ambig(config)
		else:
			self.make_false(config)
