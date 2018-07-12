# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/13 00:58:38 by dhojt            ###   ########.fr        #
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

# LINE TYPES
# 0 Error
# 1 Conditions
# 2 True
# 3 Queries
# 4 Blank Line

def parse():
	class Line:
		def __init__(self, types, string):
			self.types = types
			self.string = string

	lines = []
	for x in read_file():
		tmp = Line(3, x) #need to identify the correct type.
		lines.append(tmp)

	return (lines)
