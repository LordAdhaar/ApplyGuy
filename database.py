import psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta
import os
import sys
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

def create_table():
    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            id SERIAL PRIMARY KEY,
            company_name TEXT NOT NULL,
            company_website TEXT NOT NULL,
            job_position TEXT NOT NULL,
            founder_email TEXT NOT NULL,
            email_date DATE NOT NULL,
            email_sent BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        conn.commit()
        print("Table created successfully")
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()

def add_company(company_name, company_website, job_position, founder_email, email_date=None):
    # If no email date is provided, set it to tomorrow
    if not email_date:
        email_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    
    conn = None
    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO companies (company_name, company_website, job_position, founder_email, email_date)
        VALUES (%s, %s, %s, %s, %s)
        ''', (company_name, company_website, job_position, founder_email, email_date))
        
        conn.commit()
        print(f"Added {company_name} to the database. Email scheduled for {email_date}")
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()

def delete_company(company_id):

    conn = None
    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()
        
        # First check if the company exists
        cursor.execute("SELECT company_name FROM companies WHERE id = %s", (company_id,))
        result = cursor.fetchone()
        
        if not result:
            print(f"No company found with ID: {company_id}")
            cursor.close()
            conn.close()
            return False
            
        company_name = result[0]
        
        # Delete the company
        cursor.execute("DELETE FROM companies WHERE id = %s", (company_id,))
        
        conn.commit()
        print(f"Company '{company_name}' (ID: {company_id}) was successfully deleted.")
        cursor.close()
        conn.close()
        return True
        
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
        return False
            
def display_usage():
    print("Usage:")
    print("  python3 database.py create_table          - Create the companies table")
    print("  python3 database.py add_company           - Add an dummy company to the database")
    print("  python3 database.py delete_company ID     - Delete a company by ID")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        display_usage()
    else:
        command = sys.argv[1]
        
        if command == "create_table":
            create_table()
            print("Companies table created successfully")
        
        elif command == "add_company":
            add_company(
                "Example Company",
                "https://example.com",
                "Software Engineer",
                "founder@example.com",
                "2025-03-15"  # Format: YYYY-MM-DD
            )
        
        elif command == "delete_company":
            if len(sys.argv) < 3:
                print("Error: Company ID is required")
                display_usage()
            else:
                try:
                    company_id = int(sys.argv[2])
                    delete_company(company_id)
                except ValueError:
                    print("Error: Company ID must be a number")

        else:
            print(f"Unknown command: {command}")
            display_usage()