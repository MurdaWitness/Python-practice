# Используемые библиотеки
import random
import time

# Реализация сортировки массива методом пузырька
def mysort(number, array):
    for i in range(number-1):
        for j in range(number-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


# Ввод количества элементов
n = int(input("Введите количество элементов: "))
print("\n")
# Создание списка для хранения массива 
my_list = []

# Выбор типа заполнения массива
print("1: Строго случайные данные") 
print("2: Случайные данные с малым числом уникальных значений")
print("3: Ввести массив вручную")
typ = int(input("Выберите тип заполнения массива: "))
if typ == 1:
    for i in range(n):
        my_list.append(random.randint(1, 99))
    
elif typ == 2:
    for i in range(n):
        my_list.append(random.randint(1, 4))

elif typ == 3:
    print("\n")
    print("Вводите целые числа.")
    for i in range(n):
        my_list.insert(i, int(input("A[{}] = ".format(i))))
else:
    raise ValueError("Введено неправильное значение.")

# Копирование массива
lib_list = my_list
print("\n")
slice = int(input("Введите максимальное количество элементов, выводимых на экран: "))
print("\n")
# Показ исходного массива
print("Исходный массив:\n", my_list[0:slice])
print("\n")

# Замер скорости работы функции сортировки методом "пузырька"
tik = time.perf_counter()
my_func_result = mysort(n, my_list)
tak = time.perf_counter()
my_func_time = tak - tik
# Показ осортированного массива
print("Массив, отсортированный методом \"пузырька\":\n", my_list[0:slice])
print(f"Вычисление заняло {my_func_time:0.10f} секунд.")
print("\n")

# Замер скорости работы библиотечной функции
tik = time.perf_counter()
lib_func_result = lib_list.sort()
tak = time.perf_counter()
lib_func_time = tak - tik
# Показ осортированного массива
print("Массив, отсортированный библиотечным методом:\n", lib_list[0:slice])
print(f"Вычисление заняло {lib_func_time:0.10f} секунд.")
print("\n")

# Сравнение времени работы библиотечной сортировки и сортировки методом "пузырька"
print(f"Библиотечный метод сортировки быстрее в {my_func_time/lib_func_time:0.1f} раз.")