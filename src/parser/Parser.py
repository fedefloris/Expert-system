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
		for index, line in enumerate(self.config.lines):
			if line.type == LineLexer.RULE_TYPE:
				if self.config.bicondition_sub in line.data:
					line.string = line.string.replace(self.config.bicondition, self.config.implies, 1)
					line.data = line.data.replace(self.config.bicondition_sub, self.config.implies_sub, 1)
					split2 = line.string.split("#", 1)
					split3 = split2[0].split(self.config.implies, 1)
					new_data = split3[1].strip() + " " + self.config.implies + " " + split3[0].strip()
					if len(split2) == 2:
						new_data += " #" + split2[1]
					new = LineLexer(self.config, new_data, len(self.config.lines) + 1)
					self.config.lines.insert(index + 1, new)
				line.token = tokenParser.parse(line)
