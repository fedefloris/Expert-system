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

from itertools import islice
import os

class Reader:
	def __init__(self, file_name, max_lines):
		self.lines = None
		self._read_lines(file_name, max_lines)

	def _read_lines(self, file_name, max_lines):
		try:
			if os.path.isfile(file_name):
				with open(file_name) as file:
					self.lines = list(islice(file, max_lines))
		except Exception:
			self.lines = None
