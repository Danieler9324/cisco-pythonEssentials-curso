my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_numbers = []

for i in my_list:
    if i not in unique_numbers:
        unique_numbers.append(i)

print("La lista con elementos únicos:")
print(unique_numbers)