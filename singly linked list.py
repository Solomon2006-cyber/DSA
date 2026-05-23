class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlylinkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            Current=self.head
            while Current.next!=None:
                Current=Current.next
            Current.next=newnode

    def delete(self):
        if self.head is None:
            print("List is Empty")
        elif self.head.next is None:
            self.head=None
        else:
            Current=self.head
            while Current.next!=None:
                prev=Current
                Current=Current.next
            prev.next=None

    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            Current=self.head
            while Current!=None:
                print(Current.data,end="-->")
                Current=Current.next
            print("None")

s=singlylinkedlist()
s.insert(10)
s.insert(20)
s.insert(30)
s.display()
s.delete()
s.display()
s.delete()
s.display()
