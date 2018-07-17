# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 21:25:36 by dhojt            ###   ########.fr        #
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


def parse(config):

	# Function returns integer depending on type.
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
			if count != 1:
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

		# Must return in the following order: [1, 4, 3, 2, 0]
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

			# If initial fact, remove leading character
			if self.type == 3:
				self.data = self.data.replace(config.initial_fact, "")

			# If query, remove leading character
			if self.type == 4:
				self.data = self.data.replace(config.query, "")


	# CREATES LINES ARRAY
	# Ensures there is only one command line argument.
	if len(sys.argv) != 2:
		exit(2)

	# Initialise for the below 
	line_num = 1
	lines = []

	# Reads and checks read was succesful.
	line_read = ft.read_lines(sys.argv[1], config.max_lines)
	if not line_read:
		print("Read error: %s" % sys.argv[1])
		exit(2)

	# Loops each next line read from the input file
	for line in line_read:
		# Treats each line and appends to lines (array of Line objects)
		lines.append(Line(line, line_num))
		line_num += 1

	return (lines)
