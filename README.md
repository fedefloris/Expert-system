# Expert_system - 42born2code
[![Build Status](https://travis-ci.com/fedefloris/Expert_system.svg?branch=master)](https://travis-ci.com/fedefloris/Expert_system) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Challenge
A propositional calculus expert system.

The goal of this project is to implement a backward-chaining inference engine.

The program is able to read rules and facts from a given knowledge base contained in a text file. The [examples](/test/examples/good_files) folder contains many samples of possible text files.

The format of the file is explained in [Knowledge base](#Knowledge-base).

For more details look at the [subject](subject.pdf).

## Install dependencies
```console
pip install -r requirements.txt
```

## Using the project
Run with no arguments to see all the options:
```console
$> ./expert_system.py
usage: expert_system.py [-h] [-c file] [-v] [-o] file

A propositional calculus expert system.

positional arguments:
  file                  file with rules and facts

optional arguments:
  -h, --help            show this help message and exit
  -c file, --config file
                        file with symbols values
  -v, --verbose         displays investigation steps of the inference engine
  -o, --output          displays original input but prints facts in correct
                        colour
```
Run with no options to show only the result of the queries:
```console
$> ./expert_system.py examples/and.txt
C is true
F is false
```
Run with **-c** and specify a valid config file. The format of the config file is explained in [Config File](#Config-File).
```console
$> ./expert_system.py -c test/examples/config/change_op_and test/examples/config/and_op_changed
C is true
F is false
```
## Knowledge base

The knowledge base contains three types of statements:
  - [Rules](#Rules)
  - [Initializations](#Initializations)
  - [Queries](#Queries)

Anything preceded by **#** is treated as a comment.

An example of a text file could be:
```
# if A or B are true, C will be true
A | B => C

# if D and E are true, F will be true
D + E => F  

# List of facts that will be initially true, every other fact will be false by default
=ABDH

# Ask to the expert system the state (true/false) of the following facts:
?CF
```

#### Rules

A rule statement describes the status of facts based on logical conditions.

A fact can be represented by a single uppercase letter, its status can be either **true** or **false**.

The syntax is better described with an example:
`A + B => C` says that the status of `C` is **true** if both `A` and `B` are **true**.

To learn more about the rule's syntax check the files of the [examples](/test/examples/good_files) folder.

#### Initializations

An initialization statement sets to **true** a list of specified facts.

Every fact not contained inside this kind of statement is **false** by default.

The syntax is `=list_of_facts`. For example, `=ABC` will initialize `A`, `B` and `C` to **true**.

#### Queries

A query statement asks to the inference engine the status (**true** or **false**) of specified facts.

The syntax is `?list_of_facts`. For example, `?DE` will ask the status of `D` and `E`.

## Config file

The config file allows the changing of symbols values inside text files.

The syntax is `set symbol_identifier = "new_character"`.

Anything preceded by **#** is treated as a comment.

For example, here we're setting the **and** symbol to **&**:
```console
set op_and = "&"
```

## Running the tests
```console
pytest -v
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
