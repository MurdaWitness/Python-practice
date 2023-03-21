import sqlite3
from sqlite3 import Error

# Включение поддержки внешнего ключа SQLite
fk = 'pragma foreign_keys = 1 '

# sql-запрос на создание таблицы cert с определением столбцов и типов данных
create_cert = 'create table if not exists cert (' \
                'id int(6) primary key,' \
                'number int(6) not null)'

# sql-запрос на создание таблицы doctor с определением столбцов и типов данных
create_doctor = 'create table if not exists doctor (' \
                'id int(6) primary key,' \
                'FIO varchar(60) not null,' \
                'age int(6) not null)'

# sql-запрос на создание таблицы child с определением столбцов и типов данных
create_child = 'create table if not exists child (' \
                'id int(6) primary key,' \
                'FIO varchar(60) not null,' \
                'FIO_father varchar(60) not null,' \
                'FIO_mother varchar(60) not null,' \
                'age int(6) not null,' \
                'id_cert int(6),' \
                'id_doctor int(6),' \
                'foreign key (id_cert) references Cert (id) on update cascade on delete cascade,' \
                'foreign key (id_doctor) references Doctor (id) on update cascade on delete cascade)'


# sql-запрос на заполнение существующей таблицы cert новыми строками
ins_cert = '''insert into cert values 
                (123, 777),
                (156, 382) '''

# sql-запрос на заполнение существующей таблицы doctor новыми строками
ins_doctor = '''insert into doctor values 
                (321, 'Свиридов И.А.', 55),
                (529, 'Курчатов Г.В.', 42),
                (854, 'Смолов Е.Д.', 51) '''

# sql-запрос на заполнение существующей таблицы child новыми строками
ins_child = '''insert into child values 
                (0001, 'Цепко А.Д.', 'Цепко Д.А.', 'Цепко Л.В.', 6, 123, 321),
                (0002, 'Тимин А.Д.', 'Тимин Д.А.', 'Тимина Л.В.', 8, 123, 529),
                (0003, 'Агафьев И.Ю.', 'Агафьев Ю.Н.', 'Агафьева К.А.', 7, 156, 529)'''


# sql-запрос на изменение подмножества значений, хранящихся в таблицах
upda0 = 'update cert set number = 747 where id = 156 '
upda1 = 'update doctor set id = 322 where FIO = "Свиридов И.А." '


# sql-запрос на удаление записи из таблицы doctor
dele = 'delete from doctor where id = 854 '


# sql-запрос на вывод всех записей таблицы cert
sel_cert = 'select * from cert '
# sql-запрос на вывод всех записей таблицы doctor
sel_doctor = 'select * from doctor '
# sql-запрос на вывод всех записей таблицы child
sel_child = 'select * from child '


sel_info = '''select c.FIO, c.FIO_father, c.FIO_mother, d.FIO, c.age
                from child as c join doctor as d 
                on d.id = c.id_doctor'''


sel_sick = '''select d.FIO, count(c.id) 
                from doctor as d inner join child as c 
                on d.id = c.id_doctor 
                group by d.FIO'''


query = [create_cert, create_doctor, create_child, ins_cert, sel_cert, ins_doctor, sel_doctor, ins_child, sel_child, upda0, upda1, sel_cert, sel_doctor, dele, sel_doctor]


def res_print(val, name):
    s = ''
    for n, item in zip(name, val):
        s += f'{n}: {item}\n'
    return s

# Функция формирования sql-запросов на вывод
def execute_query(db, query):
    # Курсор используется для выполнения инструкций по связи с базой данных
    cur = db.cursor()
    # Конструкция для обработки исключений
    try:
        for item in query:
            # Метод для выполнения команды
            cur.execute(fk)
            # Метод для подтверждения изменений, внесенных в базу данных
            db.commit()
            cur.execute(item)
            if item == str(sel_cert):
                fch = cur.fetchall()
                r = None
                for it in fch:
                    r = res_print(it, ('id', 'Номер'))
                    print(r)
                print("-----------------------------")
            elif item == str(sel_doctor):
                fch = cur.fetchall()
                r = None
                for it in fch:
                    r = res_print(it, ('id', 'ФИО', 'Возраст'))
                    print(r)
                print("-----------------------------")
            elif item == str(sel_child):
                fch = cur.fetchall()
                r = None
                for it in fch:
                    r = res_print(it, ('id', 'ФИО', 'ФИО отца', 'ФИО матери', 'Возраст', 'ID_Сертификат', 'ID_Врача'))
                    print(r)
                print("-----------------------------")
    except Error as err:
        print(f"Error: '{err}'")

# Функция вывода информации построчно в консоль по заданию
def show_info(db, info):
    cur = db.cursor()
    try:
        cur.execute(fk)
        db.commit()
        cur.execute(info)
        fch = cur.fetchall()
        r = None
        for it in fch:
            r = res_print(it, ('ФИО ребёнка', 'ФИО отца', 'ФИО матери', 'ФИО врача', 'Возраст ребёнка'))
            print(r)
        print("-----------------------------")
    except Error as err:
        print(f"Error: '{err}'")

# Функция подсчёта кол-ва пациентов у врача
def count_sick(db, sick):
    cur = db.cursor()
    try:
        cur.execute(fk)
        db.commit()
        cur.execute(sick)
        fch = cur.fetchall()
        r = None
        for it in fch:
            r = res_print(it, ('ФИО врача', 'Кол-во пациентов'))
            print(r)
        print("-----------------------------")
    except Error as err:
        print(f"Error: '{err}'")

def main():
    # Функция connect() модуля sqlite3 открывает соединение с файлом базы данных SQLite
    db = sqlite3.connect('db_hospital.db')
    cur = db.cursor()

    # sql-запрос на удаление таблицы cert из базы данных
    cur.execute('drop table if exists cert ')
    # sql-запрос на удаление таблицы doctor из базы данных
    cur.execute('drop table if exists doctor ')
    # sql-запрос на удаление таблицы child из базы данных
    cur.execute('drop table if exists child ')

    execute_query(db, query)
    show_info(db, sel_info)
    count_sick(db, sel_sick)

    # Функция close() модуля sqlite3 закрывает соединение с файлом базы данных SQLite
    db.close()

if __name__ == '__main__':
    main()
