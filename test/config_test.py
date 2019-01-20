# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config_test.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 00:09:39 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 21:30:28 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.extend(["./src/", "./src/parser/"])

from Config import Config

def test_bad_syntax():
	config = Config("./test/examples/config/bad_syntax")
	assert config.left_bracket == Config().left_bracket

def test_bad_values():
	config = Config("./test/examples/config/bad_values")
	assert config.right_bracket == Config().right_bracket
	assert config.max_lines == Config().max_lines

def test_good_value():
	config = Config("./test/examples/config/change_op_and")
	assert config.op_and == "&"
	assert config.op_and != Config().op_and
