import asyncpg
import asyncio
from typing import List, Tuple, Union
from random import sample


def load_common_words() -> List[str]:
    '''
    Данная функция отличается от примера,
    в нем она была написана с ошибкой.
    Она нужна для загрузки самых популярных английских слов
    из файла 1-1000.txt в список
    '''
    result = []
    with open('1-1000.txt') as common_words:
        while True:
            line = common_words.readline()
            if not line:
                break
            result.append(line)
    return result


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str, ]]]:
    '''
    Эта функция собирает список случайных слов из переданного списка
    '''
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    '''
    Функция, которая делает всю магию.
    Передаем ей список слов (названий брендов), она вставляет их в таблицу.
    '''
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    '''
    executemany - метод для исполнения множественных sql - запросов
    Число после знака доллара равно индексу элемента КОРТЕЖА. 
    Количество кортежей (например в списке) равно количеству sql - команд.
    В нашем случае будет 100.
    '''
    return await connection.executemany(insert_brands, brands)


async def insert_new_brand(connection):
    common_words = load_common_words()
    await insert_brands(common_words, connection)


async def main():
    '''
    Осторожно! При компиляции в таблицу
    каждый раз будут добавляться 100 строк. Здесь мы просто собираем
    все выше описанные функции в единое целое.
    '''
    common_words = load_common_words()
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='vova130399')
    await insert_brands(common_words, connection)
    print(common_words)


asyncio.run(main())
