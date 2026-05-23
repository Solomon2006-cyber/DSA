class parent:
    def show(self):
        print("This is parent class method")

class child(parent):
    def show(self):
        print("This is child class method")

obj=child()
obj.show()




