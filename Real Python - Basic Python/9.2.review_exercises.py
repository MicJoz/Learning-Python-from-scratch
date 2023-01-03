food = ["rice", "beans"]
food.append("broccoli")
food.extend(["bread", "pizza"])
print(food[0:2])
print(food[-1])
breakfast = "eggs, fruit, orange juice".split(", ")
print(len(breakfast))
lengths = [len(item) for item in breakfast]
print(lengths)
