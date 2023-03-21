#Используемые библиотеки
import math

#Родительский класс Геометрические фигуры
class Geometry(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Фигура создана.")

    #Объявление виртуальных методов find_area и find_perimeter
    def find_area(self):
        raise NotImplementedError

    def find_perimeter(self):
        raise NotImplementedError

    #Вывод координат фигуры
    def show_coords(self):
        print("x:{}, y:{}".format(self.x, self.y))

#Класс Треугольник. Принимает 3 стороны и координаты x и y
class Triangle(Geometry):
    def __init__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        #Проверка на создание невозможного треугольника
        if (a + b <= c or a + c <= b or c + b <= a):
            raise ValueError("Две стороны в сумме меньше чем третья!")
        #Вызов конструктора родительского класса
        super().__init__(x, y)

    #Метод нахождения площади. Перегружает метод родительского класса
    def find_area(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    #Метод нахождения периметра. Перегружает метод родительского класса
    def find_perimeter(self):
        return self.a + self.b + self.c

#Класс Прямоугольник. Принимает 2 стороны и координаты x и y
class Rectangle(Geometry):
    def __init__(self, a, b, x, y):
        self.a = a
        self.b = b
        #Вызов конструктора родительского класса
        super().__init__(x, y)

    #Метод нахождения площади. Перегружает метод родительского класса
    def find_area(self):
        return self.a * self.b
    
    #Метод нахождения периметра. Перегружает метод родительского класса
    def find_perimeter(self):
        return 2 * (self.a + self.b)

#Класс Круг. Принимает радиус и координаты x и y
class Circle(Geometry):
    def __init__(self, R, x, y):
        self.R = R
        #Вызов конструктора родительского класса
        super().__init__(x, y)

    #Метод нахождения площади. Перегружает метод родительского класса
    def find_area(self):
        return math.pi * self.R**2
    
    #Метод нахождения периметра. Перегружает метод родительского класса
    def find_perimeter(self):
        return 2 * math.pi * self.R

#Демонстрация работы
print('1: Треугольник') 
print('2: Прямоугольник') 
print('3: Круг')
typ = int(input('Выберите тип фигуры: '))
if typ == 1:
        trian = Triangle(int(input('Введите сторону a:')),int(input('Введите сторону b:')),int(input('Введите сторону c:')),int(input('Введите координату x:')),int(input('Введите координату y:')))
        print("Площадь треугольника:", trian.find_area())
        print("Периметр треугольника:", trian.find_perimeter())
        #Вызов метода родительского класса через объект подкласса
        trian.show_coords()
elif typ == 2:
        rect = Rectangle(int(input('Введите сторону a:')),int(input('Введите сторону b:')),int(input('Введите координату x:')),int(input('Введите координату y:')))
        print("Площадь прямоугольника:", rect.find_area())
        print("Периметр прямоугольника:", rect.find_perimeter())
        #Вызов метода родительского класса через объект подкласса
        rect.show_coords()
elif typ == 3:
        circ = Circle(int(input('Введите радиус R:')),int(input('Введите координату x:')),int(input('Введите координату y:')))
        print("Площадь круга:", circ.find_area())
        print("Периметр круга:", circ.find_perimeter())
        #Вызов метода родительского класса через объект подкласса
        circ.show_coords()