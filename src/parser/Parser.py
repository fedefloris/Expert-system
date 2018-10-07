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
from Not import Not
from Base import Base
from Expr import Expr
from Fact import Fact
from LineLexer import LineLexer

class Parser:
	def __init__(self, config):
		self.config = config
		self.__create_tokens()

	def __create_tokens(self):
		for line in self.config.lines:
			if line.type == LineLexer.RULE_TYPE:
				self.__create_token(line)
				print(line.token)
				print(line.token.trueif)


	def __create_token(self, line):
		# Ordered by increasing priority
		ops = [
			(self.config.op_xor, Xor),
			(self.config.op_or, Or),
			(self.config.op_and, And),
			(self.config.op_not, Not)
		]
		expr = line.data.split(self.config.implies_sub)[0]
		line.token = self.__create_token_from_expr(expr, ops)

	def __create_token_from_expr(self, expr, ops):
		# Remove brackets both at the begin and at the end
		if len(expr) > 1 and expr[0] == self.config.left_bracket:
			expr = expr[1:-1]
		if len(expr) <= 1:
			return Base(expr)
		for op, op_token in ops:
			print(op_token)
			inside = False
			for c in expr:
				if c == self.config.left_bracket:
					inside = True
				elif c == self.config.right_bracket:
					inside = False
				elif inside == False and c == op:
					split = expr.split(op, 1)
					print(split)
					new = op_token("")
					if (op_token != Not):
						new.add_true(self.__create_token_from_expr(split[0], ops))
						new.add_true(self.__create_token_from_expr(split[1], ops))
					return new
