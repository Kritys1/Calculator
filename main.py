print("Калькулятор v1")
why = input("Что делаем + или - :")
a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))
if why == "+":
    c = a + b
    print("Результат:" + str(c))
elif why == "-":
    c = a - b
    print("Результат:" + str(c))
else:
    print("Вы ввели не правельный знак")
