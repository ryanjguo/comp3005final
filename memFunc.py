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
        goal = cursor.fetchone()[2]
        
        
        if not(goal):
            # Insert new fitness goal
            print("\nYou have not set a goal yet.")
            new_goal_name = input("Goal Name: ")
            new_target_weight = input("Target Weight (KG): ")
            new_target_time = input("Target Time (weeks): ")
            cursor.execute(
                "INSERT INTO fitnessgoals (member_id, goal_name, target_weight, target_time) VALUES (%s, %s, %s, %s)",
                (member_id, new_goal_name, new_target_weight, new_target_time)
            )
        else:
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
        
        query = f"UPDATE healthmetrics SET {column_name} = %s WHERE member_id = %s"
        
        cursor.execute(query, (new_value, member_id))
        connection.commit()
        
        print("Update successful")
        
    except Error as e:
        print(f"Error updating health metrics: {e}")
        connection.rollback()