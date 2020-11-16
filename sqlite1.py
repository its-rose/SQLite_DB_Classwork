# Базы данных - SQlite

import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()


def create_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS users( 
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT,
    lname TEXT,
    gender TEXT); """)
    conn.commit()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS orders(
        orderid INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        userid TEXT,
        total TEXT);
        """
    )
    conn.commit()


create_db()
cur.execute(
    """INSERT INTO users (fname, lname, gender)
    VALUES('Alex', 'Smith', 'male');
    """
)
conn.commit()

user = ('Lois', 'Lane', 'female')

cur.execute(f"INSERT INTO users (fname, lname, gender) VALUES{user};", )
conn.commit()
user2 = ('Peter', 'Parker', 'male')
user3 = ('Bruce', 'Wayne', 'male')

conn.commit()
cur.execute(f"INSERT INTO users (fname, lname, gender) VALUES{user2};", )
cur.execute(f"INSERT INTO users (fname, lname, gender) VALUES{user3};", )
conn.commit()

