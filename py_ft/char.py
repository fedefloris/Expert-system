# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    char.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/16 19:48:33 by dhojt             #+#    #+#              #
#    Updated: 2018/07/16 19:48:42 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_upper(c):
	if c >= "A" and c <= "Z":
		return (1)
	return (0)


# is_lower tests if single character is lower case
def is_lower(c):
	if c >= "a" and c <= "z":
		return (1)
	return (0)


# char_matches tests if single character is in substring 
def char_matches(c, substring):
	if c not in substring:
		return (0)
	return (1)
