#!/usr/bin/env python3.6

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

# To do list:
# 	- and in conclusions
# 	- nand, nor, exnor
#	- check ambigous and contradiction
#	- reasoning visualization
#	- fix inference engine, it must loop until there are no more changes

import sys
import argparse
sys.path.extend(["./src/", "./src/parser/", "./src/graph/"])

from Config import Config
from Parser import Parser
from Lexer import Lexer
from Graph import Graph
from ParsingError import ParsingError

def parse_arguments():
	parser = argparse.ArgumentParser(description='A propositional calculus expert system.')
	parser.add_argument("-c", "--config", metavar="file", help="file with settings")
	parser.add_argument("file", help="file with rules and facts")
	if len(sys.argv) == 1:
	    parser.print_help()
	    parser.exit()
	return parser.parse_args()

def main():
	args = parse_arguments()
	try:
		config = Config(args.config)
		lexer = Lexer(config, args.file)
		parser = Parser(config)
	except ParsingError as ex:
		exit(ex)
	graph = Graph(config)
	graph.solve()

if __name__== "__main__":
	main()
