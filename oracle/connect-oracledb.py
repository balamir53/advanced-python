import oracledb as cx_Oracle
# import cx_Oracle
import getpass

password = getpass.getpass()

# cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\yusuf\Downloads\WINDOWS.X64_213000_db_home\bin")

# connection = cx_Oracle.connect(user='system', password=password,
#                                dsn='localhost:1521')

# Create the session pool
pool = cx_Oracle.SessionPool(user="data_owner", password=password,
                             dsn="localhost:1521/XE", min=2,
                             max=5, increment=1, encoding="UTF-8")

# Acquire a connection from the pool
connection = pool.acquire()

# Use the pooled connection
cursor = connection.cursor()
results=[]
for result in cursor.execute("select * from test"):
# for result in cursor.execute("select count(*) from test"):
    # print(result)
    results.append(result)
# Release the connection to the pool
pool.release(connection)

# Close the pool
pool.close()
