from queries import *
from typing import Iterable
from psycopg2 import sql

# todo: Здесь нужно перенести в системные переменные
DB_HOST = '172.16.0.39'
DB_NAME = 'remote_data'
DB_USERNAME = 'monitoring'
DB_PASSWORD = 'KMKRadmin2021'


# Функция для получения последнего значения из таблиц c параметрами.
#     conn: - подключение к базе данных
#     tbl_name: - имя таблицы
#     _well_id: - номер скважины

def fetch_last_val(conn: any, tbl_name: str, _well_id: int) -> Iterable:
    cursor = conn.cursor()

    cursor.execute(sql.SQL(FETCH_LAST).format(
        table=sql.Identifier(tbl_name)
    ), [_well_id])

    result = cursor.fetchall()
    cursor.close()
    
    return result


# Функция для получения последнего значения из таблиц c параметрами.
#     conn: - подключение к базе данных
#     tbl_name: - имя таблицы
#     _well_id: - номер скважины
#     _value: - вставляемое значение

def insert_in(conn: any, tbl_name: str, _well_id: int, _value: float) -> bool:
    cursor = conn.cursor()

    cursor.execute(sql.SQL(INSERT_IN).format(
        table=sql.Identifier(tbl_name)
    ), [_well_id, _value])
    conn.commit()
    cursor.close()

    return True


# Получить список скважин
def fetch_wells(conn: any) -> Iterable:
    j_obj = {}
    cursor = conn.cursor()

    cursor.execute(sql.SQL(FETCH_WELLS))

    result = cursor.fetchall()
    cursor.close()

    for idx, item in enumerate(result):
        updates = dict([("well_name", item[0]), ("well_id", item[1]), ("deposit_name", item[2])])
        j_obj.update({idx: updates})
        del updates

    return j_obj
