# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Xor.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Expr import Expr

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
