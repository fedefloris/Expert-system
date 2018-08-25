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
sys.path.extend(["./src/", "./src/py_ft/"])

from Config import Config
from Parser import Parser
from Graph import Graph

def main():
	# Ensures there is only one command line argument.
	if len(sys.argv) != 2:
		exit("\033[1;32m[Usage] \033[1;37m./expert_system.py file")
	try:
		config = Config()
		parser = Parser(sys.argv[1], config)
		graph = Graph(config)
		graph.solve()
	except Exception as ex:
		exit(ex)

if __name__== "__main__":
	main()
