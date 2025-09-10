class Parent:
    def __init__(self):
        self.value = "test"
        print(" Parent __init__ called")

    def test(self, value):
        print(value)

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child __init__ called")

    def test2(self):
        print("========")
        print(Parent.test(self, 222))


child = Child()
child.test(1)
print(child.value)
child.test2()



