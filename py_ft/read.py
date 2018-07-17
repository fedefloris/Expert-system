# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    read.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/16 19:37:03 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 09:16:30 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# read_lines reads file and returns all lines in an array
def read_lines(file_name):
	try:
		f = open(file_name, "r")
	except IOError:
		return (0)
	if f.mode != "r":
		return (0)
	lines = f.readlines()
	f.close
	return (lines)
