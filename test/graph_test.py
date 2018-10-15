# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    graph_test.py                                      :+:      :+:    :+:    #
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
from Parser import Parser
from Graph import Graph

def test_files():
    path = "./test/examples/"
    tests = [path + file
        for file in os.listdir(path) if os.path.isfile(path + file)]
    run_tests(Config(), tests)

def run_tests(config, tests):
    for test in tests:
        print("Testing file:", test)
        run_test(config, test)
        run_assertions(config, config.lines[-1].string)

def run_test(config, test):
    lexer = Lexer(config, test)
    parser = Parser(config)
    graph = Graph(config)
    graph.solve()

def run_assertions(config, string):
    string = string.replace("#", "")
    string = string.replace("=", "")
    string = string.replace(" ", "")
    if string.isalpha():
        true_facts = set(string)
        for fact in config.facts:
            run_assertion(config, true_facts, fact)

def run_assertion(config, true_facts, fact):
    if fact in true_facts:
        assert config.graph[fact].true
    else:
        assert not fact in config.graph or not config.graph[fact].true
