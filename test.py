class Parent:
    def __init__(self):
        self.value = "test"
        print(" Parent __init__ called")

    def test(self):
        print("parent test")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child __init__ called")

child = Child()
child.test()
print(child.value)

