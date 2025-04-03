myQueue=[] #list for customers and their orders
waiting=0 #counter for how many people are waiting
served=0 #counter for how many orders have been completed

def empty(): #check if the queue is empty
    if waiting==0:
        return True
    else:
        return False
def front(): #look at top item
    if empty():
        return None
    else:
        return myQueue[0]
def rear(): #look at the bottom item
    if empty():
        return None
    else:
        return myQueue[len(myQueue)-1]
def enqueue(data): #add data to queue
    myQueue.append(data)
def dequeue(): #remove top item
    myQueue.pop(0)

def takeOrder(served,waiting):
    print("")
    ordered=input("Welcome to the Fifo's Cafe! May I take your order? ")
    customername=input("Alright! Can I get a name for this order? ")
    enqueue([customername,ordered]) #add customer to queue
    waiting+=1 #update length
    print("Thank you! Your order will be finished soon.")
    Cafe(served,waiting)
def doneOrder(served,waiting):
    print("")
    served+=1 #update statistic
    waiting-=1 #update length
    ordered=myQueue[0]
    print("Order #",served,", ",ordered[1]," for ",ordered[0],"!",sep="") #announce order
    dequeue() #remove customer from queue
    print("Thank you for coming to Fifo's Cafe! Have an orderly day!")
    Cafe(served,waiting)
def Cafe(served,waiting): #Menu screen
    print("")
    print("#FIFO'S CAFE#")
    print("-=(",served,"served"," )=-")
    print("")
    if waiting>0: #If at least one person is waiting, print the queue
        print("Queue:")
        for i in range(waiting):
            print(i+1,": ",myQueue[i][1]," (",myQueue[i][0],")",sep="")
        while True: #Print controls
            print("")
            choice=input("Input F when an order is finished, or input T to take a new order. Input X to exit. ")
            if choice=="F":
                doneOrder(served,waiting)
            elif choice=="T":
                takeOrder(served,waiting)
            elif choice=="X":
                print("Thanks for coming!")
                exit()
            else:
                print("ERROR: please choose from the list given.")
                continue
    else: #If nobody is waiting, do not include F control
        print("Nobody's here yet!")
        while True:
            print("")
            choice=input("Input T to take a customer's order, or input X to exit. ")
            if choice=="T":
                takeOrder(served,waiting)
            elif choice=="X":
                print("Thanks for coming!")
                exit()
            else:
                print("ERROR: please choose from the list given.")
                continue
Cafe(served,waiting)
