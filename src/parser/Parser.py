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
				line.tokens = self.__create_token(line.data.split(self.config.implies_sub)[0])
				print(line.tokens)
				print(line.tokens.trueif)
				# print(test.trueif[0].name)
				# print(test.trueif[1].name)

	def __create_token(self, expr):
		# Remove brackets both at the begin and at the end
		if (len(expr) > 1 and expr[0] == "("):
			expr = expr[1:-1]
		if (len(expr) <= 1):
			return Base(expr)
		# Ops ordered by increasing priority
		for op in self.config.ops:
			inside = False
			for c in expr:
				if c == "(":
					inside = True
				elif c == ")":
					inside = False
				elif inside == False and c == op:
					if op == "!":
						new = self.__create_token(expr.split(op,1)[1])
						new.make_negative()
						break
					else:
						new = And("")
						new.add_true(self.__create_token(expr.split(op,1)[0]))
						new.add_true(self.__create_token(expr.split(op,1)[1]))
						break
		return new
