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

from Config import Config
from Line import Line
import ft

class Parser:
	def __init__(self, file_name, config = Config()):
		self.parse_file(file_name, config);
		self.check_errors()

	def parse_file(self, file_name, config):
		line_read = ft.read_lines(file_name, config.max_lines)
		if not line_read:
			raise ValueError("\033[1;31mRead error\033[1;37m: %s" % file_name)
		self.lines = [Line(config, line, line_num + 1)
			for line_num, line in enumerate(line_read)]
		config.lines = self.lines

	def check_errors(self):
		error = []
		for line in self.lines:
			if line.type == Line.ERROR_TYPE:
				error.append("\033[1;31mError:\033[1;37m "
					"Invalid syntax on line \033[1;34m%d\033[1;32m\n\t"
					"\"\033[1;37m%s\033[1;32m\"\033[1;37m" % (line.num, line.string))
				error.append("\n")
		if len(error) > 1:
			raise ValueError("".join(error[:-1]))
