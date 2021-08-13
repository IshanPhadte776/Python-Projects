#Import
import math
#Class
class myPoint(object):
    #Init method with default arguments (aren't parameters) Creates point at 0,0 
    #Uses self to refer to itself
    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y
        #Updates X and Y and prints
        print("The default Values for X and Y are ...")
        print(x)
        print(y)
        print("-------------")

    #Gets X  and Y value from self 
    def getX (self):
        return self.x

    def getY (self):
        return self.y

    #Uses the argument when calling function and updates the values 
    def setX(self,newX):
        self.x = newX

    def setY (self,newY):
        self.y = newY

    def setXY (self,newX,newY):
        self.x = newX
        self.y = newY

    def getXY (self):
        #Tuple is immutable meaning unchangable 
        xyPoint = (self.x,self.y)
        print(type(xyPoint))
        return xyPoint

    #Using the self (instance point) and given X and Y, gets two points and calculates the distance between the two pythagorean theorem
    def distance (self,givenX,givenY):
        #math.sqrt is square root, ** means to the power of 
        distance = (math.sqrt((self.x - givenX) ** 2 + (self.y - givenY) ** 2))

        return distance

    #Using the self (instance point) and given X and Y, gets two points and calculates the midpoint (Rise/Run )
    def midpoint (self,givenX,givenY):

        midPoint = ((givenX + self.x) / 2 , (givenY + self.y) / 2)

        return midPoint
#Creates objects
point1 = myPoint()
point2 = myPoint()

#Sets Values and Prints
point1.setX(3)
point1.setY(4)

point2.setX(5)
point2.setY(6)


print("Point 1 X is "+ str(point1.getX()))
print("Point 1 Y is "+ str(point1.getY()))
print("-------------")

print("Point 2 X is "+ str(point2.getX()))
print("Point 2 Y is "+ str(point2.getY()))
print("-------------")

#Resets values and prints
point1.setXY(2,4)
point2.setXY(4,7)

print("Point 1 X and Y values are "+ str(point1.getXY()))
print("Point 2 X and Y values are "+ str(point2.getXY()))
print("-------------")

#Calculates the Distance and Midpoint using point1 as the "self" and point2 are the "given"
print("The Distance between Point 1 and Point 2 is "+ str(point1.distance(point2.getX(),point2.getY())))
print("The Midpoint between Point 1 and Point 2 is "+ str(point1.midpoint(point2.getX(),point2.getY())))
