class Student:
    
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name.title()
        self.lastname = lastname.title()
        self.department = department.title()
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        print(f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}.')

vasya = Student('вася', 'иванов', 'программирование', 2017)

vasya.get_student_info()