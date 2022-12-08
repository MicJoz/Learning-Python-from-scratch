def invest(amount, rate, years):
    for year in range(1, years + 1):
        growing_amount = (amount * rate) + amount
        print(f"year {year}: ${growing_amount:.2f}")
        amount = growing_amount


amount = float(input("Enter a principal amount in $: "))
rate = float(input("Enter an annual rate of return in %: ")) / 100
years = int(input("Enter a number of years: "))

invest(amount, rate, years)
