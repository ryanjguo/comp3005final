import psycopg2
from psycopg2 import sql
from psycopg2 import Error

from login import *

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
            "SELECT * FROM exerciseroutines WHERE member_id = %s",
            (member_id,)
        )
        routines = cursor.fetchall()
        
        if not(routines):
            print("No exercise routines found.")
        else:
            print("\nExercise Routines:")
            for routine in routines:
                print(routine)
        
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
        print(f"Weight: Min - {min_weight}, Max - {max_weight}, Avg - {avg_weight}")
        print(f"Steps: Min - {min_steps}, Max - {max_steps}, Avg - {avg_steps}")
        print(f"Calories: Min - {min_calories}, Max - {max_calories}, Avg - {avg_calories}")
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
