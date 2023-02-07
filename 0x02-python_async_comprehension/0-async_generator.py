#!/usr/bin/env python3
'''
 Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
Use the random module.
'''
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    ''' Returns asynchronously 10 random numbers
    '''
    for i in range(0, 10):
        yield (random.random() * 10)
        await asyncio.sleep(1)
