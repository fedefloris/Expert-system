# Expert_system - 42born2code
[![Build Status](https://travis-ci.com/fedefloris/Expert_system.svg?branch=master)](https://travis-ci.com/fedefloris/Expert_system)

## Challenge
A propositional calculus expert system.  

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

## Running the tests
```console
$> python3 -m pytest -v
```
