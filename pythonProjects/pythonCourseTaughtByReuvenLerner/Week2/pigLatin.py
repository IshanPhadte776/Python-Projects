userInput =str(input("Please enter a sentence: "))
output = []

for i in userInput.split():
    if i[0] in "aeiou":
        output.append(i + "way")        

    else:
        output.append(i[1:] + i[0] + "ay")

print(" ".join(output))
