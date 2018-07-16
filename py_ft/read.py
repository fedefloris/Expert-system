# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    read.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/16 19:37:03 by dhojt             #+#    #+#              #
#    Updated: 2018/07/16 19:54:34 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# read_file reads file and returns all lines in an array
def read_lines(file_name):
	try:
		f = open(file_name, "r")
	except IOError:
		print("File not found: %s" % file_name)
		exit(2)
	if f.mode != "r":
		exit(2)
	lines = f.readlines()
	f.close
	return (lines)
