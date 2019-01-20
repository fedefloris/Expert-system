# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from LineLexer import LineLexer
from TokenParser import TokenParser

class Parser:
	def __init__(self, config):
		self.config = config
		self._create_tokens()

	def _create_tokens(self):
		tokenParser = TokenParser(self.config)
		for line_num, line in enumerate(self.config.lines):
			if line.type == LineLexer.RULE_TYPE:
				if self.config.bicondition_sub in line.data:
					self._replace_double_implies(line)
					self._add_reversed_implies(line_num, line)
				line.token = tokenParser.parse(line)

	def _replace_double_implies(self, line):
		line.string = line.string.replace(self.config.bicondition, self.config.implies, 1)
		line.data = line.data.replace(self.config.bicondition_sub, self.config.implies_sub, 1)

	def _add_reversed_implies(self, line_num, line):
		reversed_implies = LineLexer(self.config, self._get_reversed_implies(line))
		self.config.lines.insert(line_num + 1, reversed_implies)

	def _get_reversed_implies(self, line):
		line_split = line.string.split("#", 1)
		rule_split = line_split[0].split(self.config.implies, 1)
		reversed_data = rule_split[1].strip() + " "
		reversed_data += self.config.implies + " "
		reversed_data += rule_split[0].strip()
		if len(line_split) == 2:
			reversed_data += " #" + line_split[1]
		return (reversed_data)
