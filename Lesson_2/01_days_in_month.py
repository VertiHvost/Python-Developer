# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

# TODO здесь ваш код
if month == 1:
    print(31)
elif month == 2:
    print(28)
elif month == 3:
    print(31)
elif month == 4:
    print(30)
elif month == 5:
    print(31)
elif month == 6:
    print(30)
elif month == 7:
    print(31)
elif month == 8:
    print(31)
elif month == 9:
    print(30)
elif month == 10:
    print(31)
elif month == 11:
    print(30)
elif month == 12:
    print(31)
else:
    print('В году всего 12 месяцев, введите число от 1 до 12, пожалуйста:)')


# month_of_the_year = ("Январь","Февраль","Март","Май","Апрель","Июнь","Июль","Июнь","Август","Сентябрь","Октябрь","Ноябрь","Декабрь")
# if month < 0:
#     print('В году всго 12 месяцев! Следовательно введите от 1 до 12')
# elif month > 12:а
#     print('В году всго 12 месяцев! Следовательно введите от 1 до 12')
# else:
#     print("Вы ввели номер месяца:", month_of_the_year[month-1])
r=1