# [pprintast](https://pypi.org/project/pprintast/)

[![PyPi release](https://img.shields.io/pypi/v/pprintast.svg)](https://pypi.org/project/pprintast/)

An AST (abstract syntax tree) pretty printer for Python 🐍.

## Installation

```bash
$ pip install pprintast
```

## Usage

```bash

usage: pprintast.py [-h] [-v] [-c cmd] [file]

A pretty-printing dump function for the ast module. The code was copied from
the ast.dump function and modified slightly to pretty-print.

positional arguments:
  file                   program(s) passed in as file

optional arguments:
  -h, --help             show this help message and exit
  -v, --version          show program's version number and exit
  -c cmd, --command cmd  program passed in as string

```

### Script

Pretty print AST from a *file* using the `pprintast` CLI.

```bash
$ pprintast "./path/to/script.py"
```

Pretty print AST from a *string* using the `pprintast` CLI.

```bash
$ pprintast -c "lambda a: a**2"
```

### Module

Pretty print AST from a *string* using the `pprintast` module.

```python

# 1. import the "pprintast" function.
from pprintast import pprintast as ppast # OR: from pprintast import ppast

# 2. pretty print AST from a "string".
exp = "lambda a: a**2"

ppast(exp)

```

![stdout](https://raw.githubusercontent.com/clarketm/pprintast/master/pprintast.png)

## License

MIT &copy; [**Travis Clarke**](https://blog.travismclarke.com/)
