odds = []
even = []


while True:
    userInput = input("Please enter a number: ").strip()
    
    if userInput == "":
        print("odds:" + str(odds))
        print("evens" + str(even))
        break

    elif int(userInput) % 2 == 0:
        even.append(userInput)


    elif int(userInput) % 2 == 1:
        odds.append(userInput)

