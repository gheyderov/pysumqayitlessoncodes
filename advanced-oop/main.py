from datetime import datetime

class Person:


    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def fullname(self):
        return f'{self.name} {self.surname}'
    
    @classmethod
    def get_fullname_from_str(cls, fullname_str, age):
        name, surname = fullname_str.split('-')
        return cls(name, surname, age)
    
    @classmethod
    def get_age_from_bday(cls, name, surname, bday):
        return cls(name, surname, datetime.now().year - bday)
    
    @staticmethod
    def description():
        return 'This is a StaticMethod'



p1 = Person('Ali', 'Aliyev', 20)
p2 = Person('Kanan', 'Mirzoyev', 30)



p3 = Person.get_fullname_from_str('Samir-Aliyev', 25)



p4 = Person.get_age_from_bday('Samir', 'Aliyev', 1995)

# print(p4.description())
# print(Person.description())


print(dir(Person))