#!/usr/bin/env python3

# this program for basic async syntax
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
