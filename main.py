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