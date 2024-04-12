import psycopg2
from psycopg2 import sql
from psycopg2 import Error

DB_NAME = "gym"
DB_USER = "postgres"
DB_PASSWORD = "660caa4e5c"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = connection.cursor()
    print("Connected to database successfully")
except Error as e:
    print(f"Error while connecting to PostgreSQL: {e}")
    exit()

# Account creation
def create_account():
    print("You chose to create a new account.")
    choice = input("What kind of account would you like to create? (Member/Trainer/Admin/Exit): ")

    if choice.lower() == 'member':
        username = input("Choose your account name: ")
        password = input("Choose your password: ")
        email = input("Enter your email: ")
        fullname = input("Enter your full name: ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        gender = input("Enter your gender: ")

        create_member(username, password, email, fullname, dob, gender)

    elif choice.lower() == 'trainer':
        username = input("Choose your account name: ")
        password = input("Choose your password: ")
        email = input("Enter your email: ")
        fullname = input("Enter your full name: ")

        create_trainer(username, password, email, fullname)

    elif choice.lower() == 'admin':
        username = input("Choose your account name: ")
        password = input("Choose your password: ")
        email = input("Enter your email: ")
        fullname = input("Enter your full name: ")
        role = input("Enter your role: ")

        create_admin(username, password, email, fullname, role)

    else:
        choice = 'exit'
    
    return choice.lower()

def create_member(username, password, email, fullname, dob, gender):
    try:
        cursor.execute(
            sql.SQL("INSERT INTO members (username, password, email, full_name, date_of_birth, gender) VALUES (%s, %s, %s, %s, %s, %s)"),
            (username, password, email, fullname, dob, gender)
        )
        connection.commit()
        print("Member created successfully")
    except Error as e:
        connection.rollback() 
        print(f"Error creating member: {e}")

def create_trainer(username, password, email, fullname):
    try:
        cursor.execute(
            sql.SQL("INSERT INTO trainers (username, password, email, full_name) VALUES (%s, %s, %s, %s) RETURNING trainer_id"),
            (username, password, email, fullname)
        )
        trainer_id = cursor.fetchone()[0]
        
        availability_slots = []
        print("Enter your availablility")
        while True:
            day_of_week = input("Enter day of the week (e.g., Monday): ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            availability_slots.append((trainer_id, day_of_week, start_time, end_time))
            another_slot = input("Do you want to add another availability slot? (yes/no): ").lower()
            print()
            if another_slot != 'yes':
                break
        
        for slot in availability_slots:
            cursor.execute(
                sql.SQL("INSERT INTO AvailabilitySlots (trainer_id, day_of_week, start_time, end_time) VALUES (%s, %s, %s, %s)"),
                slot
            )
        
        connection.commit()
        print("Trainer and availability slots created successfully")
    except Error as e:
        connection.rollback()
        print(f"Error creating trainer and availability slots: {e}")

def create_admin(username, password, email, fullname, role):
    try:
        cursor.execute(
            sql.SQL("INSERT INTO adminstaff (username, password, email, full_name, role) VALUES (%s, %s, %s, %s, %s)"),
            (username, password, email, fullname, role)
        )
        connection.commit()
        print("Admin created successfully")
    except Error as e:
        connection.rollback() 
        print(f"Error creating admin: {e}")

def member_login():
    while True:
        print("MEMBER LOGIN")
        username = input("Enter your username (type 'exit' to quit): ")
        if username.lower() == 'exit':
            print("Exiting Member login.")
            return 'exit'

        password = input("Enter your password: ")

        try:
            cursor.execute(
                sql.SQL("SELECT * FROM members WHERE username = %s AND password = %s"),
                (username, password)
            )
            member = cursor.fetchone()

            if member:
                return member[0]
            else:
                print("Invalid username or password. Please try again.")

        except Error as e:
            print(f"Error during login: {e}")

def trainer_login():
    while True:
        print("TRAINER LOGIN")
        username = input("Enter your username (type 'exit' to quit): ")
        if username.lower() == 'exit':
            print("Exiting Trainer login.")
            return 'exit'

        password = input("Enter your password: ")

        try:
            cursor.execute(
                sql.SQL("SELECT * FROM trainers WHERE username = %s AND password = %s"),
                (username, password)
            )
            trainer = cursor.fetchone()

            if trainer:
                print("Login successful!")
                return trainer[0]
            else:
                print("Invalid username or password. Please try again.")

        except Error as e:
            print(f"Error during login: {e}")
            return None

def admin_login():
    while True:
        print("ADMIN LOGIN")
        username = input("Enter your username (type 'exit' to quit): ")
        if username.lower() == 'exit':
            print("Exiting Admin login.")
            return 'exit'

        password = input("Enter your password: ")

        try:
            cursor.execute(
                sql.SQL("SELECT * FROM adminstaff WHERE username = %s AND password = %s"),
                (username, password)
            )
            admin = cursor.fetchone()

            if admin:
                print("Login successful!")
                return admin[0]
            else:
                print("Invalid username or password. Please try again.")

        except Error as e:
            print(f"Error during login: {e}")
            return None
