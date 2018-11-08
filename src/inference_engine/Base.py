# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Base.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Expr import Expr

# Base is the lowest level of expression. It's trueif list contains one
# element which is a character string (Fact Letter).
# It does not search recursively.
class Base(Expr):
	def __init__(self, name):
		Expr.__init__(self, name)

	def check(self, config):
		if config.graph[self.name].true:
			self.make_true(config)
		elif config.graph[self.name].ambig and not config.graph[self.name].false:
			self.make_ambig(config)
		else:
			self.make_false(config)
