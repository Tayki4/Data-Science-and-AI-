
class Araba:
    door_number = 0
    engine_size = 5.6
    torque = 500
    lenght = 3.1
    width = 1.2
    color = 'black'
    brand = 'Dodge'
    model = 'TRX 1500'

a1 = Araba()
a1.torque = 1000
print(f'Brand: {a1.brand}\nModel: {a1.model}\Torque: {a1.torque}')

class Boxer:
    alias = ''
    height = 0.0
    weight = 0
    full_name = ''
    win = 0
    lost = 0

boxer1 = Boxer()
boxer1.alias = 'iron'
boxer1.height = 1.80
boxer1.weight = 100
boxer1.win = 66
boxer1.lost = 4
print(boxer1.__dict__)


class Student:
    #* class attribute
    taken_courses = ['History I', 'Algorithm']

    def __init__(self, full_name: str, student_id: str):
        #? object attribute
        self.tam_ad = full_name
        self.ogrenci_id = student_id
    
s1 = Student(full_name='burak yılmaz', student_id='123456789')
print(
    f'Student Name: {s1.tam_ad}\n'
    f'Student Id: {s1.ogrenci_id}\n'
    f'Taken Courses: {s1.taken_courses}'
)

print(dir(Student))
#* ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'taken_courses']
print(dir(s1))
#* ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ogrenci_id', 'taken_courses', 'tam_ad']

boxers = list()
print(dir(boxers))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


class Circle:
    pi = 3.14

    def __init__(self, r: int):
        self.radius = r
    
    def calculate_area(self):
        return self.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * self.pi * self.radius

c1 = Circle(r=1.02)
print(c1.calculate_area())
print(c1.calculate_perimeter())


class Department:
    # class attribute
    departmant_name = ''
    employee_count = 0

    def __init__(self, name: str, age: int):
        # object attribute türkçe isimlendiriler
        self.adi = name
        self.yas = age
        Department.employee_count += 1
    
    def show_info(self):
        print(
            f'Name: {self.adi}\n'
            f'Age: {self.yas}\n'
            f'Depermant Name. {self.departmant_name}'
        )
    
    def show_employee_count(self):
        print(f'Total Employee: {self.employee_count}')

d1 = Department(name='burak', age=36)
d1.departmant_name = 'ARGE'
d1.show_info()
d1.show_employee_count()

d2 = Department(name='hakan', age=39)
d2.departmant_name = 'Amele'
d2.show_info()
d2.show_employee_count()

d3 = Department(name='ipek', age=42)
d3.departmant_name = 'qwe'
d3.show_info()
d3.show_employee_count()


#! SoftwareDeveloper sınıfı yaratalım
#? first_name, last_name --> object attribute olsun
#* knowledge_languages = [] --> class attribute
#todo: add_new_language()
#? sampe input --> 'python, C#, go'
#! sample -- knowledge_languages = ['python', 'c#', 'go']
#* sample input --> 'python'
#todo: show_info()

class SoftwareDeveloper:
    knowledge_languages = []

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    
    def add_new_language(self, input_language: str) -> str:
        lst_language = input_language.split(',')

        for item in lst_language:
            if item not in self.knowledge_languages:
                self.knowledge_languages.append(item)
        
        return 'Language has been added.'

    def show_info(self):
        return (
            f'First Name: {self.first_name}\n'
            f'Last Name: {self.last_name}\n'
            f'Languages: {self.knowledge_languages}'
        )

s1 = SoftwareDeveloper(first_name='Burak', last_name='Yılmaz')
print(
    s1.add_new_language(input_language='python, c#, vb.net'))
print(
    s1.show_info()
)

x = 3

boxers = ['mike tyson', 'muhammed ali']

def hello():
    print('fdsfsd')

def greeting(first_name: str):
    print(f'{first_name} hello')

