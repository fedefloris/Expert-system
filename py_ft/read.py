# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    read.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/16 19:37:03 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 09:37:13 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# read_lines reads file and returns all lines in an array
def read_lines(file_name):

	lines = []
	try:
		with open(file_name) as read:
			for line in read:
				lines.append(line)
	except IOError:
		return (0)

	return (lines)
