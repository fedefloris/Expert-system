#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 00:09:39 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 21:30:28 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('./src/')

from config import Config
from parse import Parser
from graph import graph

def main():
	# Ensures there is only one command line argument.
	if len(sys.argv) != 2:
		exit("\033[1;32m[Usage] \033[1;37m./expert_system.py file")

	config = Config()
	parser = Parser(config)
	for x in parser.lines:
		print ("Num[%d]\nType[%d]\n[%s]\n[%s]\n--------" % (x.num, x.type, x.string, x.data))
	print(config.op_and, config.op_or, config.op_xor, config.op_neg)
	graph(config)

if __name__== "__main__":
	main()
