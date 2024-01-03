#!/usr/bin/env python3
"""
Module to provide an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. This module spawns wait_random n times with
the specified max_delay.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that waits for a random delay and returns it."""

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    return sorted(delays)
