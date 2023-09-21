# Define the Employee class
class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def update_salary_by_department(self, department, percent_increase):
        if self.department == department:
            self.salary *= (1 + percent_increase / 100)

# Ask the user for the number of employee details to input
no_of_employees = int(input('Enter the number of employee details required: '))
employees = []  # Create an empty list to store employee objects

# Input employee details and create Employee objects+
for i in range(no_of_employees):
    print(f"Enter {i+1}th employee details:")
    name = input("Employee name: ")
    id = input("Employee ID: ")
    dept = input("Employee department: ")
    sal = int(input("Employee salary: "))
    employees.append(Employee(name, id, dept, sal))

# Print header for the employee details table
print('EmpName\tEmpId\tEmpDept\tEmpSalary\n')

# Print employee details
for emp in employees:
    print(emp.name, '\t', emp.employee_id, '\t', emp.department, '\t', emp.salary)

# Ask the user for the department to update the salary
dept = input('Enter the department to update the salary: ')

# Increase salaries of employees in the specified department by 10%
for employee in employees:
    if employee.department == dept:
        employee.update_salary_by_department(dept, 10)

# Print updated salaries
for employee in employees:
    print(employee.name, employee.salary)
