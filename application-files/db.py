import psycopg2
import os

DB_IP = '40.118.48.151'

try:
    connection = psycopg2.connect(host=os.getenv("DB_IP") if os.getenv("DB_IP") != None else DB_IP,
                                  port="5432",
                                  database=os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "users",
                                  user='postgres',
                                  password='test123')
except:
    print("I am unable to connect to the database")




# connection = psycopg2.connect(host=os.getenv("DB_IP") if os.getenv("DB_IP") != None else DB_IP, port="5432", database='test_erp', user='postgres', password='deeznuts12345_')

cursor = connection.cursor()
cursor.execute("""SELECT * FROM user_info2 WHERE id=1""")

print(cursor)
for query in cursor:
    print(str(query))


    #"INSERT INTO clients (id, first_name, last_name, role) VALUES (2, 'ariel', 'agranovich', 'admin')"
    # """SELECT * FROM clients WHERE id=1"""


#import psycopg2
#
# connection = psycopg2.connect(host='20.126.75.122', port="5432", database='test_erp', user='postgres', password='deeznuts12345_')
#
# cursor = connection.cursor()
#
try:
    cursor.execute("INSERT INTO user_info2 VALUES (1, {b, a, n}, 'nuts')")
    connection.commit()  # Commit the transaction
    print("Record inserted successfully.")
except psycopg2.Error as e:
    connection.rollback()  # Roll back the transaction in case of an error
    print("Error:", e)
finally:
    cursor.close()
    connection.close()