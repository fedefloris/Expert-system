# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/15 23:34:48 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import ft

def read_file():
	if len(sys.argv) != 2:
		exit(2)
	try:
		f = open(sys.argv[1], "r")
	except IOError:
		exit(2)
	if f.mode != "r":
		exit(2)
	lines = f.readlines()
	f.close
	return (lines)


# LINE TYPES
# 0 Error
# 1 Blank Line
# 2 Rule
# 3 Fact
# 4 Query


def parse():
	def get_type(line):
		def is_rule(line):
			success = 1
			for x in line:
				if not (ft.is_upper(x) or x == "+" or x == "=" or x == ">"):
					success = 0
			return (success)

		def is_blank_line(line):
			if len(line) == 0:
				return (1)
			return (0)

		if is_blank_line(line):
			return (1)
		if is_rule(line):
			return (2)
		return (0)

	class Line:
		def __init__(self, string, line_num):
			self.string = string.replace("\n", "")
			self.data = string.replace("\n", "")
			self.data = self.data.replace("\t", "")
			self.data = self.data.replace(" ", "")
			self.data = self.data.split("#")[0]
			self.type = get_type(self.data)
			self.num = line_num

	line_num = 1
	lines = []
	for line in read_file():
		tmp = Line(line, line_num)
		lines.append(tmp)
		line_num += 1
	return (lines)
