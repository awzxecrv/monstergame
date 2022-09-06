import main
import pytest


def test_main_creation():
    a = main.creation()
    assert a == 10
