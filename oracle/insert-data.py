import oracledb as cx_Oracle
import csv
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
# Predefine the memory areas to match the table definition.
# This can improve performance by avoiding memory reallocations.
# Here, one parameter is passed for each of the columns.
# "None" is used for the ID column, since the size of NUMBER isn't
# variable.  The "25" matches the maximum expected data size for the
# NAME column
# cursor.setinputsizes(None, 25)

# Adjust the number of rows to be inserted in each iteration
# to meet your memory and performance requirements
batch_size = 10000

with open('Data8317.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    sql = "insert into test (year,age,ethnic,sex,area,count) values (:1, :2, :3, :4, :5, :6)"
    data = []
    next(csv_reader)
    for line in csv_reader:
        data.append((line[0], line[1], line[2], line[3], line[4], line[5]))
        if len(data) % batch_size == 0:
            cursor.executemany(sql, data)
            data = []
        if len(data) > 9000:
            break
    if data:
        cursor.executemany(sql, data)
    connection.commit()