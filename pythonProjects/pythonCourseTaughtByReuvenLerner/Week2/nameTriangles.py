

userInput = str(input("Please enter a string: "))
outputLength = 0

while outputLength < len(userInput):
    print(userInput[0:outputLength+1])
    outputLength += 1


