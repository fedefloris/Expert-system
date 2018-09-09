# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Line.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Line:
	ERROR_TYPE = 0
	BLANK_TYPE = 1
	RULE_TYPE = 2
	FACT_TYPE = 3
	QUERY_TYPE = 4

	def __init__(self, config, string, line_num):
		self.string = string.replace("\n", "")
		self.data = self.string.replace("\t", "")
		self.data = self.data.replace(" ", "").split("#")[0]
		self.type = self.__get_type(self.data, config)
		self.num = line_num
		# If rule, substitute implies.
		if self.type == Line.RULE_TYPE:
			self.data = self.data.replace(config.bicondition, config.bicondition_sub)
			self.data = self.data.replace(config.implies, config.implies_sub)
		# If initial fact, remove leading character
		if self.type == Line.FACT_TYPE:
			self.data = self.data.replace(config.initial_fact, "")
		# If query, remove leading character
		if self.type == Line.QUERY_TYPE:
				self.data = self.data.replace(config.query, "")

	def __get_type(self, line, config):
		# Must return in the following order: [BLANK, QUERY, FACT, RULE, ERROR]
		if self.__is_blank(line):
			return (Line.BLANK_TYPE)
		if self.__is_query(line, config):
			return (Line.QUERY_TYPE)
		if self.__is_fact(line, config):
			return (Line.FACT_TYPE)
		if self.__is_rule(line, config):
			return (Line.RULE_TYPE)
		return (Line.ERROR_TYPE)

	def __is_rule(self, line, config):
		# Checks if characters are valid.
		for x in line:
			if not x in config.facts and not x in config.conditions:
				return (0)
		# Substitutes implies for substitutes
		line = line.replace(config.bicondition, config.bicondition_sub)
		line = line.replace(config.implies, config.implies_sub)
		# Checks pattern of characters is good. [A + B ++ C] is bad.
		count = 0
		for x in line:
			if x in config.facts:
				count += 1
			elif x in config.pattern:
				count -= 1
			if count > 1 or count < 0:
				return (0)
		if count != 1:
			return (0)
		# Checks to ensure that there is a maximum of one implication.
		if line.count(config.implies_sub) + line.count(config.bicondition_sub) != 1:
			return (0)
		return (1)

	def __is_fact(self, line, config):
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

	def __is_query(self, line, config):
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

	def __is_blank(self, line):
		return (len(line) == 0)
