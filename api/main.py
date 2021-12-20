from typing import Optional
from fastapi import FastAPI

import logging
from datetime import datetime

import psycopg2
import sys, os
import numpy as np
import pandas as pd
import pandas.io.sql as psql

conn_string = "host=db port=5432 dbname=postgres user=postgres password=example"

app = FastAPI()

logging.basicConfig(filename='./log/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def log(message):
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - " + message)

def connectDB():
    log("Trying to connect database")
    conn=None

    try:
        conn=psycopg2.connect(conn_string)
        log("Database connected!")
    except:
        log("Fail to connect on database")

    return conn

def insertLog(message):
    sql = "INSERT INTO log_request (message) VALUES(%s);"
    try:
        conn = connectDB()
        cur = conn.cursor()

        log("Try to insert data on database")

        cur.execute(sql, (message, ))
        conn.commit()
        cur.close()

        log("Row inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        log(str(error))
    finally:
        if conn is not None:
            conn.close()

@app.get("/")
def read_root():
    log("GET Requested")
    insertLog("New log message")

    return {"On postgres whe trust": "World with logs on db"}
