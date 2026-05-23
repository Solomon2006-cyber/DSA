class Book1:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages

class Book2:
    def __init__(self,pages):
        self.pages=pages
b1=Book1(100)
b2=Book2(200)
print("Total no of pages:",b1+b2)  
       