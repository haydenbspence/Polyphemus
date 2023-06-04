import re

from packaging.version import parse as parse_version

import polyphemus
from polyphemus.version import version_info


def test_version_info():
    s = version_info()
    assert re.match(' *polyphemus version: ', s)
    assert s.count('\n') == 5


def test_standard_version():
    v = parse_version(polyphemus.VERSION)
    assert str(v) == polyphemus.VERSION


def test_version_attribute_is_present():
    assert hasattr(polyphemus, '__version__')


def test_version_attribute_is_a_string():
    assert isinstance(polyphemus.__version__, str)