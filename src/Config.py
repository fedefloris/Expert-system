# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/17 20:59:41 by dhojt             #+#    #+#              #
#    Updated: 2018/08/04 09:36:18 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import ft
import string

class Config:
	def __init__(self, file_name = None):
		self.set_default_values()
		if file_name:
			self.parse_config_file(file_name)
		# Sets value of strings passed as arguments in other functions.
		self.ops = self.op_neg + self.op_and + self.op_or + self.op_xor
		# Used in character matching in is_rule
		self.conditions = self.left_bracket + self.right_bracket
		self.conditions += self.ops + self.implies + self.bicondition
		# Used in pattern matching in is_rule
		self.pattern = self.op_and + self.op_or + self.op_xor
		self.pattern += self.implies_sub + self.bicondition_sub
		self.max_lines = int(self.max_lines)

	def set_default_values(self):
		self.facts = string.ascii_uppercase
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
		self.max_lines = "100"
		self.lines = None
		self.graph = {x:None for x in self.facts}

	def parse_config_file(self, file_name):
		lines = ft.read_lines(file_name, 100)
		# Checks if read of config file was successful
		if lines:
			# Array of attribute names for below Loop.
			array = ["left_bracket", "right_bracket", "op_neg",
					"op_and", "op_or", "op_xor", "implies",
					"bicondition", "initial_fact", "query",
					"implies_sub", "bicondition_sub", "max_lines"]
			# Loop through parsed config, to overwrite default config.
			for line in lines:
				# Remove comment and new line
				line = line.replace("\n", "").split("#")[0]
				# Check for 'set' keyword
				if line.count("set "):
					line = line.split("set")[1]
				else:
					line = ""
				# Remove white space
				line = line.replace(" ", "").replace("\t", "")
				# Loops through array of attribute names
				for x in array:
					# Checks if modification attribute is valid.
					tmp = self.match_attr(line, x)
					# Checks if line contains only "value", sets attribute
					if line != tmp and self.is_valid_value(array, x, tmp):
							setattr(self, x, tmp)

	def match_attr(self, string, substring):
		# Appends =" to substring to ensure correct formatting for set = " "
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

	def is_valid_value(self, array, attr, value):
		if value == "":
			return (False)
		for x in self.facts:
			if (x == value):
				return (False)
		if attr == "max_lines" and not self.is_valid_max_lines(value):
			return (False)
		# Ensures that the value is unique
		for x in array:
			if getattr(self, x) == value:
				return (False)
		return (True)

	def is_valid_max_lines(self, value):
		if not ft.str_is_numeric(value):
			return (False)
		if int(value) <= 0:
			return (False)
		return (True)
	
	# Displays original input, but prints facts in correct colour.
	def display(self):
		for line in self.lines:
			comment = 0
			for char in line.string:
				if char == "#":
					comment = 1
				if char in self.facts and not comment:
					print(self.graph[char].letter(), end="")
				else:
					print(char, end ="")
			print()
