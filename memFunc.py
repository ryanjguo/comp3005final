import psycopg2
from psycopg2 import sql
from psycopg2 import Error

from login import *

def update_member(member_id, **kwargs):
    try:
        query = "UPDATE members SET "
        for key, value in kwargs.items():
            update_query += f"{key} = %s, "
        update_query = update_query[:-2] + " WHERE member_id = %s"

        cursor.execute(update_query, list(kwargs.values()) + [member_id])
        connection.commit()

        print("Update successful")
    except Error as e:
        print(f"Error updating member: {e}")
        connection.rollback()

def update_fitness_goal(member_id, fitness_goal):
    try:
        cursor.execute(
            sql.SQL("UPDATE members SET fitness_goal = %s WHERE member_id = %s"),
            (fitness_goal, member_id)
        )
        connection.commit()

        print("Update successful")
    except Error as e:
        print(f"Error updating fitness goal: {e}")
        connection.rollback()

def update_health_metrics(member_id, **kwargs):
    try:
        query = "UPDATE healthmetrics SET "
        for key, value in kwargs.items():
            update_query += f"{key} = %s, "
        update_query = update_query[:-2] + " WHERE member_id = %s"

        cursor.execute(update_query, list(kwargs.values()) + [member_id])
        connection.commit()

        print("Update successful")
    except Error as e:
        print(f"Error updating health metrics: {e}")
        connection.rollback()




