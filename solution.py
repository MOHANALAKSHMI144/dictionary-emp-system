# Solution
def add_employee(employees):
    """Adds a new employee with validations."""
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter Name: ")
    if not name.isalpha() and not all(x.isalpha() or x.isspace() for x in name):
        print("Invalid name. Name should contain only alphabets and spaces.")
        return

    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            raise ValueError
    except ValueError:
        print("Invalid age. Age should be a positive integer.")
        return

    department = input("Enter Department: ")

    employees[emp_id] = {"name": name, "age": age, "department": department}
    print("Employee added successfully!")

def remove_employee(employees):
    """Removes an employee by ID."""
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully!")
    else:
        print("Employee ID not found.")

def update_employee(employees):
    """Updates employee details."""
    emp_id = input("Enter Employee ID to update: ")
    if emp_id in employees:
        employee = employees[emp_id]
        print("Current details:", employee)

        name = input(f"Enter new Name ({employee['name']}): ") or employee["name"]
        if not name.isalpha() and not all(x.isalpha() or x.isspace() for x in name):
            print("Invalid name. Name should contain only alphabets and spaces.")
            return

        try:
            age = int(input(f"Enter new Age ({employee['age']}): ") or employee["age"])
            if age <= 0:
                raise ValueError
        except ValueError:
            print("Invalid age. Age should be a positive integer.")
            return

        department = input(f"Enter new Department ({employee['department']}): ") or employee["department"]

        employees[emp_id] = {"name": name, "age": age, "department": department}
        print("Employee updated successfully!")
    else:
        print("Employee ID not found.")

def search_employee(employees):
    """Searches employees by ID or name."""
    search_term = input("Enter Employee ID or Name to search: ")
    if search_term in employees:
        print("Employee found:", employees[search_term])
    else:
        found = False
        for emp_id, details in employees.items():
            if search_term.lower() == details["name"].lower():
                print("Employee found:", {emp_id: details})
                found = True
                break
        if not found:
            print("Employee not found.")

def sort_employees(employees):
    """Sorts employees by name, age, or department."""
    sort_by = input("Sort by (name/age/department): ").lower()
    if sort_by not in ["name", "age", "department"]:
        print("Invalid sort criteria.")
        return

    sorted_employees = sorted(employees.items(), key=lambda item: item[1][sort_by])
    print("Sorted Employees:")
    for emp_id, details in sorted_employees:
        print(f"{emp_id}: {details}")

def main():
    """Main function to run the Employee Management System."""
    employees = {}
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. Sort Employees")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            remove_employee(employees)
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            search_employee(employees)
        elif choice == "5":
            sort_employees(employees)
        elif choice == "6":
            print("Exiting Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
