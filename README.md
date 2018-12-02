# [pprintast](https://pypi.org/project/pprintast/)

[![PyPi release](https://img.shields.io/pypi/v/pprintast.svg)](https://pypi.org/project/pprintast/)

An AST (abstract syntax tree) pretty printer for Python 🐍.

## Installation

```bash
$ pip install pprintast
```

## Usage

### Script

```python

# 1. pretty print AST from "file".
pprintast "./path/to/script.py"

```

### Module

```python

# 1. import the "pprintast" function.
from pprintast import pprintast as ppast

# 2. retty print AST from "string".
exp = "lambda a: a**2"

ppast(exp)

```

![stdout](https://raw.githubusercontent.com/clarketm/pprintast/master/pprintast.png)

## License

MIT &copy; [**Travis Clarke**](https://blog.travismclarke.com/)
