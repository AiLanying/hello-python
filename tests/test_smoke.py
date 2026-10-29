"""最小冒烟测试：证明 pytest 能用、venv 生效、版本达标。"""

import sys


def test_python_version_at_least_312():
    assert sys.version_info[:2] >= (3, 12)


def test_runs_inside_virtualenv():
    assert sys.prefix != sys.base_prefix
