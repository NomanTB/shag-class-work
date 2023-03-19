# class St:   #клас начинаеться с большей буквы
#     a = "AAAAA"  #конструктор
#     b = "BBBB"
# ob = St()       #записываем клас в переменную
# ob2 = St()
# ob2.a = "Roma"    #переменную класа можно поменять
# print(ob2.a)     #виводим Roma рома потому что мы его поменяли

class Student:
    def __init__(self, name: str = "Ab", age: int =20, country: str = "France"):  #переменным в нутри мы можем дать значия по умолчанию
        self.name = name    #self это заменяемый конструктор ниже показано что место self можно поставь любую переменную и получить обект
        self.age = age       #self это заменяемый конструктор ниже показано что место self можно поставь любую переменную и получить обект
        self.country = country     #self это заменяемый конструктор ниже показано что место self можно поставь любую переменную и получить обект

    def print_date(self):
        print(f'Hello i name is {self.name}. i am {self.age}. i from {self.country}')    # сдесь мы можем подставить в место переменных функции значения



one = Student(name='Roma', age=20, country='Ukraine')     # СЕНЯЕМ ЗНАЧЕНИЯ ПЕРЕМЕННЫХ
two = Student('Sara', 13, 'Safain')    #меняем значения переменных и оставляем по умолчанию
three =Student(age = 31)

print(one.name)   # выводим часть функции

one.print_date()   #выводим функцию print_date с изменеными значениями
two.print_date()   #выводим функцию print_date с изменеными значениями
three.print_date()   #выводим функцию print_date с изменеными значениями

