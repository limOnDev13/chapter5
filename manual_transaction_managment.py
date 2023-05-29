import asyncio
import asyncpg
from asyncpg.transaction import Transaction


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='vova130399')

    transaction: Transaction = connection.transaction()
    await transaction.start()
    try:
        await connection.execute("INSERT INTO brand "
                                 "VALUES (DEFAULT, 'brand_3')")
        await connection.execute("INSERT INTO brand "
                                 "VALUES (DEFAULT, 'brand_4')")

    except asyncpg.PostgresError:
        print('Ошибка, транзакция откатывается!')
        await connection.rollbasck()
    else:
        print('Ошибки нет, транзакция фиксируется!')
        await transaction.commit()

    query = \
        """
        SELECT brand_name FROM brand
        WHERE brand_name LIKE 'brand%'
        """
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()

asyncio.run(main())
