import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee():
        employee_id = input("Enter Employee ID: ")
        if EmployeeManager.search_employee(employee_id, silent=True):
            print("Error: Employee ID must be unique.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found.")
                return
            print("Employee Records:")
            for line in lines:
                print(line.strip())

    @staticmethod
    def search_employee(employee_id, silent=False):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            if not silent:
                print("No records found.")
            return None
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == employee_id:
                    if not silent:
                        print("Employee Found:")
                        print(line.strip())
                    return data
        if not silent:
            print("Employee not found.")
        return None

    @staticmethod
    def update_employee():
        employee_id = input("Enter Employee ID to update: ")
        records = []
        updated = False

        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return

        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == employee_id:
                    name = input("Enter new Name: ") or data[1]
                    position = input("Enter new Position: ") or data[2]
                    salary = input("Enter new Salary: ") or data[3]
                    records.append(f"{employee_id},{name},{position},{salary}\n")
                    updated = True
                else:
                    records.append(line)
        
        if updated:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(records)
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def delete_employee():
        employee_id = input("Enter Employee ID to delete: ")
        records = []
        deleted = False

        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return

        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == employee_id:
                    deleted = True
                else:
                    records.append(line)
        
        if deleted:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(records)
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def run():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                EmployeeManager.add_employee()
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                EmployeeManager.search_employee(emp_id)
            elif choice == "4":
                EmployeeManager.update_employee()
            elif choice == "5":
                EmployeeManager.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
EmployeeManager.run()
