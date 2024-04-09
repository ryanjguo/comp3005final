from login import *
from menu import *
from memFunc import *
from traFunc import *

banner = """
 _______  __   __  __   __    __   __  _______  __    _  _______  _______  _______  __   __  _______  __    _  _______ 
|       ||  | |  ||  |_|  |  |  |_|  ||   _   ||  |  | ||   _   ||       ||       ||  |_|  ||       ||  |  | ||       |
|    ___||  |_|  ||       |  |       ||  |_|  ||   |_| ||  |_|  ||    ___||    ___||       ||    ___||   |_| ||_     _|
|   | __ |       ||       |  |       ||       ||       ||       ||   | __ |   |___ |       ||   |___ |       |  |   |  
|   ||  ||_     _||       |  |       ||       ||  _    ||       ||   ||  ||    ___||       ||    ___||  _    |  |   |  
|   |_| |  |   |  | ||_|| |  | ||_|| ||   _   || | |   ||   _   ||   |_| ||   |___ | ||_|| ||   |___ | | |   |  |   |  
|_______|  |___|  |_|   |_|  |_|   |_||__| |__||_|  |__||__| |__||_______||_______||_|   |_||_______||_|  |__|  |___|  
 _______  __   __  _______  _______  _______  __   __                                                                  
|       ||  | |  ||       ||       ||       ||  |_|  |                                                                 
|  _____||  |_|  ||  _____||_     _||    ___||       |                                                                 
| |_____ |       || |_____   |   |  |   |___ |       |                                                                 
|_____  ||_     _||_____  |  |   |  |    ___||       |                                                                 
 _____| |  |   |   _____| |  |   |  |   |___ | ||_|| |                                                                 
|_______|  |___|  |_______|  |___|  |_______||_|   |_|                                                                 
"""

def main():
    print(banner)
    print("Would you like to login as: ")
    print("1. Member")
    print("2. Trainer")
    print("3. Admin")
    print("4. Create an account\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        role = 'member'
    elif choice == '2':
        role = 'trainer'
    elif choice == '3':
        role = 'admin'
    elif choice == '4':
        role = create_account()
    else:
        print("Invalid choice. Please try again.\n")

    if role == 'member':
        member_id = member_login()
        if member_id != 0:
            choice = member_menu()
            if choice == '1':
                result = update_member(member_id)
            elif choice == '2':
                result = update_fitness_goal(member_id)
            elif choice == '3':
                result = update_health_metrics()
            elif choice == '4':
                pass
            elif choice == '5':
                pass
            elif choice == '6':
                pass
            elif choice == '7':
                pass
            else:
                print("Invalid choice. Please try again.\n")

    elif role == 'trainer':
        trainer_id = trainer_login()
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
        if admin_login != 0:
            choice = admin_menu()
    else:
        print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()