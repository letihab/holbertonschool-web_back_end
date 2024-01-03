#!/usr/bin/env python3
"""
coroutine that collect 10 random numbers using
an async comprehensing over async_generator, 
then return the 10 random numbers.
"""
import typing
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random floating-point numbers using an
    asynchronous comprehension over async_generator.
    Returns:
        List[float]: A list containing 10 random floating-point numbers.
    """

    random_numbers = [number async for number in async_generator()]
    return random_numbers[:10]
