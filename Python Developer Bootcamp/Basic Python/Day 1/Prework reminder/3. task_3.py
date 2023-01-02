import random

size = random.randint(3, 9)
print(f"Wielkość choinki: {size}")

rows = ""
for i in range(size):
    rows += "*"
    print(rows)
