import asyncpg
import asyncio
from sql_statements import *

async def main():
    '''
    Подключаемся к б/д postgres,
    которую заранее создали (не в python - коде)
    '''
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='postgres',
                                       password='password')

    '''
    Создаем список sql - команд, которые заранее
    прописали в файле sql - statements
    '''
    statements = [CREATE_BRAND_TABLE,
                  CREATE_PRODUCT_TABLE,
                  CREATE_PRODUCT_COLOR_TABLE,
                  CREATE_PRODUCT_SIZE_TABLE,
                  CREATE_SKU_TABLE,
                  SIZE_INSERT,
                  COLOR_INSERT]

    print('Создается база данных products...')
    '''
    connection.execute() - корутина, выполняющая sql - команды,
    раз корутина, то и результат нужно ждать через await.
    Так как таблицы зависят от других таблиц, то выполнять ДАННЫЕ команды
    следует синхронно (НЕ асинхронно, а по очереди)
    '''
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('База данных product готова!')
    await connection.close()

asyncio.run(main())
