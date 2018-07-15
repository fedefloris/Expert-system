# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/15 19:03:32 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

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

def get_type(line):
	if line == "\n":
		return (4)
	return (1)

# LINE TYPES
# 0 Error
# 1 Rule
# 2 Fact
# 3 Query
# 4 Blank Line

def parse():
	class Line:
		def __init__(self, types, string):
			self.type = types
			self.string = string
			string = string.replace("\t", "")
			string = string.replace(" ", "")
			string = string.split("#")[0]
			self.data = string

	lines = []
	for line in read_file():
		tmp = Line(get_type(line), line.replace("\n", ""))
		lines.append(tmp)
	return (lines)
