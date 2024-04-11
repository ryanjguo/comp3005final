from login import *
from menu import *
from memFunc import *
from traFunc import *
from admFunc import *

banner = """
 _______  ___   _______    _______  ______    _______  _______  __   __  _______  ______    _______ 
|  _    ||   | |       |  |  _    ||    _ |  |       ||       ||  | |  ||       ||    _ |  |       |
| |_|   ||   | |    ___|  | |_|   ||   | ||  |   _   ||_     _||  |_|  ||    ___||   | ||  |  _____|
|       ||   | |   | __   |       ||   |_||_ |  | |  |  |   |  |       ||   |___ |   |_||_ | |_____ 
|  _   | |   | |   ||  |  |  _   | |    __  ||  |_|  |  |   |  |       ||    ___||    __  ||_____  |
| |_|   ||   | |   |_| |  | |_|   ||   |  | ||       |  |   |  |   _   ||   |___ |   |  | | _____| |
|_______||___| |_______|  |_______||___|  |_||_______|  |___|  |__| |__||_______||___|  |_||_______|
 _______  __   __  __   __                                                                          
|       ||  | |  ||  |_|  |                                                                         
|    ___||  |_|  ||       |                                                                         
|   | __ |       ||       |                                                                         
|   ||  ||_     _||       |                                                                         
|   |_| |  |   |  | ||_|| |                                                                         
|_______|  |___|  |_|   |_|                                                                                                                                    
"""

def main():
    print(banner)

    while True:
        choice = 0
        print("Would you like to login as: ")
        print("1. Member")
        print("2. Trainer")
        print("3. Admin")
        print("4. Create an account")
        print("5. Exit\n")

        choice = input("Enter your choice: ")

        options = ['1', '2', '3', '4', '5', 'member', 'trainer', 'admin', 'create an account', 'exit']

        #input validation
        while choice not in options:
            print("Invalid choice. Please try again.\n")
            choice = input("Enter your choice (#): ").lower()
            print(choice)

        if choice == '1' or choice == 'member':
            role = 'member'
        elif choice == '2' or choice == 'trainer':
            role = 'trainer'
        elif choice == '3' or choice == 'admin':
            role = 'admin'
        elif choice == '4' or choice == 'create an account':
            role = create_account()
            if role == 'exit':
                break
        elif choice == '5' or choice == 'exit':
            break
            
        if role == 'member':
            member_id = member_login()
            if member_id == 'exit':
                continue
            if member_id != 0:
                while choice != '9':
                    choice = member_menu()
                    if choice == '1':
                        result = update_member(member_id)
                    elif choice == '2':
                        result = update_fitness_goal(member_id)
                    elif choice == '3':
                        result = update_health_metrics(member_id)
                    elif choice == '4':
                        result = view_exercise_routines(member_id)
                    elif choice == '5':
                        result = view_fitness_achievements(member_id)
                    elif choice == '6':
                        result = log_daily_stats(member_id)
                    elif choice == '7':
                        result = manage_schedule(member_id)
                    elif choice == '8':
                        result = pay_bill(member_id)
                    else:
                        print("Invalid choice. Please try again.\n")

        elif role == 'trainer':
            trainer_id = trainer_login()
            if trainer_id == 'exit':
                break
            if trainer_id != 0:
                choice = trainer_menu()
                if choice == '1':
                    result = update_trainer(trainer_id)
                elif choice == '2':
                    result = update_availability(trainer_id)
                elif choice == '3':
                    member_name = input("Enter the name of the member you would like to see: ")
                    result = view_member(member_name)

        elif role == 'admin':
            admin_id = admin_login()
            if admin_id == 'exit':
                break
            if admin_login != 0:
                choice = admin_menu()
                if choice == '1':
                    result = room_management_menu()
                    if result == '1':
                        result = display_rooms_and_bookings()
                    elif result == '2':
                        result = equipment_monitor()
                    elif result == '3':
                        result = class_scheduling()
                elif choice == '2':
                    result = equipment_monitor()
                elif choice == '3':
                    result = class_schedule_updating()
                elif choice == '4':
                    result = billing()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()