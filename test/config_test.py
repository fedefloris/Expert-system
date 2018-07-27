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
sys.path.append("./src/")

from config import Config

def test_config():
    config = Config("./test/config_examples/bad_syntax")
    assert config.left_bracket == Config().left_bracket
