from login import *

def main():
    print("Welcome to Health and Fitness Management Club!")
    print("Would you like to login as: ")
    print("1. Member")
    print("2. Trainer")
    print("3. Admin")
    print("4. Create an account")

    choice = input("Enter your choice: ")

    if choice == '1':
        role = member_login()
    elif choice == '2':
        role = trainer_login()
    elif choice == '3':
        role = admin_login()
    elif choice == '4':
        role = create_account()
    else:
        print("Invalid choice. Please try again.")

    if role == 'member':
        choice = member_menu()
    elif role == 'trainer':
        choice = trainer_menu()
    elif role == 'admin':
        choice = admin_menu()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()