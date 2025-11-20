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
    letterInvalid = 1

    letters = 0
    hasNumber = 0
    #isdigit??

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
            hasAt=0


    #password

    #letter requirements:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       6767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767667766776677667766776677667766776677667766776677667766776677667766776677667766776677667766776677667766776677667766776677666777666777666777666777666777666777666777666777666777666777666777666777666777666777666777666777666777666677776666777766667777666677776666777766667777
    while letterInvalid == 1:
        password = str(input("Enter a password. It must have 8 characters, include a number, and a capital letter: "))

        for char in password:
            letters = letters + 1


























            
        if letters >= 8: 
            letters = 0
        elif letters < 8:
            
            letterInvalid  = 0
            print("You need to have at least 8 letters.")
            print(" ")
    
    #number:
        
            
            



signup()




#use str. functions




#if type(email) != str