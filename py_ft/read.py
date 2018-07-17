# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    read.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/16 19:37:03 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 10:00:54 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# read_lines reads file and returns all lines in an array
def read_lines(file_name, max_lines):

	lines = []
	if max_lines > 0:
		try:
			with open(file_name) as read:
				for line in read:
					lines.append(line)
					max_lines -= 1
					if not max_lines:
						break
		except IOError:
			return (0)

	return (lines)
