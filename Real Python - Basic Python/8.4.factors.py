def finding_factors(value):
    for i in range(1, value + 1):
        if value % i == 0:
            print(f"{i} is a factor of {value}")


positive_int = int(input("Enter a positive integer: "))
finding_factors(positive_int)
