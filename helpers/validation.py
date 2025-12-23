"""
Helper functions for ICEGATE BE Message validation and normalization.
"""

import re


def _normalize(value):
    """Ensures value is always a string (empty if None)."""
    return value if value not in (None, "None") else ""


def _validate_date(value):
    """Validate YYYYMMDD format."""
    return bool(re.fullmatch(r"\d{8}", value))


def _validate_numeric(value):
    """Validate that value is numeric (handles both str and int)."""
    if isinstance(value, int):
        return True
    if isinstance(value, str):
        return value.isdigit()
    return False


def _validate_decimal(value, pattern):
    """Validate decimal format against regex pattern."""
    return bool(re.fullmatch(pattern, value))
