# Используемые библиотеки
import numpy as np
import matplotlib.pyplot as plt

# Ввод параметров функции
a = float(input('Введите параметр a: '))
b = float(input('Введите параметр b: '))
c = float(input('Введите параметр c: '))
d = float(input('Введите параметр d: '))
print("\n")

# Ввод параметров границ графика
xl = int(input('Введите левую границу OX: '))
xr = int(input('Введите правую границу OX: '))
if xl >= xr:
    raise ValueError('Значение левой границы больше или равно правой.')
print("\n")

# Ввод параметров линии
step = abs(float(input('Введите шаг точек по оси OX: ')))
lw =  abs(int(input('Задайте толщину линии: ')))
print("\n")

# Выбор типа линии
print('Типы линии:')
print('1: Сплошная')
print('2: Тире')
print('3: Пунктир')
typ = int(input('Выберите тип линии: '))
if typ == 1:
    ls = '-'   
elif typ == 2:
    ls = '--'
elif typ == 3:
    ls = ':'
else: 
    raise ValueError('Введён неверный номер параметра.')
print("\n")

# Выбор цвета графика
print('Цвета графика:')
print('1: Чёрный') 
print('2: Красный') 
print('3: Синий')
typ = int(input('Выберите цвет графика: '))
if typ == 1:
    cl = 'black'     
elif typ == 2:
    cl = 'red'
elif typ == 3:
    cl = 'blue'
else: 
    raise ValueError('Введён неверный номер параметра.')
print("\n")

# Выбор цвета фона
print('1: Белый') 
print('2: Фиолетовый') 
print('3: Зелёный')
typ = int(input('Выберите цвет фона: '))
if typ == 1:
    facecl = 'white'     
elif typ == 2:
    facecl = 'purple'
elif typ == 3:
    facecl = 'green'
else: 
    raise ValueError('Введён неверный номер параметра.')

# Создание фона с заданным цветом
ax = plt.subplot() 
ax.patch.set_facecolor(facecl)
ax.patch.set_alpha(1.0)

# Значения по x с выбранным интервалом и шагом
x = np.arange(xl, xr, step)  
# Функция
f = a * np.cos(b*x**2 + c*x + d)

# Отрисовка функции по значениям x с заданным цветом,типом линии и шириной
plt.plot(x, f, color = cl,linestyle = ls ,linewidth = lw)             
# Создание осей              
plt.subplot().spines['left'].set_position('center')        
plt.subplot().spines['bottom'].set_position('center')
# Заголовок функции
plt.title(r'$x$')           

# Показ готового графика
plt.show()