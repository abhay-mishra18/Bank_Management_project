import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data=[]

    try:
        if Path(database).exists():  
            with open (database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print (f"an exception err occured{err}")
    @staticmethod
    def __update():
        with open(Bank.database,"w") as fs:
            a=fs.write(json.dumps(Bank.data))
    @staticmethod
    def __accountgenerate():
        alpha1 = random.choices(string.ascii_uppercase,k=2)
        num1 = random.choices(string.digits,k=3)
        alpha2 = random.choices(string.ascii_uppercase,k=1)
        num2 = random.choices(string.digits,k=2)
        alpha3 = random.choices(string.ascii_uppercase,k=1)
        num3 = random.choices(string.digits,k=1)
        id=alpha1+alpha2+alpha3+num1+num2+num3
        random.shuffle(id)
        return "".join(id)
        



    def CreateAccount(self):
        info = {
            "Name" : input("Enter your name :- "),
            "age" : int(input("Enter your age :-")),
            "email" : input("Enter your email id :- "),
            "AccountNo" : Bank.__accountgenerate(),
            "pin" : input(f"Enter your desired pin for your account :-"),
            "Balance" : 0
        }

        if info['age']<18:
            print("Sorry you are not eligible to create an account")
        if "@" or "." not in info["email"]:
            print("You entered a wrong email ID..")
        if len(str(info['pin'])) !=4:
            print("Sorry you are not eligible to create an account")
        else :
            print("\n\n----You have successfully created an account----")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account No. ")
            Bank.data.append(info)
            Bank.__update()

    def depositMoney(self):
        accnumber=input("Please tell your account number :- ")
        pin = input("Please enter your pin :- ")
        userdata= [ i for i in Bank.data if i["AccountNo"] == accnumber  and i["pin"] == pin ]

        if userdata==False:
            print("Sorry no data found")    

        else :
            amount = int(input(" Enter the amount you want to deposit :- "))
            if amount < 0 or amount == 0:
                print("Please enter a valid amount..!! ")
            
            else:
                userdata[0]["Balance"] +=amount
                Bank.__update()
                print("Amount deposited successfully")

    def withdrawMoney(self):
        accnumber=input("Please tell your account number :- ")
        pin = input("Please enter your pin :- ")
        userdata= [ i for i in Bank.data if i["AccountNo"] == accnumber  and i["pin"] == pin ]

        if userdata==False:
            print("Sorry no data found")    

        else :
            amount = int(input(" Enter the amount you want to withdraw :- "))
            if amount < 0 or amount == 0:
                print("Please enter a valid amount..!! ")
            if amount >25000:
                print("WITHDRAWAL FAILED: DAILY WITHDRAWAL LIMIT EXCEEDED ")
            if userdata[0]['Balance'] < (amount):
                print("You don't have this much amount in your bank account") 
            
            else:
                userdata[0]["Balance"] -=amount
                Bank.__update()
                print("Withdrawl Successful")

    def Details(self):
        accnumber=input("Please tell your account number :- ")
        pin = input("Please enter your pin :- ")
        userdata= [ i for i in Bank.data if i["AccountNo"] == accnumber  and i["pin"] == pin ]

        if userdata==False:
            print("Sorry no data found") 

        else:
            print("\n----Your details are as follows----\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def UpdateDetails(self):
        accnumber = input("Please tell your account number :- ")
        pin = input("Please enter your pin :- ")
    
        userdata = [i for i in Bank.data if i["AccountNo"] == accnumber and i["pin"] == pin]

   
        if not userdata:
            print("Sorry no data found")
            return
        
        user = userdata[0]

        print("\nWhat do you want to update?")
        print("N - Name")
        print("P - Pin")
        print("E - Email")

        choice = input("Enter your choice (N/P/E): ").lower()

        if choice == "n":
            new_name = input("Enter new name: ")
            user["Name"] = new_name
            print("Name updated successfully!")

        elif choice == "p":
            new_pin = input("Enter new pin: ")
            user["pin"] = new_pin
            print("Pin updated successfully!")

        elif choice == "e":
            new_email = input("Enter new email: ")
            user["email"] = new_email
            print("Email updated successfully!")

        else:
            print("Invalid option!")
            return

        Bank.__update()
        print("Details saved successfully!")

    def DeleteAccount(self):
        accnumber = input("Please tell your account number :- ")
        pin = input("Please enter your pin :- ")
    
        userdata = [i for i in Bank.data if i["AccountNo"] == accnumber and i["pin"] == pin]

        if not userdata:
            print("Sorry no data found")
            return
        
        else:
            remainder= input("Do you really wanna delete your account permanently (yes/no) : ")

            if remainder == ("yes"):
                userdata[0].replace("")
                print("\n Your account has been deleted successfully..!! ")

            elif remainder == ("no"):
                print("\nThank you for staying with us! Your trust means a lot, and we are committed to providing you with better services.")

            else:
                print("\nInvalid response. Please type 'yes' or 'no'.")

        Bank.__update()



            
        



user=Bank()

print("Press 1 for creating an account")
print("Press 2 for depositing the money in account")
print("Press 3 for withdrawing money")
print("Press 4 for Details")
print("Press 5 for updating the deatils")
print("Press 6 for deleting your account ")

check=int(input("Tell your response :- "))
if check == 1:
    user.CreateAccount()

if check == 2:
    user.depositMoney()

if check == 3:
    user.withdrawMoney()

if check == 4:
    user.Details()

if check == 5:
    user.UpdateDetails()

if check == 6:
    user.DeleteAccount()