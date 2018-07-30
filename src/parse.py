# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('./src/py_ft/')

import ft

class Parser:

	def __init__(self, config):

		self.parse_file(config, sys.argv[1]);

		# Exits if any line type is ERROR
		error = 0
		for line in self.lines:
			if not line.type:
				if error:
					print("")
				print("\033[1;31mError:\033[1;37m"
					" Invalid syntax on line \033[1;34m%d\033[1;32m\n"
					"\t\"\033[1;37m%s\033[1;32m\"" % (line.num, line.string))
				error += 1
		if error:
			exit(1)

	def parse_file(self, config, file_name):
		# Reads and checks read was succesful.
		line_read = ft.read_lines(file_name, config.max_lines)
		if not line_read:
			print("\033[1;31mRead error\033[1;37m: %s" % file_name)
			exit(2)

		# Loops each next line read from the input file
		self.lines = [self.Line(config, line, line_num + 1)
			for line_num, line in enumerate(line_read)]

		config.lines = self.lines

	# LINE TYPES
	# 0 Error
	# 1 Blank Line
	# 2 Rule
	# 3 Fact
	# 4 Query

	class Line:
		def __init__(self, config, string, line_num):
			self.string = string.replace("\n", "")
			self.data = self.string.replace("\t", "")
			self.data = self.data.replace(" ", "").split("#")[0]
			self.type = self.get_type(self.data, config)
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

		# Function returns integer depending on type.
		def get_type(self, line, config):
			# Must return in the following order: [1, 4, 3, 2, 0]
			if self.is_blank_line(line):
				return (1)
			if self.is_query(line, config):
				return (4)
			if self.is_fact(line, config):
				return (3)
			if self.is_rule(line, config):
				return (2)
			# If matched non of the abvoe, then line is error.
			return (0)

		# Function returns if line is a rule.
		def is_rule(self, line, config):

			# Checks if characters are valid.
			for x in line:
				if not x in config.facts and not ft.char_matches(x, config.conditions):
					return (0)

			# Substitutes implies for substitutes
			line = line.replace(config.bicondition, config.bicondition_sub)
			line = line.replace(config.implies, config.implies_sub)

			# Checks pattern of characters is good. [A + B ++ C] is bad.
			count = 0
			for x in line:
				if x in config.facts:
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
		def is_fact(self, line, config):

			# Checks if characters are valid
			for x in line:
				if not (x in config.facts or x == config.initial_fact):
					return (0)

			# Ensures that first character is valid.
			if line[0] != config.initial_fact:
				return (0)

			# Ensures that first character is not repeated.
			if line.count(config.initial_fact) != 1:
				return (0)
			return (1)


		# Function returns if line is a query.
		def is_query(self, line, config):

			# Checks if characters are valid
			for x in line:
				if not (x in config.facts or x == config.query):
					return (0)

			# Ensures that first character is valid.
			if line[0] != config.query:
				return (0)

			# Ensures that first character is not repeated.
			if line.count(config.query) != 1:
				return (0)
			return (1)

		# Returns one if line is blank.
		def is_blank_line(self, line):
			if len(line) == 0:
				return (1)
			return (0)
