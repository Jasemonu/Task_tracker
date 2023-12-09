import sqlite3
from typing import List
import tdatetime
from model import Todo


conn = sqlite3.connect('todos.db')
cursor = conn.cursor()


def create_table():
    cursor.execute("""CFREATE TABLE IF NOT EXISTS todos (
                task text,
                category text,
                date_added text,
                date_completed text,
                status integer,
                position integer
                )""")
