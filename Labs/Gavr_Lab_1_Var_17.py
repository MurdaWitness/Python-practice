class Room(object):
    #Конструктор класса. Поля длина, ширина и высота соответственно
    def __init__(self, length, width, height):
        self.length = int(length)
        self.width = int(width)
        self.height = int(height)
    #Метод нахождения площади стен
    def square(self):
        return 2 * self.height * (self.length + self.width)
    #Метод нахождения площади стен без окна и двери
    def square_without(self):
        return self.square() - 2*15 - 2*8
    #Метод формирования строки информации об объекте
    def __str__(self):
        return "Class: Room. length = {0}, width = {1}, height = {2}".format(self.length, self.width, self.height)
    #Деструктор класса.
    def __del__(self):
        print("Object destroyed.")
    
appart_1 = Room(7,5,3)
appart_2 = Room(input("Input appartement length:"),input("Input appartement width:"),input("Input appartement height:"))
appart_3 = Room(input("Input appartement length:"),input("Input appartement width:"),input("Input appartement height:"))
print("Appartement square:", appart_1.square())
print("Appartement square without window and door:", appart_2.square_without())
#Вывод строки информации об объекте
print(appart_3)
