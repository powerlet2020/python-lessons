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

# ----------------lessons2....................
class Triangle:
    def AreaOfTriangle(self):
        return 0.5 * self.base * self.height
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

triangle1 = Triangle(2, 5)
area_of_triangle1 = triangle1.AreaOfTriangle()
print(area_of_triangle1)

# ..............lesson3.......................

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
       area =  0.5 * self.base * self.height
       return area

def main():
    base = float(input('Enter the base of the triangle:'))
    height = float(input('Enter the height of triangle:'))

    # create an instance of the triangle
    my_triangle = Triangle(base, height)
    area = my_triangle.calculate_area()
    print(f'The area of the triangle is:{area}')
if __name__ == "__main__":
    main()
