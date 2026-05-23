# Implement the following queue operations in python
def enqueue():
    n = int(input("Enter the element to be inserted into Queue:"))
    queue.append(n)
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print(queue[0],"element is deleted from the queue")
        del queue[0]
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Elements of the queue are:")
        for ele in queue:
            print(ele, end=" ")

queue = list()
while(1):
    print("Enter the operation from below\n 1 - enqueue operation\n 2 - dequeue operation\n 3 - display operation\n Enter any key to exit")
    option = int(input("Enter the option"))
    if option == 1:
        print("enqueue operation")
        enqueue()
    elif option == 2:
        print("dequeue operation")
        dequeue()
    elif option == 3:
        print("display operation")
        display()
    else:
        print("Exiting from the program")
        break
    