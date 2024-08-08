#!/usr/bin/env python3

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def wait_n(n, max_delay) -> list[float]:
    """Asynchronous coroutine that takes in an integer argument"""
    delay = max_delay
    tasks = []
    for i in range(n):
        tasks.append(wait_random(delay))
    return [await task for task in asyncio.as_completed(tasks)]
