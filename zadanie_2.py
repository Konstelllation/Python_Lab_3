def cylinder(radius, height):
    def circle():
        print('Площадь полной поверхности цилиндра: ',
              2 * 3.14 * radius * height + 2 * 3.14 * radius ** 2)
    message = input('Какую площадь вы хотите получить: площадь боковой'
                    ' поверхности или полную площадь цилиндра?\n'
                    'Площадь боковой поверхности команда - боковая\n'
                    'Площадь полной поверхности цилинда команда - полная\n'
                    '>>>')
    if message.lower() == 'боковая':
        print('Площадь боковой поверхности: ', 2 * 3.14 * radius * height)
    elif message.lower() == 'полная':
        circle()
    else:
        print('Неизвестная команда')


if __name__ == '__main__':
    radius = int(input('Введите радиус цилиндра: '))
    height = int(input('Введите высоту цилиндра: '))
    cylinder(radius, height)