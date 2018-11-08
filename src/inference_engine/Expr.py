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

	# self.check for And inherrits from this.
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
			self.make_true()
		elif ambig:
			self.make_ambig()
		else:
			self.make_false()

	def make_true(self):
		self.true = 1
		self.ambig = 0
		print(f"{self.name} is TRUE", end='')
		if not self.negative:
			print("")
			self.valid = 1
		else:
			print(" when it should be false")
			self.valid = 0

	def make_false(self):
		print(f"{self.name} is FALSE", end='')
		self.true = 0
		self.ambig = 0
		if self.negative:
			print("")
			self.valid = 1
		else:
			self.valid = 0
			print(" when it should be true")
			self.valid = 0

	def make_ambig(self):
		print(f"Evaluated {self.name} as AMBIGUOUS {type(self)}")
		self.true = 0
		self.ambig = 1
		self.valid = 0
		print(f"{self.name} is Invalid")
