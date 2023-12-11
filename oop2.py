class Student:
    def check_pass_fail(self):
        if self.marks >=50:
            return True
        else:
            return False

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
student1 = Student('Hamza', 85)
student2 = Student('jey', 40)

print(student1.name)
print(student1.marks)
did_pass= student1.check_pass_fail()
print(did_pass)

print(student2.name)
print(student2.marks)
did_pass = student2.check_pass_fail()
print(did_pass)