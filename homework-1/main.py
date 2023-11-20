"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

"""Connect to db"""
conn = psycopg2.connect(host='localhost', database='north',
                        user='postgres', password='o977kx', )

"""Create cursor"""
cur = conn.cursor()

"""Execute query"""


def csv_reader(filename: str) -> list:
    """
    Функция считывает информацию в файле
    :param filename: строка, название файла
    :return: список с кортежами
    """
    with open(f'north_data/{filename}', encoding='utf-8') as csvfile:
        all_info = csv.reader(csvfile)
        info_list = []

        for i in all_info:
            info_list.append(tuple(i))
    return info_list


def customers() -> None:
    """
    Функция заполняет таблицу customers в базе данных
    :return:
    """
    customers_list = csv_reader('customers_data.csv')

    for i in customers_list[1:]:
        cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', i)
        conn.commit()


def employees() -> None:
    """
    Функция заполняет таблицу customers в базе данных
    :return:
    """
    employees_list = csv_reader('employees_data.csv')

    for i in employees_list[1:]:
        cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', i)
        conn.commit()


def orders() -> None:
    """
    Функция заполняет таблицу customers в базе данных
    :return:
    """
    orders_list = csv_reader('orders_data.csv')

    for i in orders_list[1:]:
        cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', i)
        conn.commit()


orders()
cur.execute('SELECT * FROM orders')
rows = cur.fetchall()
for row in rows:
    print(row)

"""Close cursor and connection"""
cur.close()
conn.close()

