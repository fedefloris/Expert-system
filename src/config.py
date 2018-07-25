# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/17 20:59:41 by dhojt             #+#    #+#              #
#    Updated: 2018/07/24 16:34:57 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('./src/py_ft/')

import ft
import string
from parse import parse

class Config:
	def __init__(self, file_name = "config"):

		lines = ft.read_lines(file_name, 100)

		self.set_default_values()

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
				self.line = line
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
					tmp = self.check_match(line, x)

					# Checks if line contains only "value", sets attribute
					if line != tmp and tmp != "":
						setattr(self, x, tmp)

		# Sets value of strings passed as arguments in other functions.
		self.ops = self.op_neg + self.op_and + self.op_or + self.op_xor

		# Used in character matching in is_rule
		self.conditions = self.left_bracket + self.right_bracket
		self.conditions += self.ops + self.implies + self.bicondition

		# Used in pattern matching in is_rule
		self.pattern = self.op_and + self.op_or + self.op_xor
		self.pattern += self.implies_sub + self.bicondition_sub

		# Set string to int if string is numeric
		if not ft.str_is_numeric(self.max_lines):
			print("max_lines = [%s] must be numeric" % self.max_lines)
			exit(2)
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

	def check_match(self, string, substring):

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

	def parse(self):
		self.lines = parse(self)
