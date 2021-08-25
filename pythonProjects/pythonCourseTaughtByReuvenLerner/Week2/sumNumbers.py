total = 0

while True:
    userInput = (input("Please enter a number: ")).strip()
    if userInput == "":
        print("The Total is: "+ str(total))
        break

    total += int(userInput)
