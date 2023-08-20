#!/usr/bin/env python3
'''
Task 0's module
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    return a tuple of index range
    '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
