import csv

import psycopg2

# Получаем данные из 'customers_data.csv'
def get_customers():
    file = open('north_data/customers_data.csv', newline='')
    customers = csv.DictReader(file)
    customers = list(customers)
    return customers

# Получаем данные из 'employees_data.csv'
def get_employees():
    file = open('north_data/employees_data.csv', newline='')
    employees = csv.DictReader(file)
    employees = list(employees)
    return employees

# получаем данные из 'order_data.csv'
def get_orders():
    file = open('north_data/orders_data.csv', newline='')
    orders = csv.DictReader(file)
    orders = list(orders)
    return orders


"""Скрипт для заполнения данными таблиц в БД Postgres."""
with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='18021994'
) as conn:
    with conn.cursor() as cur:
        for row in get_employees():
            cur.execute("INSERT INTO  employees VALUES (%s, %s, %s, %s, %s, %s)", (row['employee_id'],
                        row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes']))

        for row in get_customers():
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row['customer_id'], row['company_name'],
                        row['contact_name']))

        for row in get_orders():
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (row['order_id'], row['customer_id'],
                        row['employee_id'], row['order_date'], row['ship_city']))

conn.close()
