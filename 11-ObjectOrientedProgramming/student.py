# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.sex = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.sex = "Male"
    student2.name = "Olivia"
    student2.age = 21
    student2.sex = "Female"
    student3.name = "Bolo"
    student3.age = 20
    student3.sex = "Male"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.sex}')
    print(f'{student2.name}, {student2.age} years old, {student2.sex}')
    print(f'{student3.name}, {student3.age} years old, {student3.sex}')

if __name__ == "__main__":
    main()