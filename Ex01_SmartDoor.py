#Default password is =  khul ja sim sim
import time

# This function is for text slicing
def txtFilter(txt:str) ->str:    
    """In case if you use accidentally one or more space in text it will filter it
        And will return a No SPACE text. Example : "Hello sourav" --> "hellosourav"  """

    fineTxt = "" 
    filtered = txt.split()  # splitted text will store here as LIST type

    for x in filtered :
        fineTxt = fineTxt + x

    return fineTxt

    
# Function to verify password
def userEntry (password:str) -> bool:
    """It will take a default password. 
       Then run the function and enter password to open the door.
       Returns Boolean --> True or False"""

    intro = "***** Smart Door *****"
    print(intro.center(100))            # decorating intro (ignore it)

    maxTry = 1
    flt_password = txtFilter(password)  # Additional feature: filtering the Default password
                                        # If i don't want the "flt_password" variable then -
                                        # i had to set the "password" variable with No Space Text
    while (maxTry <= 3):
        print(f"You have {4 - maxTry} chance to enter correct password")        
        pwd = input("Please enter password :\n>>> ").lower()  # Taking password from User
        flt_pwd = txtFilter(pwd)        #Additional feature: filtering the User password 

        if (pwd == password) or (flt_password == flt_pwd) :            
            print("Welcome Home Dear")
            return True                  # As i have declared Return so the Loop will BREAK here, No need extra "break" func.

        else :
            maxTry = maxTry + 1          # incrementing maxtry

            if maxTry > 3 :                
                print("\nYou have lost all chances")  # will print it, if maximum chance exceeds
                return False
            else:
                print("\nWrong password, Try again.")  # will print on every wrong attempts
        





# Program starts here __________________

d_password = "khul ja sim sim"                          #default password for the door

examine = userEntry(d_password)

if examine == False :
    print("\nInitializing Security Question...\n")
    time.sleep(2)                                       # this line is to pause program for 3 sec , just to give a realistic feel

    s_answer = input("What is the Kitchen's wall Color?\n>>> ").lower()     # taking security answer

    if s_answer == "black" :
        print("Congrats ! We recommend you to change the door password. \n")
        d_password = str(input("Set a new password : "))                    # setting up new password

        time.sleep(1)

        print("\nPassword has changed successfully ! Welcome Home \n")

    else :
        print("Please wait. Police are on the way, mr.Robber")

else :     # unnecessary line...
    pass

