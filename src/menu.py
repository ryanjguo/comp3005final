import psycopg2
from psycopg2 import sql
from psycopg2 import Error

# Menu options
def member_menu():
    print("\nWelcome to the member menu.")

    print("1. Update personal info")
    print("2. Update fitness goals")
    print("3. Update health metrics")

    print("4. View exercise routines")
    print("5. View fitness achievements and statistics")
    print("6. Log daily stats")

    print("7. Manage schedule")
    print("8. Pay bill")
    print("9. Exit")

    choice = input("Enter your choice (#): ")

    return choice

def trainer_menu():
    print()
    print("Welcome to the trainer menu.")

    print("1. Update personal info")
    print("2. Update availability slots")
    print("3. View client profile")
    print("4. Exit")

    choice = input("Enter your choice (#): ")
    
    return choice

def admin_menu():
    print()
    print("Welcome to the admin staff menu.")

    print("1. Room Booking Management")
    print("2. Equipment Maintenance Monitoring")
    print("3. Class Schedule Updating")
    print("4. Billing and Payment Processing")
    print("5. Exit")

    choice = input("Enter your choice (#): ")
    return choice

def room_management_menu():
    print()
    print("ROOM BOOKING MANAGEMENT")

    print("1. Book a class")
    print("2. Remove a class")
    print("3. Display classes")

    choice = input("Enter your choice (#): ")
    return choice

def manage_schedule_menu():
    print()
    print("Welcome to scheduling.")

    print("1. Book a personal fitness session")
    print("2. Sign up for a class")
    print("3. View Classes you are in")
    print("4. Exit")

    choice = input("Enter your choice (#): ")
    return choice