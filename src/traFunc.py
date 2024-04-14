import psycopg2
from psycopg2 import sql
from psycopg2 import Error
from datetime import timedelta

from login import *

def update_trainer(trainer_id, **kwargs):
    try:
        print("\nWhich field do you want to update?")
        print("1. Username")
        print("2. Password")
        print("3. Email")
        print("4. Full Name")
        choice = int(input("Enter the number corresponding to the field you want to update: "))
        
        # Map user choice to column name
        columns = {
            1: "username",
            2: "password",
            3: "email",
            4: "full_name",
        }
        
        # Validate user choice
        if choice not in columns:
            print("Invalid choice!")
            return
        
        column_name = columns[choice]
        new_value = input(f"Enter the new value for {column_name}: ")
        
        query = f"UPDATE members SET {column_name} = %s WHERE member_id = %s"
        
        cursor.execute(query, (new_value, trainer_id))
        connection.commit()
        
        print("Update successful")   
    except Error as e:
        print(f"Error updating member: {e}")
        connection.rollback()

def update_availability(trainer_id):
    try:
        while True:
            print_availability(trainer_id)
            print("1. Add new availability slot")
            print("2. Update existing availability slot")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                day_of_week = input("Enter the day of the week (e.g., Monday): ")
                start_time = input("Enter the start time (HH:MM): ")
                end_time = input("Enter the end time (HH:MM): ")

                cursor.execute(
                    sql.SQL("SELECT COUNT(*) FROM AvailabilitySlots WHERE trainer_id = %s AND day_of_week = %s AND NOT (start_time >= %s OR end_time <= %s)"),
                    (trainer_id, day_of_week, end_time, start_time)
                )
                conflict_count = cursor.fetchone()[0]

                if conflict_count == 0:
                    try:
                        cursor.execute(
                            sql.SQL("INSERT INTO AvailabilitySlots (trainer_id, day_of_week, start_time, end_time) VALUES (%s, %s, %s, %s)"),
                            (trainer_id, day_of_week, start_time, end_time)
                        )
                        connection.commit()
                        print("New availability slot added successfully.")
                    except Error as e:
                        connection.rollback()
                        print(f"Error adding availability slot: {e}")
                else:
                    print("Conflict detected with existing availability slots. Please choose a different time.")


            elif choice == '2':
                slot_id = input("Enter the ID of the availability slot you want to update: ")
                day_of_week = input("Enter the new day of the week (e.g., Monday): ")
                start_time = input("Enter the new start time (HH:MM): ")
                end_time = input("Enter the new end time (HH:MM): ")

                # Check for conflicts with existing availability slots
                cursor.execute(
                    sql.SQL("SELECT COUNT(*) FROM AvailabilitySlots WHERE trainer_id = %s AND day_of_week = %s AND NOT (start_time >= %s OR end_time <= %s) AND slot_id != %s"),
                    (trainer_id, day_of_week, end_time, start_time, slot_id)
                )
                conflict_count = cursor.fetchone()[0]

                if conflict_count == 0:
                    try:
                        cursor.execute(
                            sql.SQL("UPDATE AvailabilitySlots SET day_of_week = %s, start_time = %s, end_time = %s WHERE slot_id = %s AND trainer_id = %s"),
                            (day_of_week, start_time, end_time, slot_id, trainer_id)
                        )
                        connection.commit()
                        print("Availability slot updated successfully.")
                    except Error as e:
                        connection.rollback()
                        print(f"Error updating availability slot: {e}")
                else:
                    print("Conflict detected with existing availability slots. Please choose a different time.")


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

def print_availability(trainer_id):
    try:
        cursor.execute(
            sql.SQL("SELECT * FROM AvailabilitySlots WHERE trainer_id = %s"),
            (trainer_id,)
        )
        availability_slots = cursor.fetchall()

        if availability_slots:
            print("Availability slots for the trainer:")
            for slot in availability_slots:
                print(f"Slot ID: {slot[0]}, Day of the Week: {slot[2]}, Start Time: {slot[3]}, End Time: {slot[4]}")
        else:
            print("No availability slots found for the trainer.")

    except Error as e:
        print(f"Error printing availability: {e}")

def is_trainer_available(trainer_id, day_of_week, start_time, end_time):
    try:
        cursor.execute(
            """
            SELECT COUNT(*) FROM AvailabilitySlots
            WHERE trainer_id = %s 
            AND day_of_week = %s
            AND start_time <= %s AND end_time >= %s
            AND start_time <= %s AND end_time >= %s
            """,
            (trainer_id, day_of_week, end_time, start_time, start_time, end_time)
        )
        count = cursor.fetchone()[0]

        return count > 0 

    except Error as e:
        print(f"Database error: {e}")
        return False

def trainer_exists(trainer_id):
    try:
        cursor.execute(
            "SELECT COUNT(*) FROM Trainers WHERE trainer_id = %s",
            (trainer_id,)
        )
        count = cursor.fetchone()[0]

        return count > 0

    except Error as e:
        print(f"Database error: {e}")
        return False