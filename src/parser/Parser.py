# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from And import And
from Or import Or
from Xor import Xor
from Base import Base
from Expr import Expr
from Fact import Fact
from Bracket import Bracket
from LineLexer import LineLexer

class Parser:
	def __init__(self, config):
		self.config = config
		self.__create_tokens()

	def __create_tokens(self):
		for line in self.config.lines:
			if (line.type == LineLexer.RULE_TYPE):
				test = self.__create_token(line.data.split(">")[0])
				print(test)
				print(test.trueif)
				line.tokens = test
				# print(test.trueif[0].name)
				# print(test.trueif[1].name)

	def __create_token(self, expr):
		if (len(expr) > 1 and expr[0] == "("):
			expr = expr[1:-1]
		if (len(expr) <= 1):
			return Base(expr)
		for op in "^|+!":
			inside = False
			for c in expr:
				if c == "(":
					inside = True
				elif c == ")":
					inside = False
				elif inside == False and c == op:
					# if op == "!":
					# 	new = self.__create_token(expr.split(op)[1])
					# 	new.make_negative()
					# 	break
					# else:
					# print(expr.split(op))
					# print(expr.split(op)[0],"And",expr.split(op)[1])
					new = And("")
					new.add_true(self.__create_token(expr.split(op,1)[0]))
					new.add_true(self.__create_token(expr.split(op,1)[1]))
					break
		return new
