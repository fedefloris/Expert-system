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
		self._create_operations()
		self._create_tokens()

	def _create_operations(self):
		# Ordered by increasing priority
		self.operations = [
			(self.config.op_xor, Xor),
			(self.config.op_or, Or),
			(self.config.op_and, And),
			(self.config.op_not, Not)
		]

	def _create_tokens(self):
		lines_to_remove = []
		for line in self.config.lines:
			if line.type == LineLexer.RULE_TYPE:
				if self.config.bicondition_sub in line.data:
					new = LineLexer(self.config, "", len(self.config.lines) + 1)
					lines_to_remove.append(line)
					self.config.lines.append(new)
				else:
					self._create_token(line)
		for line in lines_to_remove:
			self.config.lines.remove(line)

	def _create_token(self, line):
		expr = self.config.left_bracket
		expr += line.data.split(self.config.implies_sub)[0]
		expr += self.config.right_bracket
		line.token = self._get_token_from_expr(expr)

	def _get_token_from_expr(self, expr):
		if self._brackets_at_the_edges(expr):
			expr = expr[1:-1]
		if len(expr) <= 1:
			return Base(expr)
		for op, op_token in self.operations:
			inside_brackets = False
			for i, c in enumerate(expr):
				if c == self.config.left_bracket:
					inside_brackets = True
				elif c == self.config.right_bracket:
					inside_brackets = False
				elif not inside_brackets and c == op:
					new = op_token(expr)
					if (op_token != Not):
						new.add_true(self._get_token_from_expr(expr[0:i]))
						new.add_true(self._get_token_from_expr(expr[i+1:]))
					else:
						new.add_true(self._get_token_from_expr(expr[i+1:]))
					return new
		return self._get_token_from_expr(expr)

	def _brackets_at_the_edges(self, expr):
		if len(expr) <= 1:
			return False
		if expr[0] != self.config.left_bracket or expr[-1] != self.config.right_bracket:
			return False
		return True
