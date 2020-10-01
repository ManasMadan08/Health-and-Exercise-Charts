#https://codewithharry.com/videos/python-tutorials-for-absolute-beginners-32
# soln =>   https://codewithharry.com/videos/python-tutorials-for-absolute-beginners-37
# Exercise 5: Health Management System
'''
The task is to create a "Health Management System." Suppose you are a fitness trainer and nutritionist. You have to deal with three clients, i.e., (Harry, Rohan, Hammad). For each client, you have to design their exercise and diet plan.

Instructions:
- Create a food log file for each client
- Create an exercise log file for each client.
- Ask the user whether they want to log or retrieve client data.
- Write a function that takes the user input of the client's name. After the client's name is entered, A message should display "What you want to log. Diet or Exercise"
- Use function
 

def getdate():
    import datetime
    return datetime.datetime.now()
The purpose of this function is to give time with every record of food or exercise added in the file.
Write a function to retrieve exercise or food file records for any client.
'''


def getdate():
    import datetime
    return datetime.datetime.now()


def LogChoice(name,thing):
    write = input("Enter What You Want To Write\t:\t")
    f = open(f"28_{name}_{thing}.txt","a")
    f.write(f"{getdate()}\t{write}\n")
    f.close()


def RetrieveChoice(name,thing):
    try:
        f = open(f"28_name_{thing}.txt")
        print(f.read())
        f.close()
    except:
        print("No Records Found!")


def inputs():
    name = input("Enter Your Name\t:\t")
    choice = input("What You Want To Do ( Log / Retrieve ) \t:\t")
    opt = input("Enter Exercise or Diet\t:\t")
    return choice,name,opt


choice,name,option = inputs()


if choice == "Log":
    LogChoice(name,option)
elif choice == "Retrieve":
    RetrieveChoice(name,option)
else:
    print("------------------------------------------")
    print("\n\nSomething Was Wrong!!!")
    inputs()
