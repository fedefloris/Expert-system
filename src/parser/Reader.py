# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Reader.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/18 10:23:56 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Reader:
	def __init__(self, file_name, max_lines):
		self.__read_lines(file_name, max_lines)

	def __read_lines(self, file_name, max_lines):
		self.__lines = []
		if max_lines > 0:
			try:
				with open(file_name) as read:
					for line in read:
						self.__lines.append(line)
						max_lines -= 1
						if not max_lines:
							break
			except IOError:
				self.__lines = None

	def get_lines(self):
		return (self.__lines)
