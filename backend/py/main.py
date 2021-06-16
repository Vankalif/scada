import psycopg2
from fastapi import FastAPI
from datetime import datetime
from starlette import status
from fastapi.middleware.cors import CORSMiddleware

from db import *
from schemas import Param

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
    # sdate_ = datetime.fromisoformat(sdate)
    # edate_ = datetime.fromisoformat(edate)
    result = get_chart_data(connection, table, sdate, edate, w_id)
    return result

