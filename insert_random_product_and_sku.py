import asyncio
import asyncpg
from random import sample, randint
from typing import List, Tuple
from add_functions import load_common_words


def generate_products(common_words: List[str],
                 brand_id_start: int,
                 brand_id_end: int,
                 amount_products: int) -> List[Tuple[str, int]]:
    products = []
    for _ in range(amount_products):
        description = [common_words[index].rstrip() for index in sample(range(1000), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))
    return products


def generate_skus(product_id_start: int,
                  product_id_end: int,
                  amount_skus: int) -> List[Tuple[int, int, int]]:
    skus = []
    for _ in range(amount_skus):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))
    return skus

async def insert_new_products_and_skus(connection):
    common_words = load_common_words()
    product_tuples = generate_products(common_words,
                                       brand_id_start=1,
                                       brand_id_end=100,
                                       amount_products=1000)
    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)",
                                 product_tuples)

    sku_tuples = generate_skus(product_id_start=1,
                               product_id_end=1000,
                               amount_skus=100000)
    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)",
                                 sku_tuples)


async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='vova130399')

    product_tuples = generate_products(common_words,
                                       brand_id_start=1,
                                       brand_id_end=100,
                                       amount_products=1000)
    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)",
                                 product_tuples)

    sku_tuples = generate_skus(product_id_start=1,
                               product_id_end=1000,
                               amount_skus=100000)
    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)",
                                 sku_tuples)

    await connection.close()

asyncio.run(main())
