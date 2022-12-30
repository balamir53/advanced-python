import oracledb as cx_Oracle

import getpass

password = getpass.getpass()

# Create the session pool
pool = cx_Oracle.SessionPool(user="data_owner", password=password,
                             dsn="localhost:1521/XE", min=2,
                             max=5, increment=1, encoding="UTF-8")

# Acquire a connection from the pool
connection = pool.acquire()

# Use the pooled connection
cursor = connection.cursor()
try:
    # cursor.execute('''CREATE TABLE
    #                CodeSpeedy(employee_id number(10),employee_name varchar2(10))''')
    # Year,Age,Ethnic,Sex,Area,count
    cursor.execute('''create table test(year number(10), age number(10), ethnic number(10), sex number(10), area number(10), count number(10))''')
    print("Table Created")
    cursor.close()

except Exception as e:
    print("Error: ", str(e))
