class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


s1 = Student("Navya", 80)
s2 = Student("Ravi", 90)

total = s1 + s2

print("Total Marks:", total)