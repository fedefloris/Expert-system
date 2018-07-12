# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 00:09:39 by dhojt             #+#    #+#              #
#    Updated: 2018/07/13 00:58:18 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from parse import parse

def main():
	lines = parse()
	for x in lines:
		print ("Type: %d  |  String: %s" % (x.types, x.string))

if __name__== "__main__":
	main()
