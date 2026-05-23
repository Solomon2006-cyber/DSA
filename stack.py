def push():
    n=int(input("Enter the element to be inserted into stack:"))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0,n)
        print(n,"is inserted in to stack")

def pop():
    if len(stack)==0:
        print("stack is empty") 
    else:
        print(stack[0],"is deleted from stack")
        del stack[0]


def display():
    if len(stack) == 0:
        print("stack is empty")      
    else:
        print("elements of stack are:")
        for element in stack:
            print(ele)
            print("Top of the stack is:",stack)
def reverse():
    string = input("Enter a string to reverse")
    print(string[::-1])
stack=list()
while(1):
    print("enter the option from below:\n 1-push operation\n 2-pop operation\n 3-display operation\n 4-string reverse operation\n enter any key to exit")
    str=int(input())
    if str == 1:
        print("push operation")
        push()
    elif str == 2:
        print("pop operation")
        pop()
    elif str == 3:
        print("display operation")
        display()
    elif str == 4:
        print("Reverse operation")
        reverse()
    else:
        print("Exiting from the program")
        break                 