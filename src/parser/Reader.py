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
		self._read_lines(file_name, max_lines)

	def _read_lines(self, file_name, max_lines):
		self.lines = []
		if max_lines > 0:
			try:
				with open(file_name) as read:
					for line in read:
						self.lines.append(line)
						max_lines -= 1
						if not max_lines:
							break
			except Exception:
				self.lines = None
