from database.connection import get_connection
def add_employee(employee):
    connection = get_connection()
    cursor = connection.cursor()
    query = """INSERT INTO employees(name,email,phone,department,designation,joining_date,salary,status)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (employee.name,employee.email,employee.phone,employee.department,employee.designation,employee.joining_date,employee.salary,employee.status)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    print("Employee added successfully!")

def view_employees():
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM employees"""
    cursor.execute(query)
    employees = cursor.fetchall()

    if employees:
        print("\n=============== Employee Details ==============")
        print("ID | Name | Email | Phone | Department | Designation | Joining_date | Salary | Status")
        print("_" * 110)
        for employee in employees:
            print(employee)
        else:
            print("No employees found!")
            cursor.close()
            connection.close()

def search_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """SELECT * FROM employees WHERE employee_id = %s"""
    cursor.execute(query, (employee_id,))
    found_employee = cursor.fetchone()
    if found_employee:
        print("Employee found!")
        print("Employee Details:")
        print(found_employee)
    else:
        print("Employee not found!")
        cursor.close()
        connection.close()

def delete_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """DELETE FROM employees WHERE employee_id = %s"""
    cursor.execute(query, (employee_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")
        cursor.close()
        connection.close()

def update_employee(employee_id, name, email, phone, department, designation, joining_date, salary, status):
    connection = get_connection()
    cursor = connection.cursor()

    query = """UPDATE employees SET name = %s, email = %s, phone = %s, department = %s, designation = %s, joining_date = %s,salary = %s, status = %s WHERE employee_id = %s"""
    values = (name, email, phone, department, designation, joining_date, salary, status, employee_id)
    cursor.execute(query, values)
    connection.commit()
    print("Employee updated successfully!")
    cursor.close()
    connection.close()


