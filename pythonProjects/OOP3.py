#Defines Class
class Fractions (object):
    #Init Method where a numerator and denominator is needed 
    def __init__ (self,numerator,denominator):
        #Sets variables
        self.numerator = numerator
        self.denominator = denominator

    #Creates fraction from two inputs and returns 
    def calcFunction (self):
        fraction = "Your fraction is "+str(self.numerator) + "/" + str(self.denominator)
        return fraction

    #Using the self numerator/ denominator and given , multiples fractions and reduces
    def multipleFraction (self,givenNumerator,givenDenominator):
        #Multiples Numerators and Denominators
        newNumerator = self.numerator * givenNumerator
        newDenominator = self.denominator * givenDenominator

        #i is every number to check for a commom denominator 
        i = 1
        #The default is 0 and will increase later
        gcd = 0
        #while i is any number below one value (potential GCD)
        while i <= newNumerator or i <= newDenominator:
            #If i is divisable by both the Numerator and Denominator...
            if newNumerator%i == 0 and newDenominator%i == 0:
                #Updates the GCD
                gcd = i
            #increments i
            i += 1

        #reduces both numerator and denominator by the GCD and ints it to prevent floats 
        newNumerator = int(newNumerator / gcd)
        newDenominator = int(newDenominator / gcd)

        #Returns the new Fraction
        return "Your new fraction is after Multplication is..." + str(newNumerator) + "/" + str(newDenominator)

#Asks user for a numerator and denominator 
inputtedNumerator = int(input("Type in a Numerator: "))
inputtedDenominator = int(input("Type in a Denominator: "))

#Creates an instance of the Fractions Class
myFraction = Fractions(inputtedNumerator,inputtedDenominator)
#Calls method and returns the fraction
print(myFraction.calcFunction())
#Completes multiplication, reduces and returns
print(myFraction.multipleFraction(2,8))