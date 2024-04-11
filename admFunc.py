import psycopg2
from psycopg2 import sql
from psycopg2 import Error

from datetime import datetime, timedelta
from login import *
from menu import *
from traFunc import *

def display_classes():
    try:
        cursor.execute(
            "SELECT class_id, class_name, trainer_id, room_id, start_time, end_time, capacity FROM Classes"
        )
        classes = cursor.fetchall()

        if not classes:
            print("No classes found.")
        else:
            print("Classes:")
            print("--------------------------------------------------------------------------------------------")
            print("| Class ID | Class Name               | Trainer ID | Room ID | Start Time | End Time | Capacity |")
            print("--------------------------------------------------------------------------------------------")
            for class_info in classes:
                class_id, class_name, trainer_id, room_id, start_time, end_time, capacity = class_info
                print(f"| {class_id:<9} | {class_name:<25} | {trainer_id:<10} | {room_id:<8} | {start_time.strftime('%H:%M %p'):<11} | {end_time.strftime('%H:%M %p'):<9} | {capacity:<8} |")
            print("--------------------------------------------------------------------------------------------")
    except Error as e:
        print(f"Error displaying classes: {e}")

def equipment_monitor():
    try:
        cursor.execute(
            "SELECT * FROM Equipment"
        )
        equipment = cursor.fetchall()

        for item in equipment:
            print(f"Equipment ID: {item[0]}, Name: {item[1]}, Room: {item[2]}, Status: {item[3]}")

        print("1. Update equipment status")
        print("2. Update equipment details")
        print("3. Add new equipment")
        print("4. Remove equipment")
        print("5. Exit")
        choice = input("Enter your choice (#): ")

        if choice == '1':
            equipment_id = input("Enter the equipment ID: ")
            new_status = input("Enter the new status: ")

            cursor.execute(
                "UPDATE Equipment SET maintenance_status = %s WHERE equipment_id = %s",
                (new_status, equipment_id)
            )
            connection.commit()

            print("Update successful")

        elif choice == '2':
            equipment_id = input("Enter the equipment ID: ")
            new_name = input("Enter the new name: ")
            new_room = input("Enter the new room: ")

            cursor.execute(
                "UPDATE Equipment SET equipment_name = %s, room_id = %s WHERE equipment_id = %s",
                (new_name, new_room, equipment_id)
            )
            connection.commit()

            print("Update successful")

        elif choice == '3':
            new_name = input("Enter the new equipment name: ")
            room = input("Enter the room where the equipment is located: ")

            cursor.execute(
                "INSERT INTO Equipment (equipment_name, room_id, maintenance_status) VALUES (%s, %s, 'available')",
                (new_name, room)
            )
            connection.commit()

            print("Equipment added successfully")
        
        elif choice == '4':
            equipment_id = input("Enter the equipment ID: ")

            cursor.execute(
                "DELETE FROM Equipment WHERE equipment_id = %s",
                (equipment_id,)
            )
            connection.commit()

            print("Equipment removed successfully")
        
        elif choice == '5':
            return
    
    except Error as e:
        print(f"Error viewing equipment: {e}")

def make_class():
    display_classes()
    trainer_id = input("Enter the trainer's ID: ")

    print_availability(trainer_id)
    print("\n")
    print_rooms()
    
    room_id = input("\nEnter the room ID to schedule the class: ")

    class_name = input("Enter the class name: ")
    day = input("Enter the day of the week: ")
    start_time_str = input("Enter the class start time (HH:MM AM/PM): ")
    end_time_str = input("Enter the class end time (HH:MM AM/PM): ")

    start_time = datetime.strptime(start_time_str, "%I:%M %p").time()
    end_time = datetime.strptime(end_time_str, "%I:%M %p").time()

    # duration of the class in hours the price will be calculated based on how long the class is
    duration_hours = (end_time.hour - start_time.hour) + (end_time.minute - start_time.minute) / 60
    # $5 per hour per month per year
    price = (duration_hours * 5) * 4 * 12
    print(price)

    if is_trainer_available(trainer_id, day, start_time, end_time) > 0:
        if is_time_slot_available(trainer_id, room_id, day, start_time, end_time):
            capacity = input("Enter the class capacity: ")
            insert_class(class_name, trainer_id, room_id, day, start_time, end_time, capacity, price)
            print("Class scheduled successfully!")
        else:
            print("Sorry, the requested time slot is already booked.")
    else:
        print ("Sorry the trainer is not available at this time choose another time.")

def billing():
    pass

def print_rooms():
    try:
        cursor.execute(
            sql.SQL("SELECT * FROM Rooms")
        )
        rooms = cursor.fetchall()

        if rooms:
            print("Rooms:")
            for room in rooms:
                print(f"Room ID: {room[0]}, Room Name: {room[1]}, Capacity: {room[2]}")
        else:
            print("No rooms found.")

    except Error as e:
        print(f"Error printing rooms: {e}")

def insert_class(class_name, trainer_id, room_id, day, start_time, end_time, capacity, price):
    try:
        cursor.execute(
            "INSERT INTO Classes (class_name, trainer_id, room_id, day_of_week, start_time, end_time, capacity, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (class_name, trainer_id, room_id, day, start_time, end_time, capacity, price)
        )
        connection.commit()
        print("Class scheduled successfully")
    except Error as e:
        connection.rollback()
        print(f"Error scheduling class: {e}")

def is_time_slot_available(trainer_id, room_id, day, start_time, end_time):
    try:
        query = sql.SQL("""
            SELECT COUNT(*) FROM Classes
            WHERE trainer_id = %s AND room_id = %s AND day_of_week = %s
            AND ((start_time <= %s AND end_time >= %s) OR (start_time <= %s AND end_time >= %s))
        """)
        cursor.execute(query, (trainer_id, room_id, day, start_time, start_time, end_time, end_time))
        count = cursor.fetchone()[0]

        return count == 0

    except Error as e:
        print(f"Database error: {e}")
        return False

def remove_class():
    display_classes()
    print('\n')
    print_rooms()

    room_id = input("Enter the room ID: ")
    class_id = input("Enter the class ID: ")
    try:
        cursor.execute(
            sql.SQL("SELECT class_id FROM Classes WHERE room_id = %s AND class_id = %s"),
            (room_id, class_id)
        )
        existing_class = cursor.fetchone()

        if existing_class:
            cursor.execute(
                sql.SQL("DELETE FROM Classes WHERE room_id = %s AND class_id = %s"),
                (room_id, class_id)
            )
            connection.commit()
            print("Booking removed successfully.")
        else:
            print("No booking found in the specified room for the provided class ID.")

    except Error as e:
        connection.rollback()
        print(f"Error removing booking: {e}")

def class_schedule_updating():
    display_classes()

    class_id = input("Enter the class ID to update: ")
    try:
        cursor.execute(
            sql.SQL("SELECT * FROM Classes WHERE class_id = %s"),
            (class_id,)
        )
        existing_class = cursor.fetchone()

        if existing_class:
            class_name = input("Enter the new class name (leave empty to skip): ").strip()
            trainer_id = input("Enter the new trainer ID (leave empty to skip): ").strip()
            room_id = input("Enter the new room ID (leave empty to skip): ").strip()
            start_time = input("Enter the new start time (HH:MM AM/PM) (leave empty to skip): ").strip()
            end_time = input("Enter the new end time (HH:MM AM/PM) (leave empty to skip): ").strip()

            if is_trainer_available(trainer_id, start_time, end_time) > 0:
                capacity = input("Enter the new capacity (leave empty to skip): ").strip()
            else:
                exit

            query = "UPDATE Classes SET"
            params = []

            if class_name is not None:
                query += " class_name = %s,"
                params.append(class_name)
            if trainer_id is not None:
                query += " trainer_id = %s,"
                params.append(trainer_id)
            if room_id is not None:
                query += " room_id = %s,"
                params.append(room_id)
            if start_time is not None:
                query += " start_time = %s,"
                params.append(start_time)
            if end_time is not None:
                query += " end_time = %s,"
                params.append(end_time)
            if capacity is not None:
                query += " capacity = %s,"
                params.append(capacity)

            query = query.rstrip(",") + " WHERE class_id = %s"
            params.append(class_id)
            cursor.execute(sql.SQL(query), params)

            connection.commit()
            print("Class information updated successfully.")
        else:
            print("Class not found with the provided class ID.")

    except Error as e:
        connection.rollback()
        print(f"Error updating class information: {e}")

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

        return count > 0  # If count is greater than 0, trainer is available during the specified time range

    except Error as e:
        print(f"Database error: {e}")
        return False
