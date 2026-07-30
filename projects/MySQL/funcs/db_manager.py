import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load local .env file into system environment variables
load_dotenv()

# Define top-of-file constants pulled securely from environment
DB_HOST = os.getenv("DB_HOST", "")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "")


class EmployeeDB:
    """Manages connection and SQL queries for the MySQL database."""
    
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
        except Error as e:
            print(f"Database connection error: {e}")
            self.mydb = None

    def _execute_select(self, query: str, params: tuple = None) -> list:
        """Internal helper to execute SELECT queries and return rows as dictionaries."""
        if not self.mydb or not self.mydb.is_connected():
            print("Database not connected.")
            return []
        
        cursor = self.mydb.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except Error as e:
            print(f"Select query failed: {e}")
            return []
        finally:
            cursor.close()

    def _execute_insert(self, query: str, params: tuple):
        """Internal helper to execute INSERT queries and return the auto-incremented ID."""
        if not self.mydb or not self.mydb.is_connected():
            print("Database not connected.")
            return None
        
        cursor = self.mydb.cursor()
        try:
            cursor.execute(query, params)
            self.mydb.commit()
            return cursor.lastrowid
        except Error as e:
            self.mydb.rollback()
            print(f"Insert query failed: {e}")
            return None
        finally:
            cursor.close()

    # --- Employees Table Operations ---

    def get_all_employees(self) -> list:
        """Fetches all records from the employees table."""
        return self._execute_select("SELECT id, first_name, last_name, date_birth FROM employees")

    def insert_employee(self, first_name: str, last_name: str, date_birth: str) -> int:
        """Inserts a new employee and returns their assigned database ID."""
        query = "INSERT INTO employees (first_name, last_name, date_birth) VALUES (%s, %s, %s)"
        return self._execute_insert(query, (first_name, last_name, date_birth))

    # --- Employee Details Table Operations ---

    def get_all_employee_details(self) -> list:
        """Fetches all records from the employee_details table."""
        query = """
            SELECT id, address_line1, address_line2, city, state_province_region, 
                   postal_code, country_code, phone_no 
            FROM employee_details
        """
        return self._execute_select(query)

    def insert_employee_detail(self, emp_id: int, addr1: str, addr2: str, city: str, 
                               state: str, postal: str, country: str, phone: str) -> int:
        """Inserts address and contact info tied to an employee ID."""
        query = """
            INSERT INTO employee_details (id, address_line1, address_line2, city, 
                                         state_province_region, postal_code, country_code, phone_no)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (emp_id, addr1, addr2, city, state, postal, country, phone)
        return self._execute_insert(query, params)

    def close(self):
        """Safely closes the active database connection."""
        if self.mydb and self.mydb.is_connected():
            self.mydb.close()