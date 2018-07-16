# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 00:09:39 by dhojt             #+#    #+#              #
#    Updated: 2018/07/16 12:42:12 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from parse import parse

def main():
	lines = parse()["lines"]
	config = parse()["config"]
	for x in lines:
		print ("Num[%d]\nType[%d]\n[%s]\n[%s]\n--------" % (x.num, x.type, x.string, x.data))
	print(config.op_and, config.op_or, config.op_xor, config.op_neg)

if __name__== "__main__":
	main()
