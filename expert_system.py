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

def main():
	config = Config()
	config.parse()
	for x in config.lines:
		print ("Num[%d]\nType[%d]\n[%s]\n[%s]\n--------" % (x.num, x.type, x.string, x.data))
	print(config.op_and, config.op_or, config.op_xor, config.op_neg)

if __name__== "__main__":
	main()
