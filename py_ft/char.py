# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    char.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/16 19:48:33 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 10:45:54 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# is_upper tests if single character is lower case
def is_upper(c):
	if c >= "A" and c <= "Z":
		return (1)
	return (0)


# is_lower tests if single character is lower case
def is_lower(c):
	if c >= "a" and c <= "z":
		return (1)
	return (0)


# is_digit tests if single character is a number
def is_digit(c):
	if c >= "0" and c <= "9":
		return (1)
	return (0)


# char_matches tests if single character is in substring 
def char_matches(c, substring):
	if c not in substring:
		return (0)
	return (1)
