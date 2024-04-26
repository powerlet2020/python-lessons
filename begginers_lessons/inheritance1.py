class human:
    def __init__(self):
        self.number_eyes = 2
        self.number_nose = 1
    def eat(self):
        print('i can eat :')
    def work(self):
        print('i can work')
class Male(human):
    def __init__(self, name):
        self.name = name
        super().__init__()
    def flirt(self):
        print('i can flirt')
    def work(self):
        print('i can code')
        super().work()
male_1 = Male('Hamza')
male_1.eat()
male_1.flirt()
male_1.work()
print(male_1.name)
print(male_1.number_eyes)