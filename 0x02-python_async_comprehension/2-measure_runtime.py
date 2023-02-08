#!/usr/bin/env python3
'''
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
'''
import asyncio
import time
compr = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Returns asynchronously time taken to execute gather
    '''
    s = time.perf_counter()
    await asyncio.gather(*(compr for _ in range(4)))
    elapsed = time.perf_counter() - s
    return elapsed
