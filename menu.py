import psycopg2
from psycopg2 import sql
from psycopg2 import Error

# Menu options
def member_menu():
    print("Welcome to the member menu.")

    print("1. Update personal info")
    print("2. Update fitness goals")
    print("3. Update health metrics")

    print("4. View exercise routines")
    print("5. View fitness achievements")
    print("6. View health statistics")

    print("7. Manage schedule")

    choice = input("Enter your choice (#): ")

    return choice

def trainer_menu():
    print("Welcome to the trainer menu.")

    print("1. Update personal info")
    print("2. Update availability slots")
    print("3. View client profile")

def admin_menu():
    pass