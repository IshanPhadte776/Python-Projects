#Imports
import random

#Array w/ strings for the different positions 
positionStrings = ["8th","7th","6th","5th","4th","3rd","2nd","1st"]

#Defines CLass
#Adds from the Front, Removes from the Front
class Stack (object) :
    #Init function
    def  __init__ (self):
        #Creates a blank list
        self.list = []

    #isEmpty method which checks to see if the list is empty
    def isEmpty(self):
        #If the length is 0 (no elements in array)
        if len(self.list) == 0:
            return True

        else:
            return False 

    #push method which requires an argument and will add the element to the stack
    def push(self,newItem):
        #Uses the argument and adds the item to the list
        self.list.append(newItem)

    #peek method which looks at the element at the top of the stack (last element)
    #Doesn't change anything 
    def peek(self):        

        return self.list[len(self.list) - 1]

    #size method which checks for the length of the stack and returns 
    def size(self):
        return len(self.list)

    #Removes the top element in the list and returns the popped element
    def pop(self):
        poppedElement = self.list[len(self.list) - 1]
        self.list.pop(len(self.list) - 1)
        return poppedElement

#Add from the left side (Back)
#Remove from the right side (Front)

class Queue (object):
    #Sets up an empty list
    def __init__ (self):
        self.list = []
    #Inserts new Element to the back of the list (index 0)
    def enqueue(self,newPlayer):
        self.list.insert(0, newPlayer)
    #Removes element from the front of the list and returns pop() uses the front value
    def dequeue(self):
        removedElement = self.list.pop()
        return removedElement
    #Checks size of the list and returns 
    def size(self):
        return len(self.list)

    #isEmpty method which checks to see if the list is empty
    def isEmpty(self):
        #If the length is 0 (no elements in array)
        if len(self.list) == 0:
            return True

        else:
            return False 

    #peek method which looks at the element at the top of the stack (last element)
    #Doesn't change anything 
    def peek(self): 
        return self.list[len(self.list) - 1]

#Creates Hot Potato Game 
hotPotato = Queue()
#Creates Stack to display the placements for the other players
placements = Stack()
#Ques up all players
hotPotato.enqueue("Jim")
hotPotato.enqueue("John")
hotPotato.enqueue("Sam")
hotPotato.enqueue("Blake")
hotPotato.enqueue("Aidan")
hotPotato.enqueue("Kyle")
hotPotato.enqueue("Carl")
hotPotato.enqueue("Thomas")

#Calculates the time limit for the hot potato to explode(number of players to be queued/ and dequeced)
timeLimit = random.randint(0,20)

#When the rating are still being determined
while hotPotato.isEmpty() == False:
    #Loops depending on the timeLimit
    for i in range(timeLimit):
        #removes and re-adds the player to the back 
        reShuffledPlayer = hotPotato.dequeue()
        hotPotato.enqueue(reShuffledPlayer)
    #Removes the player with the Hot Potato at the top of queue
    placements.push(hotPotato.dequeue())    
    #Prints the removed player and their position
    print(str(positionStrings[placements.size() - 1 ]) + " place is: " + str(placements.peek()))
