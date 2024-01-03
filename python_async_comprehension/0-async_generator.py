#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Asynchronously generates random floating-point numbers between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.

    This coroutine will loop 10 times, each time asynchronously waits for
    1 second, and then yields a random number between 0 and 10 using the
    random module.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
