import asyncpg
import asyncio
from asyncpg import Record
from typing import List

async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='postgres',
                                       password='password')


    '''
    Еще один вариант исполнения команд. Закомментировано, так как при 
    каждой компиляции добавляет в таблицу эти два бренда
    '''
    '''
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")
    '''
    # query - запрос
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    '''
    connection.fetch позволяет выбрать все марки из таблицы brand
    Каждый результат представлен объектом asyncpg Record.
    Эти объекты похожи на словари: они позволяют обращаться к данным,
    передавая имя столбца в качестве индекса.
    '''
    results: List[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    await connection.close()

asyncio.run(main())
