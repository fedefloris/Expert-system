# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/07/25 12:44:39 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Fact:
	def __init__(self, fact):
		self.fact = fact
		self.init_false = 1
		self.true = 0
		self.false = 0
		self.ambig = 0

	def force_true(self):
		init_false = 0
		self.true = 1

	def contradict(self):
		if self.true and self.false:
			return 1
		else:
			return 0
	
	def show(self):
		if self.contradict():
			print("%s is a contradiction" % self.fact)
		elif self.true:	
			print("%s is true" % self.fact)
		elif self.false:
			print("%s is false" % self.fact)
		elif self.ambig:
			print("%s is ambiguous" % self.fact)
		elif self.init_false:
			print("%s is false" % self.fact)

a = Fact("A")
a.force_true()
a.show()
