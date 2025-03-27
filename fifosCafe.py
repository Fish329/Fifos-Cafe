myQueue=[] #list for customers and their orders
waiting=0 #counter for how many people are waiting
served=0 #counter for how many orders have been completed

def empty(): #check if the queue is empty
    if waiting==0:
        return True
    else:
        return False
def top(): #look at top item
    if empty():
        return None
    else:
        return myQueue[0]
def push(data): #add data to queue
    myQueue.append(data)
def pop(): #remove top item
    myQueue.pop(0)

def takeOrder():
    print("")
    global served
    global waiting
    ordered=input("Welcome to the Fifo's Cafe! May I take your order? ")
    customername=input("Alright! Can I get a name for this order? ")
    push([customername,ordered]) #add customer to queue
    waiting+=1 #update length
    print("Thank you! Your order will be finished soon. Your order number is ", served+1,".", sep="")
def doneOrder():
    print("")
    global served
    global waiting
    served+=1 #update statistic
    waiting-=1 #update length
    ordered=myQueue[0]
    print("Order #",served,", ",ordered[1]," for ",ordered[0],"!",sep="") #announce order
    pop() #remove customer from queue
    print("Thank you for coming to Fifo's Cafe! Have an orderly day!")
def Cafe(): #Menu screen
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
                doneOrder()
                Cafe()
            elif choice=="T":
                takeOrder()
                Cafe()
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
                takeOrder()
                Cafe()
            elif choice=="X":
                print("Thanks for coming!")
                exit()
            else:
                print("ERROR: please choose from the list given.")
                continue
Cafe()
            