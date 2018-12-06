"""pprintast test module"""
import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from unittest.mock import patch

from pprintast import pprintast as ppast


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
            self.assertEqual(out.getvalue(), expected.lstrip())

    def test_should_pprintast_include_attributes(self):
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
            self.assertEqual(out.getvalue(), expected.lstrip())

    @patch("pprintast.pprintast")
    def test_should_pprintast_once_when_called(self, mock_ppast):
        obj = {"a": 1}
        mock_ppast(obj)

        mock_ppast.assert_called_once()
        mock_ppast.assert_called_with(obj)
        self.assertEqual(mock_ppast.call_count, 1)


if __name__ == "__main__":
    unittest.main()
