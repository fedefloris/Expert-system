# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    strings.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/17 10:21:41 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 10:45:27 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import char

# str_is_upper tests if string is lower case
def str_is_upper(string):
	for c in string:
		if not char.is_upper(c):
			return (0)
	return (1)


# str_is_lower tests if string is lower case
def str_is_lower(string):
	for c in string:
		if not char.is_lower(c):
			return (0)
	return (1)


# str_is_numeric tests if string is lower case
def str_is_numeric(string):
	for c in string:
		if not char.is_digit(c):
			return (0)
	return (1)
