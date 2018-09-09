# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Condition.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Parent class of all expressions
class Condition:
	def __init__(self, name):
		self.name = name
		self.true = 0
		self.ambig = 0
		self.negative = 0
		self.trueif = []

	def add_true(self, condition):
		self.trueif.append(condition)

	def make_negative(self):
		self.negative = 1
