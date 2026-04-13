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


