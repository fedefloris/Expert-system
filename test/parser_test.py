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
import pytest
import os
sys.path.extend(["./src/", "./src/parser/", "./src/graph/"])

from Config import Config
from Lexer import Lexer
from ParsingError import ParsingError

def test_invalid_files():
    #"/dev/zero"
    tests = ("", ".", "..", "./", " ", "/dev/random", "/dev/null")
    run_tests(tests)

def test_bad_syntax():
    path = "./test/examples/bad_files/"
    tests = [path + file
        for file in os.listdir(path) if os.path.isfile(path + file)]
    run_tests(tests)

def run_tests(tests):
    config = Config()
    for test in tests:
        with pytest.raises(ParsingError):
            print("Testing file:", test)
            parser = Lexer(config, test)
