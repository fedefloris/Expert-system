# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Or.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Expr import Expr

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
