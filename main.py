<<<<<<< HEAD
# Expense tracking System

expensesList = []  #list of expensese in th form of dictionary
print("Welcomw to Expense Tracker : Kharcha kum kiya karo")

while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. Total of All Expense")
    print("4. Exit")

    Choice = int(input("Please enter your choice :"))

# ADD EXPENSE
    if (Choice == 1):
        date = input("Enter the date :")
        category = input("Enter the category like (food ,travel makeup):")
        description = input("Enter the specific detail :")
        Amount = float(input("Enter the total Amount :"))


        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "Amount" : Amount 
        }

        expensesList.append(expense)
        print("\n Expenses added succesfully")

# View All Expenses

    elif (Choice == 2):
        if ( len(expensesList )== 0):
            print("No Expensees Added jao jakr kharcha karoo :)")

        else:
            print("====This is your total Expenses====")
            count = 1
            for eachkharcha in expensesList:
                print(f"Kharcha Number {count} -> {eachkharcha["date"]}, {eachkharcha["category"]}, {eachkharcha["description"]}, {eachkharcha["Amount"]} ")
                count= count+1

# View Total Amount spend
    elif (Choice == 3):
        Total = 0
        for eachkharch in expensesList:
            Total = Total + eachkharch["Amount"]
        print("====Total spend Money ====", Total)

# User wants to Exit
    elif(Choice == 4):
        print("================Thank You For using Our System================")
        break

    else:
        print("Invalid Choice Try Again")


=======
# RULE BASE BASIC CHATBOT

import datetime
import time

name = input("Welcome Enter your name :")
presentTime = datetime.datetime.now().hour

if 5 <= presentTime <= 11:
    print("Good Morning,",name)
elif 11 <= presentTime <= 17:
    print("Good afernooon,",name)
elif 17 <= presentTime <= 20:
    print("Good Evening,",name)
else:
    print("Good Night,",name)


print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")


# Chatbot Memory Creation [ dictionary of responses ]
responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot ",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that",
    "functions kya hote hai": "jakar chapter 7 padho"
}

# add new resppnsese using update function
responses.update({
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs 😄",
    "what is your purpose": "My purpose is to help you with basic questions and make your day easier!",
    "who created you": "I was created by a developer like you who is learning Python 🚀"
})

# method function to get a response
def getResponsebot(userQuestion):
    userQuestion = userQuestion.lower()

     # 😊 Happy response
    if "happy" in userQuestion:
        return "That's awesome 😄 Keep smiling and enjoy your day!"

    # 😢 Sad response
    elif "sad" in userQuestion:
        return "I am here for you 💙 Don't worry, things will get better!"

    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return("i am not able to ans yet i am in still learning face")


# taking and user input
while True:
    userinput = input("Pls ask your question :")
    reply = getResponsebot(userinput)
    time.sleep(1)  # add 1 sec delay to provide and ans
    print("Bot Reply :",reply)

    if "bye" in userinput.lower():
        print("Bot Reply: Bye! Have a nice day 😊")
        break
>>>>>>> 07d57a2 (Initial commit - Python Project)
