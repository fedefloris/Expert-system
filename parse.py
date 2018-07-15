# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/16 02:46:31 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import ft

char_fact = "="
char_query = "?"

# LINE TYPES
# 0 Error
# 1 Blank Line
# 2 Rule
# 3 Fact
# 4 Query


def parse():
	def get_type(line):	
		def is_rule(line):
			for x in line:
				if not (ft.is_upper(x) or ft.char_matches(x, "+|!^<=>()")):
					return (0)
			count = 0
			for x in line:
				if ft.is_upper(x):
					count += 1
				elif ft.char_matches(x, "+|^="):
					count -= 1
				if count > 1 or count < 0:
					return (0)
			if line.count("=>") + line.count("<=>") != 1 or line.count("=") != 1:
				return (0)
			return (1)


		def is_fact(line):
			for x in line:
				if not (ft.is_upper(x) or x == char_fact):
					return (0)
			if line[0] != char_fact:
				return (0)
			if line.count(char_fact) != 1:
				return (0)
			return (1)


		def is_query(line):
			for x in line:
				if not (ft.is_upper(x) or x == char_query):
					return (0)
			if line[0] != char_query:
				return (0)
			if line.count(char_query) != 1:
				return (0)
			return (1)


		def is_blank_line(line):
			if len(line) == 0:
				return (1)
			return (0)

		if is_blank_line(line):
			return (1)
		if is_query(line):
			return (4)
		if is_fact(line):
			return (3)
		if is_rule(line):
			return (2)
		return (0)


	def check_match(string, substring):
		if string.count(substring):
			string = string.split(substring)[1]
		else:
			return (string)
		if string.count("=\""):
			string = string.split("=\"")[1]
			if string.count("\""):
				string = string.split("\"")[0]
			else:
				string = ""
		return (string)		
	class Line:
		def __init__(self, string, line_num):
			self.string = string.replace("\n", "")
			self.data = string.replace("\n", "")
			self.data = self.data.replace("\t", "")
			self.data = self.data.replace(" ", "")
			self.data = self.data.split("#")[0]
			self.type = get_type(self.data)
			self.num = line_num
	

# WORKING ON THIS SECTION - PARSING .sh FILE.
	class Config:
		def __init__(self, string):
			self.string = string
			string = string.replace("\n", "")
			string = string.split("#")[0]
			if string.count("set "):
				string = string.split("set")[1]
			else:
				string = ""
			string = string.replace("\t", "")
			string = string.replace(" ", "")
			string = check_match(string, "!") # require all
			print(string)


	line_num = 1
	lines = []
	config = []
	if len(sys.argv) != 2:
		exit(2)
	for line in ft.read_file(sys.argv[1]):
		tmp = Line(line, line_num)
		lines.append(tmp)
		line_num += 1
	for line in ft.read_file("expert_system.sh"):
		tmp = Config(line)
		config.append(tmp)
		
	return (lines)
