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
sys.path.extend(["./src/", "./src/parser/", "./src/graph/"])

from Config import Config
from Parser import Parser
import pytest
import os

def test_invalid_files():
    tests = ("", ".", "..", "./", " ")
    run_tests(tests)

def test_bad_syntax():
    tests = ["./test/examples/bad_files/" + file
        for file in os.listdir("./test/examples/bad_files/")]
    run_tests(tests)

def run_tests(tests):
    for test in tests:
        with pytest.raises(ValueError):
            parser = Parser(test)
