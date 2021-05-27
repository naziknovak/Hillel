import math

print("Задача №1")
num1 = 13
num2 = 10
if (num1 % 2) == 0:
    print("Нечетное число: {0}".format(num2))
else:
    print("Нечетное число: {0}".format(num1))

print("\nЗадача №2")
num3 = 12
numbers = sorted([num1, num2, num3])
print("Среднее число: ", numbers[1])

print("\nЗадача №3")
x_point = 1
y_point = -1
r_circle = 2

hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)

if hypotenuse <= r_circle:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")

print("\nЗадача №4")
x = int(4)

if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
else:
    y = 2 * abs(x) - 1

print("Значение функции по переданному x равно", y)

print("\nЗадача №5")
print("Наибольшее число: ", numbers[2])

print("\nЗадача №6")
a = 3.0
b = 3.5
c = 3.5

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")

print("\nЗадача №7")
x = int(input("x="))
y = int(input("y="))
print("Четверть координатной плоскости: ")
if x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x > 0 and y < 0:
    print('IV')

print("\nЗадача №8")
print("Частное: ", int(num1 / num2))
quotient = str(num1 / num2)
print("Остаток: ", quotient[2:])

print("\nЗадача №9")
print("Введите коэффициенты для квадратного уравнения:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
