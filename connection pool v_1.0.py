import asyncio
import asyncpg
from sql_statements import product_query


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


async def main():
    async with asyncpg.create_pool(host='127.0.0.1',
                                   port=5432,
                                   user='postgres',
                                   password='vova130399',
                                   database='products',
                                   min_size=6,
                                   max_size=6) as pool:
        await asyncio.gather(query_product(pool),
                             query_product(pool))

asyncio.run(main())
