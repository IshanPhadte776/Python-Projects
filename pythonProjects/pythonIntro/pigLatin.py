userInput = input("Provide me a Word and I will convert the variable into Pig Latin: ")

if userInput[0] == "a" or userInput[0] == "e" or userInput[0] == "i" or userInput[0] == "o" or userInput[0] == "u":
    output = userInput + "way"

else:
    firstLetter = userInput[0]
    output = userInput[1:] + firstLetter + "ay"
print(output)