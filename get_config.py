# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get_config.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/17 20:59:41 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:13:26 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import ft
import string

class Config:
	def __init__(self, lines):

		# Set default values for config.
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

		# Checks if read of config file was successful
		if lines:

			# Array of attribute names for below Loop.
			array = ["left_bracket", "right_bracket", "op_neg"]
			array.extend(["op_and", "op_or", "op_xor", "implies"])
			array.extend(["bicondition", "initial_fact", "query"])
			array.extend(["implies_sub", "bicondition_sub", "max_lines"])

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
					tmp = check_match(line, x)

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


def get_config():
	# Creates and returns config object.
	return (Config(ft.read_lines("config", 100)))	