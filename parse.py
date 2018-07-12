# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/12 23:21:47 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def parse():
	if len(sys.argv) != 2:
		exit(2)
	try:
		f = open(sys.argv[1], "r")
	except IOError:
		exit(2)
	if f.mode != "r":
		exit(0)
	lines = f.readlines()
	for x in lines:
		print(x)
	f.close
