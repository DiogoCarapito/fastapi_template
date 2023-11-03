# import pytest
from utils.utils import hello


def test_hello():
    assert hello() == "hello world!"
