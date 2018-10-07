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
		self.__create_operations()
		self.__create_tokens()

	def __create_operations(self):
		# Ordered by increasing priority
		self.operations = [
			(self.config.op_xor, Xor),
			(self.config.op_or, Or),
			(self.config.op_and, And),
			(self.config.op_not, Not)
		]

	def __create_tokens(self):
		for line in self.config.lines:
			if line.type == LineLexer.RULE_TYPE:
				self.__create_token(line)


	def __create_token(self, line):
		expr = line.data.split(self.config.implies_sub)[0]
		line.token = self.__get_token_from_expr(expr)

	def __get_token_from_expr(self, expr):
		# Remove brackets both at the begin and at the end
		if len(expr) > 1 and expr[0] == self.config.left_bracket:
			expr = expr[1:-1]
		if len(expr) <= 1:
			return Base(expr)
		for op, op_token in self.operations:
			insideBrackets = False
			for c in expr:
				if c == self.config.left_bracket:
					insideBrackets = True
				elif c == self.config.right_bracket:
					insideBrackets = False
				elif insideBrackets == False and c == op:
					split = expr.split(op, 1)
					new = op_token("")
					if (op_token != Not):
						new.add_true(self.__get_token_from_expr(split[0]))
						new.add_true(self.__get_token_from_expr(split[1]))
					else:
						new.add_true(self.__get_token_from_expr(split[1]))
					return new
