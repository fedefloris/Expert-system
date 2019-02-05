# Expert_system - 42born2code
[![Build Status](https://travis-ci.com/fedefloris/Expert_system.svg?branch=master)](https://travis-ci.com/fedefloris/Expert_system) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) ![](https://img.shields.io/github/license/fedefloris/Expert_system.svg)

## Challenge
A propositional calculus expert system.

The goal of this project is implementing a backward-chaining inference engine, it must be able to read rules and facts from a given text file. The [examples](/test/examples/good_files) folder contains many samples of possibile text files.

The text file format is explained in [Rules and facts](#Rules-and-facts).

For more general details look at the [subject](subject.pdf)

## Using the project
Run with no arguments to see all the options
```console
$> ./expert_system.py
usage: expert_system.py [-h] [-c file] [-v] [-o] file

A propositional calculus expert system.

positional arguments:
  file                  file with rules and facts

optional arguments:
  -h, --help            show this help message and exit
  -c file, --config file
                        file with settings
  -v, --verbose         displays investigation steps of the inference engine
  -o, --output          displays original input but prints facts in correct
                        colour
```

## Rules and facts
Any fact can be represented by a single letter of the alphabet.

A example of a text file could be:
```console
A + B => C  # A and B are True, so C is True
D + E => F  # Only D is True, so F is False

=ABDH
?CF
```
As you can see anything preceded by *#* will be a comment.

## Running the tests
```console
$> python3 -m pytest -v
```
