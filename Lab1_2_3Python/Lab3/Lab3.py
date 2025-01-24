#Zad 1,2
import json

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def to_dict(self):
        return {"name": self.name, "age": self.age, "salary": self.salary}

    @staticmethod
    def from_dict(data):
        return Employee(data["name"], data["age"], data["salary"])

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeesManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.employees = self.load_employees()

    def load_employees(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [Employee.from_dict(emp) for emp in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_employees(self):
        with open(self.file_path, "w") as file:
            json.dump([emp.to_dict() for emp in self.employees], file, indent=4)

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_employees()

    def list_employees(self):
        return self.employees

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        self.save_employees()

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, new_salary):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.salary = new_salary
            self.save_employees()
            return True
        return False

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager("employees.json")

    def login(self):
        print("Login to the Employees System")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        return username == "admin" and password == "admin"

    def run(self):
        if not self.login():
            print("Invalid credentials. Exiting system.")
            return

        while True:
            print("\n--- Employees System Menu ---")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Remove Employees by Age Range")
            print("4. Update Employee Salary")
            print("5. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                name = input("Enter name: ").strip()
                age = input("Enter age: ").strip()
                salary = input("Enter salary: ").strip()

                if not age.isdigit() or not salary.replace('.', '', 1).isdigit():
                    print("Error: Age and salary must be numeric values.")
                    continue

                employee = Employee(name, int(age), float(salary))
                self.manager.add_employee(employee)
                print("Employee added successfully.")

            elif choice == "2":
                employees = self.manager.list_employees()
                if not employees:
                    print("No employees found.")
                else:
                    for emp in employees:
                        print(emp)

            elif choice == "3":
                min_age = input("Enter minimum age: ").strip()
                max_age = input("Enter maximum age: ").strip()

                if not min_age.isdigit() or not max_age.isdigit():
                    print("Error: Age range values must be numeric.")
                    continue

                self.manager.remove_employees_by_age_range(int(min_age), int(max_age))
                print("Employees in the specified age range have been removed.")

            elif choice == "4":
                name = input("Enter the name of the employee: ").strip()
                new_salary = input("Enter the new salary: ").strip()

                if not new_salary.replace('.', '', 1).isdigit():
                    print("Error: Salary must be a numeric value.")
                    continue

                if self.manager.update_salary_by_name(name, float(new_salary)):
                    print("Employee salary updated successfully.")
                else:
                    print("Employee not found.")

            elif choice == "5":
                print("Exiting system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    FrontendManager().run()
