import psycopg2
from psycopg2 import sql
from psycopg2 import Error
import math
from datetime import datetime
from login import *
from traFunc import trainer_exists
from admFunc import display_classes

def update_member(member_id, **kwargs):
    # Prompt user to select the field to update
    try:
        print("\nWhich field do you want to update?")
        print("1. Username")
        print("2. Password")
        print("3. Email")
        print("4. Full Name")
        print("5. Date of Birth")
        print("6. Gender")
        choice = int(input("Enter the number corresponding to the field you want to update: "))
        
        # Map user choice to column name
        columns = {
            1: "username",
            2: "password",
            3: "email",
            4: "full_name",
            5: "date_of_birth",
            6: "gender"
        }
        
        # Validate user choice
        if choice not in columns:
            print("Invalid choice!")
            return
        
        column_name = columns[choice]
        new_value = input(f"Enter the new value for {column_name}: ")
        
        query = f"UPDATE members SET {column_name} = %s WHERE member_id = %s"
        
        cursor.execute(query, (new_value, member_id))
        connection.commit()
        
        print("Update successful")
        
    except Error as e:
        print(f"Error updating member: {e}")
        connection.rollback()

def update_fitness_goal(member_id):
    try:
        cursor.execute(
            "SELECT * FROM fitnessgoals WHERE member_id = %s",
            (member_id,)
        )
        goal_row = cursor.fetchone()
        if goal_row is None:
            # No goal found, insert new fitness goal
            print("\nYou have not set a goal yet.")
            new_goal_name = input("Goal Name: ")
            new_target_weight = input("Target Weight (KG): ")
            new_target_time = input("Target Time (weeks): ")
            cursor.execute(
                "INSERT INTO fitnessgoals (member_id, goal_name, target_weight, target_time) VALUES (%s, %s, %s, %s)",
                (member_id, new_goal_name, new_target_weight, new_target_time)
            )
        else:
            goal = goal_row[2]
            print(f"Current goal: {goal}")
            new_goal_name = input("New Goal Name: ")
            new_target_weight = input("New Target Weight (KG): ")
            new_target_time = input("New Target Time (weeks): ")
            # Update existing fitness goal
            cursor.execute(
                "UPDATE fitnessgoals SET goal_name = %s, target_weight = %s, target_time = %s WHERE member_id = %s",
                (new_goal_name, new_target_weight, new_target_time, member_id)
            )
        
        # Commit the transaction
        connection.commit()
        
        print("Update successful")
        
    except Error as e:
        print(f"Error updating fitness goal: {e}")
        connection.rollback()

def update_health_metrics(member_id):
    try:
        print("\nWhich health metric do you want to update?")
        print("1. Weight (KG)")
        print("2. Height (CM)")
        choice = int(input("Enter the number corresponding to the health metric you want to update: "))
        
        columns = {
            1: "weight",
            2: "height"
        }
        
        if choice not in columns:
            print("Invalid choice!")
            return
        
        column_name = columns[choice]
        new_value = input(f"Enter the new value for {column_name}: ")
        
        query_select = "SELECT * FROM healthmetrics WHERE member_id = %s"
        cursor.execute(query_select, (member_id,))
        existing_metric = cursor.fetchone()
        
        if not existing_metric:
            # No health metrics exist for this user yet, create new ones
            print("\nNo health metrics found for this user. Creating new ones.")
            cursor.execute(
                "INSERT INTO healthmetrics (member_id, metric_date, weight, height) VALUES (%s, CURRENT_DATE, NULL, NULL)",
                (member_id,)
            )
            connection.commit()
        
        # Update the selected health metric
        query_update = f"UPDATE healthmetrics SET {column_name} = %s WHERE member_id = %s"
        cursor.execute(query_update, (new_value, member_id))
        connection.commit()
        
        print("Update successful")
        
    except Error as e:
        print(f"Error updating health metrics: {e}")
        connection.rollback()

def view_exercise_routines(member_id):
    try:
        cursor.execute(
            "SELECT class_name, exercise_routine FROM Classes WHERE trainer_id = %s",
            (member_id,)
        )
        routines = cursor.fetchall()
        
        if not routines:
            print("No exercise routines found.")
        else:
            print("\nExercise Routines:")
            for class_name, exercise_routine in routines:
                print(f"Class: {class_name}, Exercise Routine: {exercise_routine}")
        
    except Error as e:
        print(f"Error viewing exercise routines: {e}")

def view_fitness_achievements(member_id):
    try:
        min_weight = 0
        max_weight = 0
        avg_weight = 0
        min_steps = 0
        max_steps = 0
        avg_steps = 0
        min_calories = 0
        max_calories = 0
        avg_calories = 0

        cursor.execute(
            "SELECT min(weight) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        min_weight = cursor.fetchone()[0]

        cursor.execute(
            "SELECT max(weight) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        max_weight = cursor.fetchone()[0]

        cursor.execute(
            "SELECT avg(weight) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        avg_weight = cursor.fetchone()[0]

        cursor.execute(
            "SELECT min(steps) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        min_steps = cursor.fetchone()[0]

        cursor.execute(
            "SELECT max(steps) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        max_steps = cursor.fetchone()[0]

        cursor.execute(
            "SELECT avg(steps) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        avg_steps = cursor.fetchone()[0]

        cursor.execute(
            "SELECT min(calories) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        min_calories = cursor.fetchone()[0]

        cursor.execute(
            "SELECT max(calories) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        max_calories = cursor.fetchone()[0]

        cursor.execute(
            "SELECT avg(calories) FROM healthmetrics WHERE member_id = %s ",
            (member_id,)
        )
        avg_calories = cursor.fetchone()[0]

        print("\nFitness Achievements and Statistics:")
        print(f"Weight: Min - {min_weight}, Max - {max_weight}, Avg - {math.floor(avg_weight)}")
        print(f"Steps: Min - {min_steps}, Max - {max_steps}, Avg - {math.floor(avg_steps)}")
        print(f"Calories: Min - {min_calories}, Max - {max_calories}, Avg - {math.floor(avg_calories)}")
    except Error as e:
        print(f"Error viewing fitness achievements and statistics: {e}")


def log_daily_stats(member_id):
    try:
        weight = input("Enter your weight (KG): ")
        steps = input("Enter the number of steps taken: ")
        calories = input("Enter the number of calories consumed: ")
        date = input("Enter the date (YYYY-MM-DD): ")

        cursor.execute(
            "INSERT INTO healthmetrics (member_id, weight, steps, calories, metric_date) VALUES (%s, %s, %s, %s, %s)",
            (member_id, weight, steps, calories, date)
        )
        connection.commit()
        
        print("Daily stats logged successfully.")
        
    except Error as e:
        print(f"Error logging daily stats: {e}")
        connection.rollback()

def pay_bill(member_id):
    try:
        cursor.execute(
            "SELECT balance FROM members WHERE member_id = %s",
            (member_id,)
        )

        balance = cursor.fetchone()[0]

        if balance <= 0:
            print("No outstanding balance.")
            return
        else:
            print(f"Outstanding balance: {balance}")
            pay = input("Would you like to pay your balance? (y/n): ")

            if pay.lower() == 'y':
                cursor.execute(
                    "UPDATE members SET balance = 0 WHERE member_id = %s",
                    (member_id,)
                )
                connection.commit()
                print("Payment successful.")
            else:
                print("Payment cancelled.")

            return
        
    except Error as e:
        print(f"Error paying bill: {e}")
        connection.rollback()

def book_fitness_session(member_id):
    trainer_id = input("Enter the ID of the trainer you would like to book with: ")
    if not trainer_exists(trainer_id):
        print("Trainer with ID " + str(trainer_id) + " does not exist")
        return

    try:
        cursor.execute(
            """
            SELECT day_of_week, start_time, end_time 
            FROM AvailabilitySlots 
            WHERE trainer_id = %s
            """,
            (trainer_id,)
        )
        availability_slots = cursor.fetchall()

        cursor.execute(
            """
            SELECT day_of_week, start_time, end_time 
            FROM Classes 
            WHERE trainer_id = %s
            """,
            (trainer_id,)
        )
        class_slots = cursor.fetchall()

        cursor.execute(
            """
            SELECT day_of_week, start_time, end_time 
            FROM PersonalFitnessSessions 
            WHERE trainer_id = %s
            """,
            (trainer_id,)
        )
        personal_slots = cursor.fetchall()

        merged_slots = availability_slots + class_slots + personal_slots

        print("Available Times for Trainer:")
        availability = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

        for day, start_time, end_time in merged_slots:
            slot_range = (start_time, end_time)
            if slot_range not in availability[day]:
                availability[day].append(slot_range)

        for day, slots in availability.items():
            print(day + ":")
            if not slots:
                print("No available slots")
            else:
                available_slots = []
                for slot in slots:
                    if not available_slots:
                        available_slots.append(slot)
                    else:
                        for available_slot in available_slots[:]:
                            if slot[0] < available_slot[1] and slot[1] > available_slot[0]:
                                available_slots.remove(available_slot)
                                if available_slot[0] < slot[0]:
                                    available_slots.append((available_slot[0], slot[0]))
                                if available_slot[1] > slot[1]:
                                    available_slots.append((slot[1], available_slot[1]))
                            else:
                                available_slots.append(slot)

                for start_time, end_time in available_slots:
                    print(f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}")

        day = input("Enter the day of the week you would like your session: ").strip()
        start_time = input("What time do you want to start your fitness session (HH:MM AM/PM): ").strip()
        end_time = input("What time do you want to end your fitness session (HH:MM AM/PM): ").strip()
        
        # Convert input time strings to time objects
        start_time_obj = datetime.strptime(start_time, '%I:%M %p').time()
        end_time_obj = datetime.strptime(end_time, '%I:%M %p').time()

        slots = availability[day]
        for slot_start_time, slot_end_time in slots[1:]:
            if start_time_obj >= slot_start_time and end_time_obj <= slot_end_time:
                print("The selected time conflicts with an existing booking. Please choose another time.")
                return
            else:
                continue

        duration_hours = (end_time_obj.hour - start_time_obj.hour) + (end_time_obj.minute - start_time_obj.minute) / 60
        # $15 an hour
        price = (duration_hours * 15)
        cursor.execute("UPDATE Members SET balance = balance + %s WHERE member_id = %s", (price, member_id))

        # If no conflicts, book the session
        cursor.execute(
            """
            INSERT INTO PersonalFitnessSessions (member_id, trainer_id, day_of_week, start_time, end_time)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (member_id, trainer_id, day, start_time_obj, end_time_obj)
        )
        connection.commit()
        
        print("Session booked successfully!")
        print("You have been scheduled in:")
        print("Day: " + day)
        print("Start Time: " + start_time)
        print("End Time: " + end_time)
        
    except Error as e:
        print(f"Database error: {e}")

def cancel_personal_fitness_session(member_id):
    try:
        cursor.execute(
            """
            SELECT session_id, trainer_id, day_of_week, start_time, end_time
            FROM PersonalFitnessSessions
            WHERE member_id = %s
            """,
            (member_id,)
        )
        sessions = cursor.fetchall()

        if sessions:
            print("Your booked sessions:")
            for session_id, trainer_id, day_of_week, start_time, end_time in sessions:
                print(f"Session ID: {session_id}, Trainer ID: {trainer_id}, Day: {day_of_week}, Start Time: {start_time}, End Time: {end_time}")

            session_to_cancel = input("Enter the ID of the session you want to cancel: ")

            for session_id, _, _, _, _ in sessions:
                if session_to_cancel == str(session_id):
                    cursor.execute(
                        """
                        DELETE FROM PersonalFitnessSessions
                        WHERE session_id = %s
                        """,
                        (session_to_cancel,)
                    )
                    connection.commit()
                    
                    print("Session cancellation successful!")
                    return True

            print("Invalid session ID. Please enter a valid session ID.")
        else:
            print("You don't have any booked sessions.")

    except Error as e:
        print(f"Database error: {e}")

def sign_up(member_id):
    try:
        display_classes()

        class_id = input("Enter the ID of the class you want to sign up for: ")

        cursor.execute(
            "SELECT capacity, price FROM Classes WHERE class_id = %s",
            (class_id,)
        )
        class_data = cursor.fetchone()
        capacity = class_data[0]
        price = class_data[1]

        if capacity > 0:
            cursor.execute(
                "INSERT INTO ClassMembers (class_id, member_id) VALUES (%s, %s)",
                (class_id, member_id)
            )
            connection.commit()

            cursor.execute(
                "UPDATE Classes SET capacity = capacity - 1 WHERE class_id = %s",
                (class_id,)
            )
            connection.commit()

            cursor.execute(
                "UPDATE Members SET balance = balance + %s WHERE member_id = %s",
                (price, member_id)
            )
            connection.commit()

            print("You have successfully signed up for the class!")
        else:
            print("Sorry, there are no available slots for this class.")

    except Error as e:
        connection.rollback()
        print(f"Error signing up for the class: {e}")

def cancel_class(member_id):
    view_classes(member_id)
    try:
        cursor.execute(
            "SELECT class_id FROM ClassMembers WHERE member_id = %s",
            (member_id,)
        )
        class_ids = cursor.fetchall()

        if class_ids:
            class_id_to_cancel = input("Enter the ID of the class you want to cancel: ")

            if (class_id_to_cancel,) in class_ids:
                cursor.execute(
                    "DELETE FROM ClassMembers WHERE member_id = %s AND class_id = %s",
                    (member_id, class_id_to_cancel)
                )
                connection.commit()

                cursor.execute(
                    "UPDATE Classes SET capacity = capacity + 1 WHERE class_id = %s",
                    (class_id_to_cancel,)
                )
                connection.commit()

                cursor.execute(
                    "SELECT price FROM Classes WHERE class_id = %s",
                    (class_id_to_cancel,)
                )
                price = cursor.fetchone()[0]

                cursor.execute(
                    "UPDATE Members SET balance = balance - %s WHERE member_id = %s",
                    (price, member_id)
                )
                connection.commit()

                print("Class cancellation successful!")
            else:
                print("You are not signed up for this class.")
        else:
            print("You are not signed up for any classes.")

    except Error as e:
        connection.rollback()
        print(f"Error canceling class: {e}")


def view_classes(member_id):
    try:
        # Query to fetch classes for the given member
        cursor.execute(
            """
            SELECT c.class_id, c.class_name, c.trainer_id, c.room_id, c.day_of_week, c.start_time, c.end_time
            FROM Classes c
            JOIN ClassMembers cm ON c.class_id = cm.class_id
            WHERE cm.member_id = %s
            """,
            (member_id,)
        )
        classes = cursor.fetchall()

        if not classes:
            print("No classes found for this member.")
        else:
            print("Classes for Member:")
            print("-------------------------------------------------------------------------------------------")
            print("| Class ID | Class Name               | Trainer ID | Room ID | Day        | Time             |")
            print("-------------------------------------------------------------------------------------------")
            for class_info in classes:
                class_id, class_name, trainer_id, room_id, day_of_week, start_time, end_time = class_info
                print(f"| {class_id:<9} | {class_name:<25} | {trainer_id:<10} | {room_id:<8} | {day_of_week:<10} | {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')} |")
            print("-------------------------------------------------------------------------------------------")
    except Error as e:
        print(f"Error displaying classes: {e}")

def view_personal_fitness_sessions(member_id):
    try:
        cursor.execute(
            """
            SELECT pfs.session_id, pfs.trainer_id, pfs.day_of_week, pfs.start_time, pfs.end_time
            FROM personalfitnesssessions pfs
            WHERE pfs.member_id = %s
            """,
            (member_id,)
        )
        sessions = cursor.fetchall()

        if not sessions:
            print("No personal fitness sessions found for this member.")
        else:
            print("Personal Fitness Sessions for Member:")
            print("-------------------------------------------------------------------------------------------")
            print("| Session ID | Trainer ID | Day        | Time             |")
            print("-------------------------------------------------------------------------------------------")
            for session_info in sessions:
                session_id, trainer_id, day_of_week, start_time, end_time = session_info
                print(f"| {session_id:<11} | {trainer_id:<11} | {day_of_week:<10} | {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')} |")
            print("-------------------------------------------------------------------------------------------")
    except Error as e:
        print(f"Error displaying personal fitness sessions: {e}")

def reschedule_personal_fitness_session(member_id):
    if cancel_personal_fitness_session(member_id):
        book_fitness_session(member_id)