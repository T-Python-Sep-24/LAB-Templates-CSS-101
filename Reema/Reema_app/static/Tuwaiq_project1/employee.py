# Import necessary modules
import json

# Function to display menu
def display_menu():
    print("\n--- Online Employee Recruitment System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

# Function to add an employee
def add_employee(employees):
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))

    employee_id = len(employees) + 1
    employees[employee_id] = {
        'name': name,
        'age': age,
        'position': position,
        'salary': salary
    }
    print("Employee added successfully!")

# Function to view all employees
def view_employees(employees):
    if not employees:
        print("No employees found.")
    else:
        for emp_id, details in employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Position: {details['position']}, Salary: {details['salary']}")

# Function to search for an employee
def search_employee(employees):
    emp_id = int(input("Enter employee ID to search: "))
    if emp_id in employees:
        details = employees[emp_id]
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Position: {details['position']}, Salary: {details['salary']}")
    else:
        print("Employee not found.")

# Main function
def main():
    employees = {}  # Dictionary to store employee data
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
