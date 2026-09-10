class Student:
    def __init__(self, n, r, p):
        self.name = n
        self.roll = r
        self.phone = p

    def display(self):
        print(f'Name: {self.name}')
        print(f'Roll: {self.roll}')
        print(f'Phone: {self.phone}')


student1 = Student("Miftahul Islam", "3", "01711111111")
student1.display()
