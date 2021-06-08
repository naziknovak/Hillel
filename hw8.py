import math

print("Задача 1:")
list_ = [0] * 100
list_.insert(0, 1)
list_.append(1)
print(list_)

print("\nЗадача 2:")
elements = 45
numbers = []
for number in range(0, elements * 2 + 1, 2):
    numbers.append(number)
print(numbers)

print("\nЗадача 3:")
number = int(input("Введите число: "))
list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
if number in list_:
    print(f"Элемент '{number}' найден в списке {list_}")
else:
    print(f"Элемент '{number}' не найден в списке {list_}")

print("\nЗадача 4:")
numbers = [11, 4, 9, 5]
zero = 0
for number in numbers:
    zero += number
print(f"Сумма чисел {numbers} =", zero)
print(f"Произведение чисел {numbers} =", math.prod(numbers))

print("\nЗадача 5:")
numbers = [15, 72, 14, 42]
print(f'Максимальное число списка {numbers}: ', max(numbers))

print("\nЗадача 6:")
fruits = ['apple', 'banana', 'melon', 'pineapple', 'apple', 'melon', 'melon']
list_ = []
for fruit in fruits:
    if fruits.count(fruit) >= 2:
        list_.append(fruit)
newlist = set(list_)
for word in newlist:
    print(f"Элемент {word} повторяется в списке")

print("\nЗадача 7:")
my_list = [15, 72, 14, 42, 11]
my_result = list()
for number in my_list:
    if number == max(my_list):
        my_result.append(min(my_list))
    elif number == min(my_list):
        my_result.append(max(my_list))
    else:
        my_result.append(number)
print("Оригинальный список: ", my_list)
print("Измененный список: ", my_result)

print("\nЗадача 8:")
fruits = ['apple', 'banana', 'melon', 'pineapple', 'strawberry', 'orange']
print("Оригинальный список: ", fruits)
fruits.reverse()
print("Обратный список: ", fruits)

