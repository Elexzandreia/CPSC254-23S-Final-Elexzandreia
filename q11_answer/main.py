from user import *

def main():

    print("AD: Hello! This is a paid advertisment from a nearby restaurant")
    username = input("Please enter your username: ")
    password = input("please enter your password: ")
    
    new_user = User(username, password)
    user_choice = '0'
    
    while(user_choice != '4'):
        print ("option 1: view balance")
        print ("option 2: make deposit")
        print ("option 3: make withdrawal")
        print ("option 4: exit")
        user_choice = input("Please choose your selection: ")
        if user_choice == '1':
            new_user.check_balance()
        elif(user_choice == '2'):
            new_user.deposit()
        elif(user_choice =='3'):
            new_user.withdrawal()
        elif(user_choice == '4'):
            print("Goodbye")
            exit

main()
