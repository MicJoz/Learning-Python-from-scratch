import random

random_rows = random.randint(5, 15)
random_columns = random.randint(5, 15)
print(f"Wartość zmiennej rows: {random_rows}")
print(f"Wartość zmiennej columns: {random_columns}")

columns_stars = "*" * random_columns

i = 0
while i < random_rows:
    print(columns_stars)
    i += 1
