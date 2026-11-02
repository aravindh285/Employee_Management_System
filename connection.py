import mysql.connector
def get_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='MySql@1234',
        database='employee_management')
    return conn

if __name__ == '__main__':
    connection = get_connection()
    if connection.is_connected():
        print("Database Connected successfully")
        connection.close()