# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse_test.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 00:09:39 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 21:30:28 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append("./src/")
sys.path.append("./src/py_ft/")

from Parser import Parser

def test_bad_syntax():
    assert 1 == 1
