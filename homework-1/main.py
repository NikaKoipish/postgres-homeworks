"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="123")
with open('north_data/employees_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    with conn.cursor() as cur:
        for row in reader:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s,%s, %s)",(row))
        cur.execute("SELECT * FROM employees")
        conn.commit()
        rows = cur.fetchall()


with open('north_data/customers_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    with conn.cursor() as cur:
        for row in reader:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",(row))
        cur.execute("SELECT * FROM customers")
        conn.commit()
        rows = cur.fetchall()

with open('north_data/orders_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    with conn.cursor() as cur:
        for row in reader:
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",(row))
        cur.execute("SELECT * FROM orders")
        conn.commit()
        rows = cur.fetchall()
conn.close()
