print("Задача 1:")
numbers = [5, 7, 14, 22]
zero = 0
for number in numbers:
    zero += number
print(f"Сумма чисел {numbers} =", zero)

print("\nЗадача 2:")
fruits = ['banana', 'apple', 'orange']
symbol = 'a'
for fruit in fruits:
    print(f"Символ '{symbol}' встречается "
          f"{fruit.count(symbol)} раз(а) в слове {fruit}")

print("\nЗадача 3:")
number = int(input("Введите число: "))
list_= [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
if number in list_:
    print(f"Элемент '{number}' найден в списке")
else:
    print(f"Элемент '{number}' не найден в списке")