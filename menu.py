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

    choice = input("Enter your choice (#): ")

    return choice

def trainer_menu():
    print("Welcome to the trainer menu.")

    print("1. Update personal info")
    print("2. Update availability slots")
    print("3. View client profile")
    print("4. Exit")

    choice = input("Enter your choice (#): ")

    return choice

def admin_menu():
    print("Welcome to the admin staff menu.")

    print("1. Room Booking Management")
    print("2. Equipment Maintenance Monitoring")
    print("3. Class Schedule Updating")
    print("4. Billing and Payment Processing")

    choice = input("Enter your choice (#): ")

    return choice

def room_management_menu():
    print("ROOM BOOKING MANAGEMENT")

    print("1. Display rooms and bookings")
    print("2. Book a room")
    print("3. Remove a room booking")

    choice = input("Enter your choice (#): ")

    return choice
