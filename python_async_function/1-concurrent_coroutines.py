#!/usr/bin/env python3
"""
Routine that runs 'wait_random(max_delay)'
n times, all in parallel, and returns a list
of the results of each 'wait_random' call
(which should be the amount of time the coroutine took
ot run)
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

seconds = float


async def run_and_append(max_delay: int, l: list) -> None:
    """
    Runs 'wait_random(max_delay)', awaits its return value,
    and appends its result to 'l'.
    """
    l.append(await wait_random(max_delay))


async def wait_n(n: int, max_delay: int) -> List[seconds]:
    """
    Runs 'wait_random(max_delay)' in parallel 'n' times,
    and returns a list of the amount of time
    (in floats representing seconds) each 'wait_random'
    call took, IN THE ORDER THAT THEY FINISHED.

    Returns a list of floats that represent
    the time, IN SECONDS,
    each coroutine took. The result should
    be in ascending order, since 'asyncio.gather'
    appends first the coroutines that finish first.
    """
    result = []

    await asyncio.gather(
        *(
            run_and_append(max_delay, result)
            for _ in range(n)
        )
    )

    return result
