# -*- coding: utf-8 -*-

import pytest
from promtempl.skeleton import fib

__author__ = "Marco Valente"
__copyright__ = "Marco Valente"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
