import psycopg2
import os
from easeoflife import os_or_default



try:
    connection = psycopg2.connect(host=os_or_default("DB_IP", '20.160.194.133'),
                                  port=os_or_default("DB_PORT", "5432"),
                                  database=os_or_default("DB_NAME", "aks_project_db"),
                                  user=os_or_default("DB_USER", 'python'),
                                  password=os_or_default("DB_PASSWORD", 'pythonTEST123_'))
except:
    print("I am unable to connect to the database")




# connection = psycopg2.connect(host=os.getenv("DB_IP") if os.getenv("DB_IP") != None else DB_IP, port="5432", database='test_erp', user='postgres', password='deeznuts12345_')

cursor = connection.cursor()
cursor.execute("""SELECT * FROM """)

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
