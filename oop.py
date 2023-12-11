class Student:
    def pass_fail(self):
        if self.marks >=50:
           return True
        else:
            return False
student1 = Student()
student1.name = 'Hamza'
student1.marks = 85
did_pass = student1.pass_fail()

print(student1.name , student1.marks)
print(did_pass)

student2 = Student()
student2.name = 'jey'
student2.marks = 40
did_pass = student2.pass_fail()

print(student2.name,student2.marks)
print(did_pass)
