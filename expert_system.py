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

from parse import parse
from get_config import get_config

def main():
	config = get_config()
	lines = parse(config)
	for x in lines:
		print ("Num[%d]\nType[%d]\n[%s]\n[%s]\n--------" % (x.num, x.type, x.string, x.data))
	print(config.op_and, config.op_or, config.op_xor, config.op_neg)

if __name__== "__main__":
	main()
