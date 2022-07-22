import sys
import random
import time

# Run this program and PLEASE create 2 bank accounts at very first stage. It will help you to test all functions of this program.
# or you can simply download attached "DontDareToOpen.txt" file for better experience  [Optional]


class AccountOpening :
    def __init__(self, name: str, age: str, phone: str, bPin : int= 0, money = 0.00) -> None:
        """This function will take exact details to open an account"""

        self.uName = name
        self.uAge = age
        self.uPhone = phone
        self.uBankPin = bPin
        self.uMoney =  money

        # Random Number is for creating a bank ID, but no guarantee if it is unique or not. However check below -
        randNum = random.randint(1111,99999)
        self.bankId = randNum
        
        # This portion is t
        with open("DontDareToOpen.txt","a+") as AccLog :
            AccLog.seek(0)
            data =  AccLog.readlines()      # Database's all data is now stored in this "data" variable as list of strings
                                            # You may check the .txt file to see how it saved records before
            for x in range(len(data)):
                y = data[x].split("--")     # As one user's all data is saved in one line, therefore we are slicing the line to get specified details about user

                if (self.uPhone) == (y[3]) :  # This line will find if new user has already account in database
                    # raise Exception(f"Sorry you have already an account with this name: {y[1]} and phone number: {y[3]}")
                    sys.exit((f"Sorry you have already an account with this name: {y[1]} and phone number: {y[3]}"))

                else : 
                    # This else portion will provide UNIQUE random number as Bank ID                   
                    if self.bankId == int(y[0]) : 
                        randNum = random.randint(1111,99999)
                        self.bankId = randNum
                        break   
            # Upon successfull filtering proceess of previous lines, the next line will entry data as a new bank user                    
            AccLog.write(f"{self.bankId}--{self.uName}--{self.uAge}--{self.uPhone}--{self.uBankPin}--{self.uMoney}--\n")

        print("Please wait...")
        time.sleep(1)
        print("Account Creation Successfully Done !")



class AccountManage :
    """This function takes your Phone number and Pin no. to verify your account's existense.
    It will return nothing. But there is a variable called " verifyReturn " will give list if your account is exist"""

    AccLog = open("DontDareToOpen.txt","a+")
    AccLog.seek(0)
    data =  AccLog.readlines()      # saved full data line by line in this variable
    AccLog.close()

    def __init__(self, phone_no:str, pin_no:str):
        self.phone = phone_no
        self.pin = pin_no
        self.verifyReturn = ["","","",""]  # Null list

        for x in range(len(self.data)) :
            y = self.data[x].split("--")

            if (self.phone, self.pin) == (y[3], y[4]) :
                print("\nLogin successfull !\n")
                # Filling up null list - it will be used later when an object will call the class
                self.verifyReturn[0] = True             # Boolean verify
                self.verifyReturn[1] = self.data[x]     # saving "session" of the logged-in user
                self.verifyReturn[2] = x                # Storing the Line number where the user's data is located
                self.verifyReturn[3] = float(y[5])      # Money
                                                        # y[5] means user's Cash ammount. (Check .txt file)
            else:
                if x == len(self.data):
                    print("Failed to login !")
                    self.verifyReturn[0] = False


    def addMoney(self, taka) -> float :
        money = taka
        newData = self.verifyReturn[1]             # "session" of the Logged-in user
        x = self.verifyReturn[2]                   # line location of the user's data
        y = newData.split("--")                    # slicing the line logged-in user's line

        sumOfMoney = float(y[5]) + float(money)

        self.data[x] = f"{y[0]}--{y[1]}--{y[2]}--{y[3]}--{y[4]}--{sumOfMoney}--\n"  # Modifying pre exist logged in user's data to add money

        with open("DontDareToOpen.txt","w") as file :
            file.writelines(self.data)

        print("\nMoney has added successfully")
        return (sumOfMoney)



    def sendMoney(self) -> float :
        
        loggedInData = self.verifyReturn[1]    # Logged in user's non updated data --> unnecessary line 
        loggedInDataLocation = self.verifyReturn[2]


        with open("DontDareToOpen.txt","r") as AccLog_new :
            AccLog_new.seek(0)
            tempData = AccLog_new.readlines()       # temporarily took all data in tempData variable

        # Logged in user's Latest updated data -->  (updated after money was added recently)
        newData =  tempData[loggedInDataLocation]      # directly caught the STRING line where logged in user's updated data is located
        list_newData = newData.split("--")
        latestMoney = float(list_newData[5])
        print(f"You have : {latestMoney} taka\n")        
        
        chul = 1
        breakMe = False
        while chul == 1:
            try :
                rec_phone = input("Please enter receiver's phone no. : ")
                taka = float(input("Enter the ammount you want to send : "))

                if taka > latestMoney :       # checking sufficiency of money
                    sys.exit(f"You don't have enough money. Your balance is : {latestMoney} taka.\nPlease add more money and then try sending again")
                else :
                    latestMoney = latestMoney - taka
                    # the following line refers " it will reduce money from your main account"
                    tempData[loggedInDataLocation] = f"{list_newData[0]}--{list_newData[1]}--{list_newData[2]}--{list_newData[3]}--{list_newData[4]}--{latestMoney}--\n"
                    

            except Exception as ex:
                sys.exit("You have entered wrong ammount\n",ex)
                

            for x in range(len(tempData)) :
                rec_Data = tempData[x].split("--")     # current receiver's one line data's splitted version

                if rec_phone == rec_Data[3] :      #  rec_Data[3] contains a bank user's phone number
                    myPin = input("Please Carefully enter your 4 digit Pin-code to confirm : ")
                    
                    if myPin == list_newData[4] :        # verifying logged in user's PIN code

                        rec_money = float(rec_Data[5]) + taka
                        tempData[x] = f"{rec_Data[0]}--{rec_Data[1]}--{rec_Data[2]}--{rec_Data[3]}--{rec_Data[4]}--{rec_money}--\n"
                            # tempData[x] is now defined , now we just have to write this " tempData " variable to that .txt file
                            # thus all data wil be updated                        
                        breakMe = True
                        break

                    else :
                        sys.exit("Wrong Pin code ! ") 
            
            if breakMe == True :
                break
            else :
                # Below line will run if above's all loops and nested loops are false 
                print("Couldn't find the receiver, Check again the phone  number\n")


        with open("DontDareToOpen.txt","w") as temfile :
            temfile.writelines(tempData)        # now all data has been updated

            print("\nSending money...")
            time.sleep(2)
            print("Successfully sent money !\n")
        
        return latestMoney



    # Please read the sendMoney() function carefully to understand withdrawMoney() func
    def withdrawMoney(self) -> float :

        loggedInDataLocation = self.verifyReturn[2]
        vool = True
        with open("DontDareToOpen.txt","r") as AccLog_new :
            AccLog_new.seek(0)
            tempData = AccLog_new.readlines()

        newData =  tempData[loggedInDataLocation]
        list_newData = newData.split("--")
        latestMoney = float(list_newData[5])
        print(f"You have : {latestMoney} taka\n")
                
        while vool == True :
            try:
                taka = float(input("Enter the ammount to withdraw : "))
                if taka > latestMoney :       
                    print(f"You don't have enough money. Your balance is : {list_newData[5]} taka.\nPlease add more money or try again with little ammount")
                else :  
                    latestMoney = latestMoney - taka
                    tempData[loggedInDataLocation] = f"{list_newData[0]}--{list_newData[1]}--{list_newData[2]}--{list_newData[3]}--{list_newData[4]}--{latestMoney}--\n"
                    break
            except Exception as ex :
                print("Wrong entry\n")
        
        with open("DontDareToOpen.txt","w") as temfile :
            temfile.writelines(tempData)        # now all data has been updated

            print("\nWithdrawing...")
            time.sleep(2)
            print("Successfully withdrawn money !\n")
        
        return latestMoney


    def viewDetails(self) :
        location = self.verifyReturn[2]
        with open("DontDareToOpen.txt","r") as temfile :
            temfile.seek(0)
            tem_y =  temfile.readlines()
            y = tem_y[location].split("--")     # getting latest updated data of logged in user

        return(f"Name : {y[1]}\nAge : {y[2]}\nPhone no. : {y[3]}\nPin code : {y[4]}\nBalance : {y[5]}\n")


    def closeAcc(self):
        location = self.verifyReturn[2]
        with open("DontDareToOpen.txt","r") as temfile :
            temfile.seek(0)
            data =  temfile.readlines()
            data.pop(location)

        with open("DontDareToOpen.txt","w") as file :
            file.writelines(data)
        print("Your account is permanently deleted")

        





if __name__ == "__main__" :
    cout = 0
    print("\n")
    print("-------------------Welcome to Goriber Kandari Bank-------------------".center(100))

    while cout == 0 :
        print("***** Choose an option from below *****\n1. Account Login\n2. Open account")
        uIn = input(">>> ")
        if uIn == "1":
            phoneNo = input("Enter your phone number\n>> ")
            pinNo = input("Enter your 4 digit bank PIN code\n>> ")
            cout = 1
            objt = AccountManage(phoneNo, pinNo)
            verf = objt.verifyReturn

            while cout < 3 :
                if verf[0] == True :
                    
                    menu = "***** Choose an option from below *****\n1. Add Money\n2. Send Money\n3. Withdraw Money\n4. Manage Account\n5. Exit\n>>> "
                    
                    while cout < 3 :
                        userChoice = input(menu)
                        if userChoice == "1" :
                            print(f"You have : {verf[3]} taka")
                            try : 
                                monVal = float(input("Enter ammount of the money : \n>> "))
                                newMoney = objt.addMoney(monVal)
                                print(f"Your new balance is : {newMoney} taka\n")
                            except Exception as ex :
                                print(ex,"\nRe-check money ammount. No string input will work\n")
                            
                        elif userChoice == "2" :
                            newMoney2 = objt.sendMoney()
                            print(f"Your new balance is {newMoney2} taka")

                        elif userChoice == "3" :
                            newMoney3 = objt.withdrawMoney()
                            print(f"Your new balance is {newMoney3} taka")

                        elif userChoice == "4" :
                            while cout == 1 :
                                inp = input("--------Account Manager--------\n1. View your details\n2. Close account\n>> ")
                                if inp == "1" :
                                    print("\nYour details is below :")
                                    print(objt.viewDetails())  
                                    break                                  

                                elif inp == "2" :
                                    print("\nClosing your account. Please wait...\n")
                                    time.sleep(2)
                                    objt.closeAcc()
                                    sys.exit("We hope you will open account again !")
                                else :
                                    print("Wrong choice try again...\n")

                        elif userChoice == "5" :
                            sys.exit("Thanks for using our service\n")
                            
                        else :
                            print("Wrong input !")
                else :                    
                    print("Try again. Wrong phone number or pin")
                    break

        elif uIn == "2" :
            cout = 1
            name =  input("What is your name ?\n>>> ")
            age =  input("How old are you ?\n>>> ")
            phNo =  input("Write your phone number\n>>> ")
            print("We are almost done opening your account !\nPlease wait -")
            time.sleep(2)
            x = 0
            while x == 0 :
                try:
                    pinCode =  int(input("Please set 4 digit Pin Code\n>>> "))

                    obj = AccountOpening(name,age,phNo,pinCode)

                    break

                except:
                    print("Wrong input, Try again with only 4 or more digits\n")                    
            
        
        else:     
            print("\nChoose only 1 or 2\n")
