from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def display(self):
        pass
class Employee:
    def __init__(self, employee_id="", name="", age=0, salary=0):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def display(self):
        class_name = self.__class__.__name__
        print(f"\n{class_name} Details:")
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")
        print(f"{class_name} ID: {self.get_employee_id()}")
        print(f"Salary : {self.get_salary()}")

    def __del__(self):
        pass
        # return "Employee Object Deleted" #Not display deconstructor.


class Manager(Employee):
    def __init__(self, employee_id="", name="", age=0, salary=0, department=""):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department :", self.department)


class Developer(Employee):
    def __init__(self, employee_id="", name="", age=0, salary=0, programming_language=""):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print("Programming_Language: ", self.programming_language)


employee1 = None
manager1 = None
developer1 = None

print("--- Python OOP Project: Employee Management System ---")
while True:
    print("\nChoose an option:")
    print("1. Create an Employee")
    print("2. Create a Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Exit")
    try:
        choice1 = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter only a number.")
        continue
    match choice1:
        case 1:
            emp_name = input("\nEnter Name: ")
            emp_age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            emp_salary = float(input("Enter salary: "))

            employee1 = Employee(emp_id, emp_name, emp_age, emp_salary)  # created object.
            print(f"\nEmployee Created with name: {emp_name}, age: {emp_age}, ID: {emp_id}, and salary: ${emp_salary}.")
            # print(issubclass(Employee,Developer))
            print("\n--- Choose another operation ---")

        case 2:
            manager_name = input("\nEnter Name: ")
            manager_age = int(input("Enter Age: "))
            manager_id = input("Enter Manager ID: ")
            manager_salary = float(input("Enter Salary: "))
            manager_department = input("Enter Department: ")

            manager1 = Manager(
                manager_id,
                manager_name,
                manager_age,
                manager_salary,
                manager_department,
            )  # object created for manager
            print(f"\nManager Created with name: {manager_name}, age: {manager_age}, ID: {manager_id}, salary: ${manager_salary}, and department: {manager_department}.")
            print(issubclass(Manager, Employee))
            print("\n--- Choose another operation ---")

        case 3:
            developer_name = input("\nEnter Name: ")
            developer_age = int(input("Enter Age: "))
            developer_id = input("Enter Developer ID: ")
            developer_salary = float(input("Enter Salary: "))
            developer_programming_language = input("Enter Programming Language: ")
            developer1 = Developer(
                developer_id,
                developer_name,
                developer_age,
                developer_salary,
                developer_programming_language,
            )  # object created for Developer
            print(f"Developer created name: {developer_name}, age: {developer_age}, ID: {developer_id}, salary: ${developer_salary}, and programming language: {developer_programming_language}.")
            print(issubclass(Developer, Employee))
            print("\n--- Choose another operation ---")

        case 4:
            print("\nChoose Details To Show")
            print("1. Employee")
            print("2. Manager")
            print("3. Developer")
            user1 = int(input("Enter Your Choice: "))
            match user1:
                case 1:
                    if employee1 is not None:
                        employee1.display()
                    else:
                        print("Employee Not Found!")
                case 2:
                    if manager1 is not None:
                        manager1.display()
                    else:
                        print("Manager Not Found!")
                case 3:
                    if developer1 is not None:
                        developer1.display()
                    else:
                        print("Developer Not Found!")
                case _:
                    print("Invalid Choice!")
            print("\n--- Choose another operation ---")

        case 5:
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!")
            break 

        case _:
            print("Invalid choice!")
