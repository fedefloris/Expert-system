# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.sh                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/16 01:32:49 by dhojt             #+#    #+#              #
#    Updated: 2018/07/16 02:20:39 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Each string must be unique.
# Can only use speech-marks to open and close a string.
# Can not use spaces, tabs or new line characters in strings.

# objects
set facts = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# conditions
set left_bracket = "("
set right_bracket = ")"
set not = "!"
set and = "+"
set or = "|"
set xor = "^"
set implies = "=>"
set bicondition = "<=>"

# identifiers
set initial_fact = "="
set query = "?"

# substitutions
set implies_sub = ">"
set bicondition_sub = "<"
