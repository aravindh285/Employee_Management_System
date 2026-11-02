class Employee:
    def __init__(self,name,email,phone,department,designation,joining_date,salary,status="Active"):
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.designation = designation
        self.joining_date = joining_date
        self.salary = salary
        self.status = status