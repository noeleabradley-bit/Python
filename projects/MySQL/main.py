import datetime
import re
from funcs.db_manager import EmployeeDB
from funcs.validators import validate_date, validate_phone, prompt_user

# ==========================================
# MAIN EXECUTION ORCHESTRATOR
# ==========================================

def run_manual_insert(db: EmployeeDB):
    """Handles UI flow for collecting, validating, and saving a new record."""
    print("\n--- [Step 1] Base Employee Information ---")
    first_name = prompt_user("First Name: ")
    last_name = prompt_user("Last Name: ")
    
    while True:
        raw_dob = prompt_user("Date of Birth (YYYY-MM-DD): ")
        date_birth = validate_date(raw_dob)
        if date_birth:
            break
        print("Invalid date format! Try again.")

    # Write primary record to get the auto-incremented ID
    emp_id = db.insert_employee(first_name, last_name, date_birth)
    if not emp_id:
        print("Database failed to generate an Employee ID. Aborting details step.")
        return

    print(f"-> Base employee profile saved. Generated ID: {emp_id}")

    print("\n--- [Step 2] Contact & Address Information ---")
    addr1 = prompt_user("Address Line 1: ")
    addr2 = prompt_user("Address Line 2 (Optional): ", allow_empty=True)
    city = prompt_user("City: ")
    state = prompt_user("State/Province/Region: ")
    postal = prompt_user("Postal Code: ")
    
    while True:
        country = prompt_user("Country Code (2 characters, e.g., US): ")
        if len(country) == 2:
            country = country.upper()
            break
        print("Error: Country code must be exactly 2 letters.")

    while True:
        raw_phone = prompt_user("Phone Number (International format, e.g., 0013455053456): ")
        phone_no = validate_phone(raw_phone)
        if phone_no:
            break
        print("Error: Invalid phone structure. Use numeric characters (7-15 digits).")

    # Write secondary record linked by the employee ID
    success = db.insert_employee_detail(emp_id, addr1, addr2, city, state, postal, country, phone_no)
    if success:
        print("\nSuccess: Profile and contact specifics fully synchronized.")
    else:
        print("\nWarning: Profile was established, but address processing failed.")


def view_tables(db: EmployeeDB):
    """Displays snapshots of current data configurations."""
    print("\n--- Employees Base Table ---")
    employees = db.get_all_employees()
    if not employees:
        print("No employee data records returned.")
    for emp in employees:
        print(f"ID: {emp['id']} | Name: {emp['first_name']} {emp['last_name']} | DOB: {emp['date_birth']}")

    print("\n--- Employee Details Profile Table ---")
    details = db.get_all_employee_details()
    if not details:
        print("No context address records returned.")
    for det in details:
        print(f"ID: {det['id']} | Address: {det['address_line1']}, {det['city']} | Phone: {det['phone_no']}")


def main():
    db = EmployeeDB()
    if not db.mydb:
        print("Initialization failed: Unable to bind application engine to MySQL pipeline.")
        return

    while True:
        print("\n======================================")
        print("        MY_FUNCS CONTROL CORE         ")
        print("======================================")
        print("1. Manually Provision New Employee")
        print("2. Display Database Table Snapshots")
        print("3. Exit Application Space")
        
        choice = prompt_user("Selection: ")
        if choice == "1":
            run_manual_insert(db)
        elif choice == "2":
            view_tables(db)
        elif choice == "3":
            print("Severing connections. Exiting runtime framework.")
            db.close()
            break
        else:
            print("Invalid operator statement selection.")


if __name__ == "__main__":
    main()