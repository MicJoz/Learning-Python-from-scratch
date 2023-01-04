data = ((1, 2), (3, 4))
total = 0
row = 1
for item in data:
    print(f"Row {row} sum: {sum(item)}")
    row += 1
numbers = [4, 3, 2, 1]
numbers_copy = numbers[:]
numbers.sort()
print(numbers)
print(numbers_copy)