#!/usr/bin/env python3
'''
 mport wait_random from the previous python file
 that you've written and write an async routine
 called wait_n that takes in 2 int arguments (in this order):
 n and max_delay. You will spawn wait_random n times with
 the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without
using sort() because of concurrency.
'''
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' wait for a wait_random for a specified n times
    '''

    return_list: List[float] = []
    for i in range(0, n):
        wait_seconds: float = await wait_random(max_delay)
        return_list.append(wait_seconds)
    return sorted(return_list)
