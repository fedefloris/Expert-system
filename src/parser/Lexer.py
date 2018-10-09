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

from LineLexer import LineLexer
from Config import Config
from Reader import Reader

class Lexer:
	def __init__(self, file_name):
		self.config = Config()
		self.__parse_file(file_name);
		self.__check_errors()

	def __parse_file(self, file_name):
		line_read = Reader(file_name, self.config.max_lines).lines
		if not line_read:
			raise ValueError("\033[1;31mRead error\033[1;37m: %s" % file_name)
		self.lines = [LineLexer(self.config, line, line_num + 1)
			for line_num, line in enumerate(line_read)]
		self.config.lines = self.lines

	def __check_errors(self):
		error = []
		for line in self.lines:
			if line.type == LineLexer.ERROR_TYPE:
				error.append("\033[1;31mError:\033[1;37m "
					"Invalid syntax on line \033[1;34m%d\033[1;32m\n\t"
					"\"\033[1;37m%s\033[1;32m\"\033[1;37m" % (line.num, line.string))
				error.append("\n")
		if len(error) > 0:
			raise ValueError("".join(error[:-1]))
