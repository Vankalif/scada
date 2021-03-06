import hashlib

import psycopg2

from queries import *
from typing import Iterable
from psycopg2 import sql
from psycopg2 import extras
from datetime import datetime
from schemas import User


# todo: Здесь нужно перенести в системные переменные
DB_HOST = '172.16.0.39'
DB_NAME = 'remote_data'
DB_USERNAME = 'monitoring'
DB_PASSWORD = 'KMKRadmin2021'


# Функция для получения последнего значения из таблиц c параметрами.
#     conn: - подключение к базе данных
def fetch_last_val(conn: any) -> Iterable:
    j_obj = {}
    cursor = conn.cursor()

    cursor.execute(sql.SQL(FETCH_LAST))

    result = cursor.fetchall()
    cursor.close()
    for idx, item in enumerate(result):
        updates = dict([("well_id", item[0]),
                        ("well_name", item[1]),
                        ("deposit_id", item[2]),
                        ("deposit_name", item[3]),
                        ("temperature", item[4]),
                        ("temperature_timestamp", item[5]),
                        ("pressure", item[6]),
                        ("pressure_timestamp", item[7]),
                        ("level", item[8]),
                        ("level_timestamp", item[9]),
                        ])
        j_obj.update({idx: updates})
        del updates
    
    return j_obj


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
    cursor = conn.cursor(cursor_factory=extras.DictCursor)

    cursor.execute(sql.SQL(FETCH_WELLS))

    result = cursor.fetchall()
    cursor.close()

    for idx, item in enumerate(result):
        updates = dict([("well_name", item[0]), ("well_id", item[1]), ("deposit_name", item[2])])
        j_obj.update({idx: updates})
        del updates

    return j_obj


# Получить данные для построения графика
def get_chart_data(conn: any, tbl_name: str, start_date: str, end_date: str, well_id: str) -> Iterable:
    j_obj = {'vals': [], 'dates': []}
    cursor = conn.cursor()

    cursor.execute(sql.SQL(CHART_DATA).format(
        table=sql.Identifier(tbl_name),
    ), [str(datetime.fromisoformat(start_date)), str(datetime.fromisoformat(end_date)), int(well_id)])

    result = cursor.fetchall()
    cursor.close()

    for item in result:
        j_obj['vals'].append(item[0])
        j_obj['dates'].append(item[1].strftime("%Y-%m-%d %H:%M:%S"))

    return j_obj


def get_server_room_sensors_data(conn: any, start_date: str, end_date: str) -> Iterable:
    j_obj = {'vals': [], 'dates': []}
    cursor = conn.cursor()
    one = str(datetime.fromisoformat(start_date))
    two = str(datetime.fromisoformat(end_date))
    print(one, two)
    cursor.execute(sql.SQL(SERVER_ROOM_TEMP), [str(datetime.fromisoformat(start_date)),
                                               str(datetime.fromisoformat(end_date))])

    result = cursor.fetchall()
    cursor.close()

    for item in result:
        j_obj['vals'].append(item[0])
        j_obj['dates'].append(item[1].strftime("%H:%M"))

    return j_obj


def insert_in_server_room_temp(conn: any, _value: float) -> bool:
    cursor = conn.cursor()

    cursor.execute(sql.SQL(INSERT_IN_SERVER_ROOM_TEMP), [float(_value)])
    conn.commit()
    cursor.close()

    return True


def create_user(conn: ..., user: User) -> bool:
    cursor = conn.cursor()
    user.password = hashlib.sha256(user.password.encode()).hexdigest()
    try:
        cursor.execute(sql.SQL(INSERT_IN_USERS), [user.name,
                                                  user.surname,
                                                  user.patronymic,
                                                  user.login,
                                                  user.password])
        conn.commit()
        cursor.close()
        return True
    except psycopg2.Error:
        cursor.close()
        return False
