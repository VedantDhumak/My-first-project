import random
user_choice=int(input("Enter your choice Type-0 for Rock,Type-1 for Paper,Type-2 for Sicssors "))
if user_choice>=3 or user_choice<0:
    print("The number entered is invalid try again")
else:    
    computer_choice=random.randint(0,2)
    print(user_choice)
    print("Computer choice is :")
    print(computer_choice)
    if user_choice==computer_choice:
         print("Its a draw")
    elif user_choice==2 and computer_choice==0:
         print("Sorry you lose")    
    elif user_choice>computer_choice:   
         print("Congrats you won")
    elif user_choice==0 and computer_choice==2:
         print("Congrats you won")    
    elif computer_choice>user_choice:
         print("Sorry you lose")
