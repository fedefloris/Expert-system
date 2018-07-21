# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/15 22:27:18 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 10:44:48 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import char
import strings
import read

###                              ## char ##

# is_upper tests if single character is upper case
def is_upper(c):
	return (char.is_upper(c))


# is_lower tests if single character is lower case
def is_lower(c):
	return (char.is_lower(c))


# is_digit tests if single character is a number
def is_digit(c):
	return (char.is_digit(c))


# char_matches tests if single character is in substring
def char_matches(c, substring):
	return (char.char_matches(c, substring))





###                              ## strings ##

# str_is_upper tests if string is lower case
def str_is_upper(string):
	return (strings.str_is_upper(string))


# str_is_lower tests if string is lower case
def str_is_lower(string):
	return (strings.str_is_lower(string))


# str_is_numeric tests if string is lower case
def str_is_numeric(string):
	return (strings.str_is_numeric(string))





###                              ## read ##

# read_file reads file and returns all lines in an array
def read_lines(file_name, max_lines):
	return (read.read_lines(file_name, max_lines))
