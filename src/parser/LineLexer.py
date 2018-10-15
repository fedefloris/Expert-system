# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    LineLexer.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class LineLexer:
	ERROR_TYPE = 0
	BLANK_TYPE = 1
	RULE_TYPE = 2
	FACT_TYPE = 3
	QUERY_TYPE = 4

	def __init__(self, config, string, line_num):
		self.num = line_num
		self.string = string.replace("\n", "")
		string = self.string.replace("\t", "")
		string = string.replace(" ", "").split("#")[0]
		# Substitutes implies for substitutes
		string = string.replace(config.bicondition, config.bicondition_sub)
		string = string.replace(config.implies, config.implies_sub)
		self.type = self._get_type(string, config)
		self.data = self._get_data(string, config)

	def _get_type(self, line, config):
		# Must return in the following order: [BLANK, QUERY, FACT, RULE, ERROR]
		if self._is_blank(line):
			return (LineLexer.BLANK_TYPE)
		if self._is_query(line, config):
			return (LineLexer.QUERY_TYPE)
		if self._is_fact(line, config):
			return (LineLexer.FACT_TYPE)
		if self._is_rule(line, config):
			return (LineLexer.RULE_TYPE)
		return (LineLexer.ERROR_TYPE)

	def _is_rule(self, line, config):
		# Checks if characters are valid.
		for x in line:
			if not x in config.facts and not x in config.conditions:
				return (0)
		# Checks pattern of characters is good. [A++B], [((A+B)] are bad
		if not self._balanced_symbols(line, config):
			return (0)
		# Checks to ensure that there is a maximum of one implication.
		if line.count(config.implies_sub) + line.count(config.bicondition_sub) != 1:
			return (0)
		return (1)

	def _balanced_symbols(self, line, config):
		brackets_count = 0
		operands_count  = 0
		for char in line:
			if char == config.left_bracket:
				brackets_count += 1
			elif char == config.right_bracket:
				brackets_count -= 1
			if brackets_count < 0:
				return (0)
			if char in config.facts:
				operands_count += 1
			elif char in config.pattern:
				operands_count -= 1
			if operands_count > 1 or operands_count < 0:
				return (0)
		if operands_count != 1 or brackets_count:
			return (0)
		return (1)

	def _is_fact(self, line, config):
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

	def _is_query(self, line, config):
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

	def _is_blank(self, line):
		return (len(line) == 0)

	def _get_data(self, line, config):
		# If rule, substitute implies.
		if self.type == LineLexer.RULE_TYPE:
			pass
		# If initial fact, remove leading character
		elif self.type == LineLexer.FACT_TYPE:
			line = line.replace(config.initial_fact, "")
		# If query, remove leading character
		elif self.type == LineLexer.QUERY_TYPE:
			line = line.replace(config.query, "")
		return (line)
