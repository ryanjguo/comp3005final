import psycopg2
from psycopg2 import sql
from psycopg2 import Error

DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_PORT = ""

try:
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = connection.cursor()
    print("Connected to the database successfully!")
except Error as e:
    print(f"Error while connecting to PostgreSQL: {e}")
    exit()

# Account creation
def create_account():
    print("You chose to create a new account.")
    choice = input("What kind of account would you like to create? (Member/Trainer/Admin): ")

    if choice.lower() == 'member':
        username = input("Choose your account name: ")
        password = input("Choose your password: ")
        email = input("Enter your email: ")
        fullname = input("Enter your full name: ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        gender = input("Enter your gender: ")
        fitness_goal = input("Enter your fitness goal: ")

        create_member(username, password, email, fullname, dob, gender, fitness_goal)

    elif choice.lower() == 'trainer':
        username = input("Choose your account name: ")
        password = input("Choose your password: ")
        email = input("Enter your email: ")
        fullname = input("Enter your full name: ")
        expertise = input("Enter your expertise: ")

        create_trainer(username, password, email, fullname, expertise)

    elif choice.lower() == 'admin':

        username = input("Choose your account name: ")
        password = input("Choose your password: ")
        email = input("Enter your email: ")
        fullname = input("Enter your full name: ")
        role = input("Enter your role: ")

        create_admin(username, password, email, fullname, role)

    else:
        print("Invalid choice. Please try again.")
    
    return

def create_member(username, password, email, fullname, dob, gender, fitness_goal):
    connectDb()
    try:
        cursor.execute(
            sql.SQL("INSERT INTO members (username, password, email, fullname, dob, gender, fitness_goal) VALUES (%s, %s, %s, %s, %s, %s, %s)"),
            (username, password, email, fullname, dob, gender, fitness_goal)
        )

def create_trainer():
    pass

def create_admin():
    pass

# Login options
def member_login():
    print("You chose option 1")

def trainer_login():
    print("You chose option 2")

def admin_login():
    print("You chose option 3")


# Menu options
def member_menu():
    pass

def trainer_menu():
    pass

def admin_menu():
    pass