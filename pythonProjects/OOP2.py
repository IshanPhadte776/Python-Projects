#Defines CLass
class Stack (object) :
    #Init function
    def  __init__ (self):
        #Creates a blank list
        self.list = []
        #Prints
        print("-------------")
        print("The Array looks like " + str(self.list))
        print("-------------")


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
        #Prints
        print("The Array looks like " + str(self.list))
        print("-------------")

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
#Creates an instance of the class
myList = Stack()
#Calls methods and prints
print("The list is empty? " + str(myList.isEmpty()))
print("-------------")
myList.push(4)
myList.push('dog')
print("The Top element in the list is... "+ str(myList.peek()))
print("-------------")
myList.push(True)
print("The length of the list is "+str(myList.size()) + " Elements long")
print("-------------")
print("The list is empty? " + str(myList.isEmpty()))
print("-------------")
myList.push(8.4)
print("The popped element in the list is: "+str(myList.pop()))
print("-------------")
print("The popped element in the list is: "+str(myList.pop()))
print("-------------")
print("The length of the list is "+str(myList.size()) + " Elements long")
print("-------------")
