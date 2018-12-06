"""pprintast test module"""
import argparse
import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from unittest.mock import patch

from pprintast import Mode, cli, pprintast as ppast


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class test_pprintast(unittest.TestCase):
    """pprintast function tests."""

    @patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(
            command="4 * 4", mode=Mode.EXEC, terse=False, attributes=False
        ),
    )
    def test_cli(self, mock_args):
        expected = """
Module(body=[
    Expr(value=BinOp(left=Num(n=4), op=Mult(), right=Num(n=4))),
  ])
""".lstrip()
        with captured_output() as (out, err):
            cli()
            mock_args.assert_called_once()
            self.assertEqual(out.getvalue(), expected)

    def test_should_pprintast(self):
        exp = "lambda a: a**2"
        expected = """
Module(body=[
    Expr(value=Lambda(args=arguments(args=[
        arg(arg='a', annotation=None),
      ], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=BinOp(left=Name(id='a', ctx=Load()), op=Pow(), right=Num(n=2)))),
  ])
""".lstrip()
        with captured_output() as (out, err):
            ppast(exp)
            self.assertEqual(out.getvalue(), expected)

    def test_should_pprintast_attributes(self):
        exp = "lambda a: a**2"
        expected = """
Module(body=[
    Expr(value=Lambda(args=arguments(args=[
        arg(arg='a', annotation=None, lineno=1, col_offset=7),
      ], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=BinOp(left=Name(id='a', ctx=Load(), lineno=1, col_offset=10), op=Pow(), right=Num(n=2, lineno=1, col_offset=13), lineno=1, col_offset=10), lineno=1, col_offset=0), lineno=1, col_offset=0),
  ])
""".lstrip()
        with captured_output() as (out, err):
            ppast(exp, attributes=True)
            self.assertEqual(out.getvalue(), expected)

    def test_should_pprintast_terse(self):
        exp = "lambda a: a**2"
        expected = """
Module([
    Expr(Lambda(arguments([
        arg('a', None),
      ], None, [], [], None, []), BinOp(Name('a', Load()), Pow(), Num(2)))),
  ])
""".lstrip()
        with captured_output() as (out, err):
            ppast(exp, terse=True)
            self.assertEqual(out.getvalue(), expected)

    def test_should_pprintast_exec_mode(self):
        exp = "lambda a: a**2"
        expected = """
Module(body=[
    Expr(value=Lambda(args=arguments(args=[
        arg(arg='a', annotation=None),
      ], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=BinOp(left=Name(id='a', ctx=Load()), op=Pow(), right=Num(n=2)))),
  ])
""".lstrip()
        with captured_output() as (out, err):
            ppast(exp, mode=Mode.EXEC)
            self.assertEqual(out.getvalue(), expected)

    def test_should_pprintast_eval_mode(self):
        exp = "lambda a: a**2"
        expected = """
Expression(body=Lambda(args=arguments(args=[
    arg(arg='a', annotation=None),
  ], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=BinOp(left=Name(id='a', ctx=Load()), op=Pow(), right=Num(n=2))))
""".lstrip()
        with captured_output() as (out, err):
            ppast(exp, mode=Mode.EVAL)
            self.assertEqual(out.getvalue(), expected)

    def test_should_pprintast_single_mode(self):
        exp = "lambda a: a**2"
        expected = """
Interactive(body=[
    Expr(value=Lambda(args=arguments(args=[
        arg(arg='a', annotation=None),
      ], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=BinOp(left=Name(id='a', ctx=Load()), op=Pow(), right=Num(n=2)))),
  ])
""".lstrip()
        with captured_output() as (out, err):
            ppast(exp, mode=Mode.SINGLE)
            self.assertEqual(out.getvalue(), expected)

    @patch("pprintast.pprintast")
    def test_should_pprintast_with_specified_mode(self, mock_ppast):
        exp = "4 // 3"
        mock_ppast(exp, mode=Mode.EVAL)

        mock_ppast.assert_called_once()
        mock_ppast.assert_called_with(exp, mode=Mode.EVAL)
        self.assertEqual(mock_ppast.call_count, 1)

    @patch("pprintast.pprintast")
    def test_should_pprintast_once_when_called(self, mock_ppast):
        exp = "4 + 4"
        mock_ppast(exp)

        mock_ppast.assert_called_once()
        mock_ppast.assert_called_with(exp)
        self.assertEqual(mock_ppast.call_count, 1)


if __name__ == "__main__":
    unittest.main()
