def test_input(message):
    try:
        str_to_int(message)
    except ValueError:
        print('False')


def str_to_int(message):
    i = int(message)
    print_int(i)


def print_int(i):
    print(i)


def get_input():
    message = input('Введите строку: ')
    test_input(message)


if __name__ == '__main__':
    while True:
        get_input()