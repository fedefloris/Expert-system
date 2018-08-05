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

import ft
from Line import Line

class Parser:
	def __init__(self, config, file_name):
		self.parse_file(config, file_name);
		self.check_errors()

	def parse_file(self, config, file_name):
		line_read = ft.read_lines(file_name, config.max_lines)
		if not line_read:
			print("\033[1;31mRead error\033[1;37m: %s" % file_name)
			exit(2)
		self.lines = [Line(config, line, line_num + 1)
			for line_num, line in enumerate(line_read)]
		config.lines = self.lines

	def check_errors(self):
		error = []
		for line in self.lines:
			print(line.data)
			if line.type == Line.ERROR_TYPE:
				error.append("\033[1;31mError:\033[1;37m"
					" Invalid syntax on line \033[1;34m%d\033[1;32m\n"
					"\t\"\033[1;37m%s\033[1;32m\"" % (line.num, line.string))
				error.append("\n")
		if len(error) > 1:
			raise ValueError("".join(error[:-1]))
