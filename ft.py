# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/15 22:27:18 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 10:03:02 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('./py_ft/')
import char
import read

# is_upper tests if single character is upper case
def is_upper(c):
	return (char.is_upper(c))


# is_lower tests if single character is lower case
def is_lower(c):
	return (char.is_lower(c))


# char_matches tests if single character is in substring 
def char_matches(c, substring):
	return (char.char_matches(c, substring))


# read_file reads file and returns all lines in an array
def read_lines(file_name, max_lines):
	return (read.read_lines(file_name, max_lines))
