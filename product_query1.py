import asyncpg
import asyncio
from asyncpg import Record
from typing import List

async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='vova130399')

    # query - запрос
    product_query = \
    """
    SELECT DISTINCT
    p.product_id,
    p.product_name,
    p.brand_id,
    s.sku_id,
    pc.product_color_name,
    ps.product_size_name
    FROM product as p
    JOIN sku as s on s.product_id = p.product_id
    JOIN product_color as pc on pc.product_color_id = s.product_color_id
    JOIN product_size as ps on ps.product_size_id = s.product_size_id
    WHERE p.product_id = 100;
    """
    results: List[Record] = await connection.fetch(product_query)

    for product in results:
        print(f'product_id: {product["product_id"]},'
              f' product_name: {product["product_name"]}'
              f' brand_id: {product["brand_id"]}'
              f' sku_id: {product["sku_id"]}'
              f' product_color_name: {product["product_color_name"]}'
              f' product_size_name: {product["product_size_name"]}')

    await connection.close()

asyncio.run(main())
