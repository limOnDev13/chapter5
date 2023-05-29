import functools
import asyncio
import aiohttp
from aiohttp import ClientSession
import time
from typing import Callable, Any, List


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'Выполняется {func} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')
        return wrapped
    return wrapper


async def delay(delay_seconds: int) -> int:
    print(f'Засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течение {delay_seconds} закончился.')
    return delay_seconds


@async_timed()
async def fetch_status(session: ClientSession,
                       url: str,
                       delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


def load_common_words() -> List[str]:
    result = []

    with open('1-1000.txt') as common_words:
        while True:
            line = common_words.readline()
            if not line:
                break
            result.append(line)

    return result
