#Imports
import random

#My range function which inputs and start and stop number and prints the start number 
#and all numbers bigger til the stop num (not including the stop number)
def newRangeFunc(startNum,stopNum):
    #Steps up an array to print the results
    result = []
    #Adds the start number to the result
    result.append(startNum)
    #While the startNum (which changes) is less than the stopNum 
    while startNum != stopNum - 1:
        #Increments the startNum
        startNum = startNum + 1
        #Adds the num to the result
        result.append(startNum)

    #Results the result
    return result

#My custom maxFunction which takes an input, 
#creates a random array contains numbers from 0 to the input and returns the maximum value
def newMaxFunction (input):
    #Creates an array containing all the random integers
    randomInts = []
    #The maximum number in the array
    maxNum = 0

    #When there's less numbers in the array compared to the input
    while len(randomInts) < input:
        #Picks a random number between 0 and the input
        randomNum = random.randint(0,input)
        #Adds the random number the array (includes the duplicates)
        randomInts.append(randomNum)

    #Makes a print statement for the array
    print("The Array of the random Numbers are "+ str(randomInts))

    #For every element within the array
    for i in randomInts :
        #If that number is larger than the maxNum
        if i > maxNum:
            #Updates the maxNum to the new max Number
            maxNum = i
    #Returns the maxNum
    return maxNum

#Formatted print statements
print("Calling the new Range Function with 5 as the start and 10 as the end. The result will display 5,6,7,8,9")
print(newRangeFunc(5,10))
print("Calling the new Max function with the number 8")
print("The Max number is " + str(newMaxFunction(8)))
