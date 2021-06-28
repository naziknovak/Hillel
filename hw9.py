print("Задание 1:")
machine = {'type': 'car', 'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'max_speed': 125.5}
list_ = list(machine.items())
list_[0], list_[-1] = list_[-1], list_[0]
del list_[1]
list_.append(("new_key", "new_value"))
new = dict(list_)
print(new)

print("\nЗадание 2:")
student = {"name": "Emma", "class": 9, "marks": 75}
print(student.get('marks'))

print("\nЗадание 3:")
p = {"name": "Mike", "salary": 8000}
print(p.get("age"))

print("\nЗадание 4:")
sample = {"1":["a","b"], "2":["c","d"]}
for value in sample.get("2"):
    if value == "d":
        print("d")


print("\nЗадание 5:")
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
list_3 = []; dict_ = {}; d = {}
for element in list_1:
    country, *cities = element.split("-")
    for city in cities:
        dict_[city] = country
for city in list_2:
    list_3.append({dict_[city]: city})
    for ell in list_3:
        d.update(ell)
print(d)

print("\nЗадание 6:")
if __name__ == '__main__':
    result = []
    message = input(str())
    keys = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
            'g': 7, 'h': 8, 'i': 9, 'k': 10, 'l': 11, 'm': 12,
            'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
            't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
            'z': 25}
    message = list(message)
    for symbol in message:
        for key in keys:
            if key == symbol:
                result.append(keys[key])
    print(result)

print("\nЗадание 7:")
my_dict = {num : num ** 3 for num in range(1, 11)}
print(my_dict)

print("\nЗадание 8:")
string_ = "Hello,world"
my_dict = {symbol: string_.count(symbol) for symbol in string_}
print(my_dict)

