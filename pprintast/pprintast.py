"""
A pretty-printing dump function for the ast module.  The code was copied from
the ast.dump function and modified slightly to pretty-print.
"""

from ast import *
from enum import Enum

__VERSION__ = "1.0.0"


class StringEnum(str, Enum):
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Mode(StringEnum):
    EXEC = "exec"
    EVAL = "eval"
    SINGLE = "single"


def _dump(node, terse: bool, attributes: bool, indent: str):
    """
    Return a formatted dump of the tree in *node*.  This is mainly useful for
    debugging purposes.  The returned string will show the names and the values
    for fields.  This makes the code impossible to evaluate, so if evaluation is
    wanted *terse* must be set to True.  Attributes such as line
    numbers and column offsets are not dumped by default.  If this is wanted,
    *attributes* can be set to True.
    """

    def _format(node, level=0):
        if isinstance(node, AST):
            fields = [(a, _format(b, level)) for a, b in iter_fields(node)]
            if attributes and node._attributes:
                fields.extend(
                    [(a, _format(getattr(node, a), level)) for a in node._attributes]
                )
            return "".join(
                [
                    node.__class__.__name__,
                    "(",
                    ", ".join(
                        ("%s=%s" % field for field in fields)
                        if not terse
                        else (b for a, b in fields)
                    ),
                    ")",
                ]
            )
        elif isinstance(node, list):
            lines = ["["]
            lines.extend(
                (indent * (level + 2) + _format(x, level + 2) + "," for x in node)
            )
            if len(lines) > 1:
                lines.append(indent * (level + 1) + "]")
            else:
                lines[-1] += "]"
            return "\n".join(lines)
        return repr(node)

    if not isinstance(node, AST):
        raise TypeError("expected AST, got %r" % node.__class__.__name__)
    return _format(node)


def pprintast(
    source: str,
    filename: str = "<ast>",
    mode: str = Mode.EXEC,
    terse: bool = False,
    attributes: bool = False,
    indent: str = "  ",
):
    """Parse some code from a string and pretty-print it."""
    node: AST = parse(source, filename=filename, mode=mode)
    print(_dump(node, terse, attributes, indent))


# Alias (i.e. shortname)
ppast = pprintast


def cli():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=35, width=100
        ),
    )
    parser.add_argument(
        "-a",
        "--attributes",
        help="include attributes such as line numbers and column offsets",
        action="store_true",
    )
    parser.add_argument(
        "-c", "--command", type=str, metavar="cmd", help="program passed in as string"
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=Mode,
        metavar="mode",
        default=Mode.EXEC,
        choices=list(Mode),
        help="compilation mode (choices: %(choices)s) (default: %(default)s)",
    )
    parser.add_argument(
        "-t",
        "--terse",
        help="terse output by disabling field annotations",
        action="store_true",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__VERSION__}"
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r"),
        help="program(s) passed in as file",
        default=sys.stdin,
    )
    args = parser.parse_args()

    if args.command:
        pprintast(
            args.command, mode=args.mode, terse=args.terse, attributes=args.attributes
        )
    else:
        pprintast(
            args.file.read(),
            filename=args.file.name,
            mode=args.mode,
            terse=args.terse,
            attributes=args.attributes,
        )


if __name__ == "__main__":
    cli()
