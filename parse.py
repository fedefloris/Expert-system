# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/12 22:20:51 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def parse():
	if len(sys.argv) != 2:
		exit(2)
	f = open(sys.argv[1], "r")
	if f.mode != "r":
		exit(2)
	lines = f.readlines()
	for x in lines:
		print(x)
	f.close
