import psycopg2
from fastapi import FastAPI, Response
from starlette import status
from fastapi.middleware.cors import CORSMiddleware
from schemas import User

from db import *

connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD)
app = FastAPI()


origins = [
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000",
    "http://localhost:8000",
    "https://localhost:8000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("shutdown")
async def shutdown():
    connection.close()


@app.get("/")
def hello() -> str:
    return "Status - OK"


@app.get("/current_values")
def get_last_in() -> Iterable:
    result = fetch_last_val(connection)
    return result


@app.get("/get_wells")
def get_wells():
    result = fetch_wells(connection)
    return result

#
# # TODO: Добавить ответ
# @app.post("/set_val_in", status_code=status.HTTP_201_CREATED)
# def create_param(param: Param):
#     insert_in(connection, param.table_name, param.well_id, param.value)
#     return None


@app.get("/get_chart/{table}")
def chart_data(table: str, sdate: str, edate: str, w_id: str):
    result = get_chart_data(connection, table, sdate, edate, w_id)
    return result


@app.get("/get_server_room_sensors_data")
def server_room_sensors_data(sdate: str, edate: str):
    result = get_server_room_sensors_data(connection, sdate, edate)
    return result


@app.post("/set_server_room_temp", status_code=status.HTTP_201_CREATED)
def create_server_room_temp_item(value: float):
    insert_in_server_room_temp(connection, value)
    return None


@app.post("/login")
def login():
    pass


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(usr: User, response: Response):
    result = create_user(connection, usr)
    if not result:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status_code": 500}
    return {"status_code": 201}
