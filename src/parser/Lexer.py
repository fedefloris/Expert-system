# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Lexer.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Config import Config
from Reader import Reader
from LineLexer import LineLexer
from ParsingError import ParsingError

class Lexer:
	def __init__(self, config, file_name):
		self.config = config
		self._parse_file(file_name);
		self._check_errors()

	def _parse_file(self, file_name):
		line_read = Reader(file_name, self.config.max_lines).lines
		if not line_read:
			raise ParsingError(f"\033[1;31mRead error\033[1;37m: {file_name}")
		self.lines = [LineLexer(self.config, line) for line in line_read]
		self.config.lines = self.lines

	def _check_errors(self):
		errors = []
		for line_num, line in enumerate(self.lines):
			if line.type == LineLexer.ERROR_TYPE:
				errors.append("\033[1;31mError:\033[1;37m "
					f"Invalid syntax on line \033[1;34m{line_num + 1}\033[1;32m\n\t"
					f"\"\033[1;37m{line.string}\033[1;32m\"\033[1;37m")
				errors.append("\n")
		if len(errors) > 0:
			raise ParsingError("".join(errors[:-1]))
