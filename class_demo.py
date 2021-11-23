class Employee:

    # init method or constructor
    def __init__(self, no, name):
        self.no = no
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my number is', self.no)
        print('Hello, my name is', self.name)


e = Employee(123, 'Nikhil')
e.say_hi()