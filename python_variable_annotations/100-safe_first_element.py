#!/usr/bin/env python3
"""
The 'safe_first_element', protype was provide and it is need to
use the 'typing' module(?) to properly annotete it.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    If 'lst' is not empty,
    this function returns 'lst[0]'.
    Otherwise, this function returns None.

    'lst' is annotated as a 'Sequence',
    because this function assumes
    it supports indexes, and its
    bool representation must be True when
    full, and False when empty.

    To see ALL of the Sequence attributes, see:

https://docs.python.org/3.7/library/collections.abc.html#collections-abstract-base-classes
    """
    if lst:
        return lst[0]
    else:
        return None
