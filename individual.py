import sys


def get_student():
    """
        Запросить данные о студенте.
        """
    fio = input("Фамилия и инициалы: ")
    group = input("Номер группы: ")
    score = input("Успеваемость: ")
    score = score.split(' ')
    # Создать словарь.
    return {
        'fio': fio,
        'group': group,
        'score': score,
    }


def display_students(staff):
    """
    Отобразить список студентов.
    """
    # Проверить, что список студентов не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 25
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^25} |'.format(
                "No",
                "Фамилия и инициалы",
                "Номер группы",
                "Успеваемость"
            )
        )
        print(line)

        # Вывести данные о всех студентах.
        for idx, student in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    student.get('fio', ''),
                    student.get('group', 0),
                    '{}'.format(student.get('score', ''))
                )
            )

        print(line)

    else:
        print("Список пуст")


def select_students(staff):
    """
    Выбрать двоечников.
    """
    # Сформировать список студентов.
    result = []
    for student in staff:
        if 2 in list(map(int, student.get('score', ''))):
            result.append(student)

    # Возвратить список выбранных студентов.
    return result


def main():
    """
    Главная функция программы.
    """
    # Список студентов.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте.
            student = get_student()

            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('fio', ''))

        elif command == 'list':
            # Отобразить всех студентов.
            display_students(students)

        elif command.startswith('select '):
            # Выбрать двоечников
            selected = select_students(students)
            # Отобразить выбранных студентов
            display_students(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select двоечники - запросить двоечников;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()