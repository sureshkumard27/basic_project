class Student:
#class variable
    Stream = "COE"
#constructor

def__init__(self, name, roll_no):
self.name = name;
self.roll_no = roll_no
#Driver's code
a = Student("Ramesh", 1134)
b = Student("Mahesh", 1152)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)


print(Student.stream)

