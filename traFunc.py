import psycopg2
from psycopg2 import sql
from psycopg2 import Error

from login import *

def update_trainer(trainer_id, **kwargs):
    return

def update_availability(trainer_id):
    try:
        # First, fetch the current availability slots for the given trainer
        cursor.execute(
            sql.SQL("SELECT * FROM AvailabilitySlots WHERE trainer_id = %s"),
            (trainer_id,)
        )
        availability_slots = cursor.fetchall()

        if availability_slots:
            print("Current availability slots for the trainer:")
            for slot in availability_slots:
                print(f"Slot ID: {slot[0]}, Day of the Week: {slot[2]}, Start Time: {slot[3]}, End Time: {slot[4]}")
        else:
            print("No availability slots found for the trainer.")

        # Prompt the user to update or add new availability slots
        while True:
            print("1. Add new availability slot")
            print("2. Update existing availability slot")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                day_of_week = input("Enter the day of the week (e.g., Monday): ")
                start_time = input("Enter the start time (HH:MM): ")
                end_time = input("Enter the end time (HH:MM): ")

                # Insert the new availability slot into the database
                cursor.execute(
                    sql.SQL("INSERT INTO AvailabilitySlots (trainer_id, day_of_week, start_time, end_time) VALUES (%s, %s, %s, %s)"),
                    (trainer_id, day_of_week, start_time, end_time)
                )
                print("New availability slot added successfully.")

            elif choice == '2':
                slot_id = input("Enter the ID of the availability slot you want to update: ")
                day_of_week = input("Enter the new day of the week (e.g., Monday): ")
                start_time = input("Enter the new start time (HH:MM): ")
                end_time = input("Enter the new end time (HH:MM): ")

                # Update the existing availability slot in the database
                cursor.execute(
                    sql.SQL("UPDATE AvailabilitySlots SET day_of_week = %s, start_time = %s, end_time = %s WHERE slot_id = %s AND trainer_id = %s"),
                    (day_of_week, start_time, end_time, slot_id, trainer_id)
                )
                print("Availability slot updated successfully.")

            elif choice == '3':
                print("Exiting availability slot update.")
                break

            else:
                print("Invalid choice. Please try again.")

        connection.commit() 

    except Error as e:
        connection.rollback() 
        print(f"Error updating availability: {e}")


def view_member(full_name):
    try:
        cursor.execute(
            sql.SQL("SELECT * FROM members WHERE full_name = %s"),
            (full_name,)
        )
        member = cursor.fetchone()

        if member:
            print("Member found:")
            print(f"Member ID: {member[0]}")
            print(f"Username: {member[1]}")
            print(f"Email: {member[3]}")
            print(f"Full Name: {member[4]}")
            print(f"Date of Birth: {member[5]}")
            print(f"Gender: {member[6]}")
            print(f"Fitness Goal: {member[7]}")
        else:
            print("Member not found.")

    except Error as e:
        print(f"Error viewing member: {e}")
