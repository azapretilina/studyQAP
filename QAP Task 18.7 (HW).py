import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        0. Вывести список команд
        1. Добавить новый предмет 
        2. Добавить нового ученика 
        3. Добавить оценки ученика по предмету 
        4. Редактировать оценку ученика 
        5. Редактировать ученика/предмет
        6. Удалить оценку 
        7. Удалить ученика/предмет
        8. Вывести средний балл по всем предметам по каждому ученику 
        9. Вывести средний балл по всем предметам для ученика 
        10. Вывести все оценки по всем ученикам 
        11. Вывести все оценки по ученику 
        12. Выход из программы 
        ''')
while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить новый предмет')
        # вводим наименование нового предмета
        new_class_ = input('Введите наименование предмета: ').strip().title()
        # проверяем отсутствие такого предмета в списке
        if new_class_ not in classes:
            # добавляем новый предмет
            classes.append(new_class_)
            # добавляем предмет всем ученикам
            for s in students:
                students_marks[s][new_class_] = []
            print(f'Предмет {new_class_} добавлен ученикам')
        else:
            print('ОШИБКА: данный предмет уже есть в журнале')
        print(f'Список предметов журнала: {classes}')
    elif command == 2:
        print('2. Добавить нового ученика')
        new_student_ = input('Введите имя ученика: ').strip().title()
        # проверяем наличие ученика в списке
        if new_student_ not in students:
            # добавляем ученика в список учеников и привязываем его к предметам
            students.append(new_student_)
            students_marks[new_student_] = {}
            for class_ in classes:
                students_marks[new_student_][class_] = []
            print(f'Новый ученик {new_student_} добавлен в журнал')
            print()
            # выводим получившийся словарь с оценками с новым учеником
            for student in students:
                print(f'''{student}
                        {students_marks[student]}''')
        else:
            print('ОШИБКА: данный ученик в уже есть в журнале. Добавьте фамилию и/или иные опознавательные символы')
            print(f'Список учеников журнала: {students}')
    elif command == 3:
        print('3. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ').strip().title()
        # считываем название предмета
        class_ = input('Введите предмет: ').strip().title()
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 4:
        print('4. Редактировать оценку ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ').strip().title()
        # считываем название предмета
        class_ = input('Введите предмет: ').strip().title()
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            marks = students_marks[student][class_]
            # проверяем есть ли вообще оценки у ученика по этому предмету
            if not marks:
                print(f'У ученика {student} ещё нет оценок по предмету {class_}')
                continue
            # выводим все имеющиеся оценки ученика
            print(f'Текущие оценки ученика {student} по предмету {class_}:')
            for i in range(len(marks)):
                print(f'{i+1}) {marks[i]}')
            # запрашиваем оценку для изменения
            markOld = int(input('Введите порядковый номер оценки для редактирования: '))
            # если пользователь ввел несуществующий порядковый номер оценки
            if markOld < 1 or markOld > len (marks):
                print(f'ОШИБКА: оценки с порядковым номером {markOld} нет в списке')
                continue
            markNew = int(input('Введите новую оценку: '))
            # проверка на корректный ввод оценки
            if markNew > 5 or markNew < 1:
                print('ОШИБКА: некорректное значение оценки. Диапазон оценок должен быть от 1 до 5')
                continue
            else:
                marks[markOld-1] = markNew
                print(f'Для {student} по предмету {class_} изменена оценка. Новая оценка: {markNew}')
                # выводим обновленный список оценок ученика по предмету
                print()
                print(f'\t{class_} - {students_marks[student][class_]}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 5:
        print('5. Редактировать ученика/предмет')
        sub_command = int(input('''
            Что вы хотите отредактировать?
            1. Имя ученика
            2. Наименование предмета
            Введите команду: '''))
        if sub_command == 1:
            # считываем имя ученика
            student = input('Введите имя ученика: ').strip().title()
            # проверяем наличие ученика в списке
            if student not in students:
                print('ОШИБКА: Данного ученика нет в журнале')
                continue
            else:
                # получаем новое значение для ученика
                studentNew = input('Введите новое имя для ученика: ').strip().title()
                # проверяем наличие нового имени ученика в журнале
                if studentNew in students:
                    print('ОШИБКА: ученик с таким именем уже есть в журнале')
                    print()
                    print(f'Текущий список учеников: {students}')
                else:
                    # выясняем индекс ученика, которого будем менять и присваиваем новое имя по индексу
                    studentOld = students.index(student)
                    students[studentOld] = studentNew
                    # сохраняем его оценки
                    marks = students_marks[student]
                    # создаем новую запись в словаре и присваиваем ему оценки
                    students_marks[studentNew] = marks
                    # удаляем старого ученика
                    del students_marks[student]
                    print(f'Имя ученика изменено. Новое имя {studentNew}')
                    print(f'{studentNew}: {students_marks[studentNew]}')
                    continue
        if sub_command == 2:
            # считываем предмет
            class_ = input('Введите предмет: ').strip().title()
            # проверяем наличие предмета в списке
            if class_ not in classes:
                print('ОШИБКА: Данного предмета нет в журнале')
                continue
            else:
                # получаем новое значение для предмета
                classNew = input('Введите наименование для нового класса: ').strip().title()
                # проверяем наличие нового имени предмета в журнале
                if classNew in classes:
                    print('ОШИБКА: такой предмет уже есть в журнале')
                    print()
                    print(f'Текущий список предметов: {classes}')
                    continue
                else:
                    # выясняем индекс предмета, которого будем менять и присваиваем новое имя по индексу
                    classOld = classes.index(class_)
                    classes[classOld] = classNew
                    for student in students:
                        marks = students_marks[student].pop(class_)
                        students_marks[student][classNew] = marks
                    print(f'Имя предмета изменено. Новое имя {classNew}')
                    print(f'Текущий список предметов: {classes}')
                    continue
    elif command == 6:
        print('6. Удалить оценку')
        # считываем имя ученика
        student = input('Введите имя ученика: ').strip().title()
        # считываем название предмета
        class_ = input('Введите предмет: ').strip().title()
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            marks = students_marks[student][class_]
            # проверяем есть ли вообще оценки у ученика по этому предмету
            if not marks:
                print(f'У ученика {student} ещё нет оценок по предмету {class_}')
                continue
            # выводим все имеющиеся оценки ученика
            print(f'Текущие оценки ученика {student} по предмету {class_}:')
            for i in range(len(marks)):
                print(f'{i + 1}) {marks[i]}')
            # запрашиваем оценку для изменения
            markDel = int(input('Введите порядковый номер оценки для удаления: '))
            # если пользователь ввел несуществующий порядковый номер оценки
            if markDel < 1 or markDel > len(marks):
                print(f'ОШИБКА: оценки с порядковым номером {markDel} нет в списке')
                continue
            else:
                marks.pop(markDel-1)
                print(f'Оценка удалена. Текущие оценки ученика {student}: ')
                # выводим обновленный список оценок ученика по предмету
                print()
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 7:
        print('7. Удалить ученика/предмет')
        sub_command = int(input('''
            Кого вы хотите удалить?
            1. Ученика
            2. Предмет
            Введите команду: '''))
        # удаляем ученика
        if sub_command == 1:
            # считываем имя ученика
            student = input('Введите имя ученика для удаления: ').strip().title()
            # убеждаемся в наличии ученика в списке учеников
            if student not in students:
                print('ОШИБКА: Данного ученика нет в журнале')
                continue
            else:
                students.remove(student)
                print(f'Ученик удален. Текущий список учеников: ')
                # выводим текущий список учеников
                print(students)
        elif sub_command == 2:
            # считываем название предмета
            class_ = input('Введите предмет для удаления: ').strip().title()
            # убеждаемся в наличии класса в списке
            if class_ not in classes:
                print('ОШИБКА: Данного класса нет в журнале')
                continue
            else:
                classes.remove(class_)
                print(f'Предмет удален. Текущий список предметов: ')
                # выводим текущий список учеников
                print(classes)
        else:
            print('ОШИБКА: введенный номер команды некорректный')
    elif command == 8:
        print('8. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # оберегаемся от деления на 0
                if marks_count == 0:
                    print(f"{class_} - нет оценок")
                    continue
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 9:
        print('9. Вывести средний балл по всем предметам для ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ').strip().title()
        # проверяем существует ли такой ученик
        if student in students:
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # оберегаемся от деления на 0
                if marks_count == 0:
                    print(f"{class_} - нет оценок")
                    continue
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
        else:
            print('ОШИБКА: неверное имя ученика')
        print()
    elif command == 10:
        print('10. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 11:
        print('11. Вывести все оценки по ученику')
        # считываем имя ученика
        student = input('Введите имя ученика: ').strip().title()
        # проверяем существует ли такой ученик
        if student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
        else:
            print('ОШИБКА: неверное имя ученика')
        print()
    elif command == 12:
        print('11. Выход из программы')
        break
    elif command == 0:
        print('''
                Список команд:
                0. Вывести список команд
                1. Добавить новый предмет 
                2. Добавить нового ученика 
                3. Добавить оценки ученика по предмету 
                4. Редактировать оценку ученика 
                5. Редактировать ученика/предмет
                6. Удалить оценку 
                7. Удалить ученика/предмет
                8. Вывести средний балл по всем предметам по каждому ученику 
                9. Вывести средний балл по всем предметам для ученика 
                10. Вывести все оценки по всем ученикам 
                11. Вывести все оценки по ученику 
                12. Выход из программы
                ''')