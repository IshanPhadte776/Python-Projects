vowelCount = 0
consonantCount = 0

userInput = str(input("Please enter a string: "))

for i in userInput.strip().lower():
    if i in "aeiou": 
        vowelCount += 1
    
    elif i in "qwrtypsdfghjklzxcvbnm":
        consonantCount += 1

    else:
        print("Invalid character")


print("The Vowel Count is: " + str(vowelCount))
print("The Consonant Count is: " + str(consonantCount))
