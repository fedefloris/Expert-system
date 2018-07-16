# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/16 23:24:51 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import ft

# LINE TYPES
# 0 Error
# 1 Blank Line
# 2 Rule
# 3 Fact
# 4 Query


def parse():

	# Returns integer of above value depending on type.
	def get_type(line):

		# Function returns if line is a rule.
		def is_rule(line):

			# Checks if characters are valid.
			for x in line:
				if not (ft.is_upper(x) or ft.char_matches(x, config.conditions)):
					return (0)

			# Substitutes implies for substitutes
			line = line.replace(config.bicondition, config.bicondition_sub)
			line = line.replace(config.implies, config.implies_sub)

			# Checks pattern of characters is good. [A + B ++ C] is bad.
			count = 0
			for x in line:
				if ft.is_upper(x):
					count += 1
				elif ft.char_matches(x, config.pattern):
					count -= 1
				if count > 1 or count < 0:
					return (0)

			# Checks to ensure that there is a maximum of one implication.
			if line.count(config.implies_sub) + line.count(config.bicondition_sub) != 1:
				return (0)
			return (1)

		# Function returns if line is a fact.
		def is_fact(line):

			# Checks if characters are valid
			for x in line:
				if not (ft.is_upper(x) or x == config.initial_fact):
					return (0)

			# Ensures that first character is valid.
			if line[0] != config.initial_fact:
				return (0)

			# Ensures that first character is not repeated.
			if line.count(config.initial_fact) != 1:
				return (0)
			return (1)


		# Function returns if line is a query.
		def is_query(line):

			# Checks if characters are valid
			for x in line:
				if not (ft.is_upper(x) or x == config.query):
					return (0)

			# Ensures that first character is valid.
			if line[0] != config.query:
				return (0)

			# Ensures that first character is not repeated.
			if line.count(config.query) != 1:
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
		# If matched non of the abvoe, then line is error.
		return (0)


	def check_match(string, substring):

		# Appends =" to substring
		substring += "=\""

		# Ensures that the occurence of the matching atribute is left most
		if string.count(substring) and string.split(substring)[0] == "":
			string = string.split(substring)[1]
		else:
			return (string)

		# Ensures that the closing " is the last characteer on the line
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
				string = string.replace("\n", "").split("#")[0]

				# Check for 'set' keyword
				if string.count("set "):
					string = string.split("set")[1]
				else:
					string = ""

				# Remove white space
				string = string.replace(" ", "").replace("\t", "")

				# Loops through array of attribute names
				for x in array:
					# Checks if modification attribute is valid.
					tmp = check_match(string, x)

					# Checks if string contains only "value", sets attribute
					if string != tmp and tmp != "":
						setattr(self, x, tmp)

			# Sets value of strings passed as arguments in other functions.
			self.ops = self.op_neg + self.op_and + self.op_or + self.op_xor

			# Used in character matching in is_rule
			self.conditions = self.left_bracket + self.right_bracket
			self.conditions += self.ops + self.implies + self.bicondition

			# Used in pattern matching in is_rule
			self.pattern = self.op_and + self.op_or + self.op_xor
			self.pattern += self.implies_sub + self.bicondition_sub


	class Line:
		def __init__(self, string, line_num):
			self.string = string.replace("\n", "")
			self.data = string.replace("\n", "")
			self.data = self.data.replace("\t", "")
			self.data = self.data.replace(" ", "")
			self.data = self.data.split("#")[0]
			self.type = get_type(self.data)
			self.num = line_num

			# If rule, substitute implies.
			if self.type == 2:
				self.data = self.data.replace(config.bicondition, config.bicondition_sub)
				self.data = self.data.replace(config.implies, config.implies_sub)
				print(config.bicondition, config.bicondition_sub)
			
			# If initial fact, remove leading character
			if self.type == 3:
				self.data = self.data.replace(config.initial_fact, "")
	
			# If query, remove leading character
			if self.type == 4:
				self.data = self.data.replace(config.query, "")


	# CREATES CONFIG OBJECT
	config = Config(ft.read_lines("expert_system.sh"))	

	# CREATES LINES ARRAY
	# Ensures there is only one command line argument.
	if len(sys.argv) != 2:
		exit(2)

	# Initialise for the below 
	line_num = 1
	lines = []
	
	# Loops each next line read from the input file
	for line in ft.read_lines(sys.argv[1]):
		# Treats each line and appends to lines (array of Line objects)
		lines.append(Line(line, line_num))
		line_num += 1
	
	return {"lines":lines, "config":config}
