# [pprintast](https://pprintast.readthedocs.io/en/latest/)

[![PyPi release](https://img.shields.io/pypi/v/pprintast.svg)](https://pypi.org/project/pprintast/)
[![Downloads](https://pepy.tech/badge/pprintast)](https://pepy.tech/project/pprintast)
[![Documentation Status](https://readthedocs.org/projects/pprintast/badge/?version=latest)](https://pprintast.readthedocs.io/en/latest/?badge=latest)

An AST (abstract syntax tree) pretty printer for Python 🐍.

[Check out the pprintast docs](https://pprintast.readthedocs.io/en/latest/)

## Installation

```bash
$ pip install pprintast
```

## Usage

```text

usage: pprintast.py [-h] [-a] [-c cmd] [-m mode] [-t] [-v] [file]

A pretty-printing dump function for the ast module. The code was copied from the ast.dump function
and modified slightly to pretty-print.

positional arguments:
  file                   program passed in as file

optional arguments:
  -h, --help             show this help message and exit
  -a, --attributes       include attributes such as line numbers and column offsets
  -c cmd, --command cmd  program passed in as string
  -m mode, --mode mode   compilation mode (choices: exec, eval, single) (default: exec)
  -t, --terse            terse output by disabling field annotations
  -v, --version          show program's version number and exit

```

### Script

Pretty print AST from a **file** using the `pprintast` CLI.

```bash
$ pprintast "./path/to/script.py"
```

Pretty print AST from a **string** using the `pprintast` CLI.

```bash
$ pprintast -c "lambda a: a**2"
```

### Module

Pretty print AST from a **string** using the `pprintast` module.

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
