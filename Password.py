# Word Problem: The School Portal Login System
# Your school is creating a new online portal for students to sign up for accounts. The login system needs a function that accepts two pieces of information from the user:
# Their email address
# Their password
# Before creating the new account, the function must verify that the email and password follow school rules:
# The email must be a string and must contain an "@" symbol.
# The password must also be a string.
# The password must be at least 8 characters long.
# The password must include at least one number.
# The password must include at least one uppercase letter.
# If ANY of these rules are broken, the function should return an error message explaining what went wrong.
# If EVERYTHING is good, the function should return a dictionary that represents the newly created user.

def signup():

    hasAt = 0
    eInvalid =1
    pInvalid = 1


    print("Welcome to the Study Johnny and William (SJW) organization. Register an account here.")
    print("   ")
    while eInvalid == 1:
        
        email = str(input("Enter your email: "))
        for char in email:
            if char == '@':
                hasAt=+1

        if hasAt == 1:
            print(f"Your email, {email}, is valid.")
            print("   ")
            eInvalid = 0
        else:
            print("Your email did not have an @ symbol.")
            print("   ")



    while pInvalid == 1:
        password = str(input("Enter a password. It must have 8 characters, include a number, amd a capital letter: "))

signup()




#use str. functions




