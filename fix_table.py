import asyncpg
import asyncio


async def main():
    '''
    Подключаемся к б/д postgres,
    которую заранее создали (не в python - коде)
    '''
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='vova130399')
    '''
    Создадим список команд для очистки таблиц
    '''
    clear_tables = ['DELETE FROM sku;',
                    'DELETE FROM product;',
                    'DELETE FROM brand;']

    for command in clear_tables:
        status = await connection.execute(command)
        print(status)
    print('Все ок, данные удалены!')

    '''
    Теперь откатим параметры по умолчанию до начального состояния
    '''
    set_default = ['ALTER SEQUENCE sku_id_seq RESTART;',
                   'ALTER SEQUENCE product_id_seq RESTART;',
                   'ALTER SEQUENCE brand_id_seq RESTART;']
    for command in set_default:
        status = await connection.execute(command)
        print(status)
    print('Все ок, дефолты откачены!')

    await connection.close()


asyncio.run(main())
