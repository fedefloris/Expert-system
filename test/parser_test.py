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
    tests = [
        "", ".", "..", "./", " ",
        "/dev/random", "/dev/null", "/dev/zero"
    ]
    run_tests(tests)

def test_bad_files():
    run_tests(get_files("./test/examples/bad_files"))

def get_files(path):
    files = []
    for file in os.listdir(path):
        file_path = path + "/" + file
        if os.path.isdir(file_path):
            files.extend(get_files(file_path))
        elif os.path.isfile(file_path):
            files.append(file_path)
    return (files)

def run_tests(tests):
    config = Config()
    for test in tests:
        with pytest.raises(ParsingError):
            print("Testing file:", test)
            parser = Lexer(config, test)
