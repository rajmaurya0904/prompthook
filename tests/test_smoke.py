"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import prompthook


def test_version_is_set() -> None:
    assert prompthook.__version__
