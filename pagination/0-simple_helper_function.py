#!/usr/bin/env python3
"""
function that takes two integer arguments and return 
a tuple size two containing a star index and end index
"""

import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """ return a tuple of size two containing a start
    index and an end index corresponding to
    the range of indexes to return in a
    list for those particular pagination parametes"""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
