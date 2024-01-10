#!/usr/bin/env python3
"""
function that takes two integer arguments and return 
a tuple size two containing a star index and end index
"""


def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index

