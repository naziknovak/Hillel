print("Задача 1:")
numbers = {1, 2, 3, 4}
set_ = {0, False}
fruits = ['apple', 'orange', 'banana']
enumerateFruits = enumerate(fruits)
print(all(numbers))
print(any(set_))
print(list(enumerateFruits))
print(len(numbers))
print(max(fruits))
print(min(set_))
print(sorted(fruits))
print(sum(numbers))

print("\nЗадача 2:")
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
print(set1.intersection(set2, set3))

print("\nЗадача 3:")
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
print(set1.difference(set2, set3)), print(set2.difference(set1, set3)), print(set3.difference(set2, set1))

print("\nЗадача 4:")
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
print(set1.union(set2, set3))

print("\nЗадача 5:")
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)

print("\nЗадача 6:")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

print("\nЗадача 7:")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))

print("\nЗадача 8:")
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

print("\nЗадача 9:")
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

print("\nЗадача 11:")
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1.intersection(set2))

print("\nЗадача 12:")
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set1.update(set2)
print(set1)

print("\nЗадача 13:")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

