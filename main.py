from database.connection import get_connection
from employee import Employee
from services.employee_service import(add_employee,view_employees,search_employee,delete_employee,update_employee)

def main():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Update Employee")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("\nEnter Employee Details")
            name = input("Enter Employee Name: ")
            email = input("Enter Employee Email: ")
            if "@" not in email or "." not in email:
                print("Invalid email! Please enter a valid email address.")
                continue
            phone = input("Enter Employee Phone Number: ")
            if not phone.isdigit() or len(phone) != 10:
                print("Invalid phone number! Please enter a valid phone number.")
                continue
            department = input("Enter Employee Department: ")
            designation = input("Enter Employee Designation: ")
            joining_date = input("Enter Employee Joining Date(YYYY-MM-DD): ")
            salary_input = input("Enter Employee Salary: ")
            if not salary_input.isdigit():
                print("Invalid salary! Please enter numbers only.")
            else:
                salary = float(salary_input)
                status = input("Enter Employee Status: ")
                if salary > 0:
                    employee = Employee(name, email, phone, department, designation, joining_date, salary, status)
                    add_employee(employee)
                else:
                 print("Invalid salary! salary must be greater than 0")
        elif choice == 2:
            view_employees()
        elif choice == 3:
            employee_id = int(input("Enter Employee ID to search: "))
            search_employee(employee_id)
        elif choice == 4:
            employee_id = int(input("Enter Employee ID to delete: "))
            delete_employee(employee_id)
        elif choice == 5:
            employee_id = int(input("Enter Employee ID to update: "))
            name = input("Enter Employee Name: ")
            email = input("Enter Employee Email: ")
            phone = input("Enter Employee Phone Number: ")
            department = input("Enter Employee Department: ")
            designation = input("Enter Employee Designation: ")
            joining_date = input("Enter Employee Joining Date(YYYY-MM-DD): ")
            salary = float(input("Enter Employee Salary: "))
            status = input("Enter Employee Status: ")
            update_employee(employee_id, name, email, phone, department, designation, joining_date, salary, status)
        elif choice == 6:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
   main()