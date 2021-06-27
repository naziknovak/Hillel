print("Задача 1:")
list_dict = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
result = [(key['color'], key['value']) for key in list_dict]
print(result)

print("\nЗадача 2:")
a_dictionary = {"a": 1, "b": 2, "c": 3}
tuple_ = tuple(a_dictionary.items())
print(tuple_)

print("\nЗадача 3:")
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = [(x,y) for x,y in zip(list_a,list_b)]
print(list_c)

print("\nЗадача 4:")
dict_ = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
list_ = list(dict_.items())
list_new = list_[0:3]
tuple_ = tuple(list_new)
print(tuple_)

print("\nЗадача 5:")
list_ = ["bar", "baz", "qux", "etc"]
list_.insert(0, "foo")
tuple_ = tuple(list_)
print(tuple_)

