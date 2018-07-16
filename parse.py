# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/16 12:40:31 by dhojt            ###   ########.fr        #
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


		# Returns one if line is blank.
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
		substring += "=\""
		if string.count(substring) and string.split(substring)[0] == "":
			string = string.split(substring)[1]
		else:
			return (string)
		if string.count("\"") == 1 and string.split("\"")[1] == "":
			string = string.split("\"")[0]
		else:
			string = ""
		return (string)
	
	
	class Config:
		def __init__(self, lines):
			# Set default values for config.
			self.facts = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			self.left_bracket = "("
			self.right_bracket = ")"
			self.op_neg = "!"
			self.op_and = "+"
			self.op_or = "|"
			self.op_xor = "^"
			self.implies = "=>"
			self.bicondition = "<=>"
			self.initial_fact = "="
			self.query = "?"
			self.implies_sub = ">"
			self.bicondition_sub = "<"

			# Array of attribute names for below Loop.
			array = ["facts", "left_bracket", "right_bracket", "op_neg"]
			array.extend(["op_and", "op_or", "op_xor", "implies"])
			array.extend(["bicondition", "initial_fact", "query"])
			array.extend(["implies_sub", "bicondition_sub"])

			# Loop through parsed config, to overwrite default config.
			for string in lines:
				# Remove comment and new line
				self.string = string
				string = string.replace("\n", "")
				string = string.split("#")[0]

				# Check for 'set' keyword
				if string.count("set "):
					string = string.split("set")[1]
				else:
					string = ""

				# Remove white space
				string = string.replace("\t", "")
				string = string.replace(" ", "")

				# Loops through array of attribute names
				for x in array:
					# Checks if modification attribute is valid.
					tmp = check_match(string, x)

					# Checks if string contains only "value", sets attribute
					if string != tmp and tmp != "":
						setattr(self, x, tmp)


	class Line:
		def __init__(self, string, line_num):
			self.string = string.replace("\n", "")
			self.data = string.replace("\n", "")
			self.data = self.data.replace("\t", "")
			self.data = self.data.replace(" ", "")
			self.data = self.data.split("#")[0]
			self.type = get_type(self.data)
			self.num = line_num
	

	# CREATES CONFIG OBJECT
	config = Config(ft.read_file("expert_system.sh"))	

	# CREATES LINES ARRAY
	# Ensures there is only one command line argument.
	if len(sys.argv) != 2:
		exit(2)

	# Initialise for the below 
	line_num = 1
	lines = []
	
	# Loops each next line read from the input file
	for line in ft.read_file(sys.argv[1]):
		# Treats each line and appends to lines (array of Line objects)
		lines.append(Line(line, line_num))
		line_num += 1
	
	return {"lines":lines, "config":config}
