from login import *
from menu import *
from memFunc import *


def main():
    print("Welcome to Health and Fitness Management Club!")
    print("Would you like to login as: ")
    print("1. Member")
    print("2. Trainer")
    print("3. Admin")
    print("4. Create an account")

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
        print("Invalid choice. Please try again.")

    if role == 'member':
        member_id = member_login()
        if member_id != 0:
            choice = member_menu()
            if choice == '1':
                result = update_member(member_id)
            elif choice == '2':
                result = update_fitness_goal()
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
                print("Invalid choice. Please try again.")

    elif role == 'trainer':
        choice = trainer_menu()
    elif role == 'admin':
        choice = admin_menu()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()