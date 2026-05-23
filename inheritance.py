# Multi level inheritance
class grandfather:
    def property(self):
        print("grandfathers property")
class father(grandfather):
    def business(self):
        print("fathers business")
class son(father):
    def hobby(self):
        print("sons hobby:playing cricket")

# s=son()
# s.property()
# s.business()
# s.hobby()

#Multiple inheritance
class A:
    def __init__(self):
        self.a='a'
        print(self.a)
        super.__init__()

class B:
    def __init__(self):
        self.b='b'
        print(self.b)
        super.__init__()
class C(A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super.__init__()

obj=C()
