def convert_cel_to_far(cel):
    temp_far = cel * 9 / 5 + 32
    return temp_far


def convert_far_to_cel(far):
    temp_cel = (far - 32) * 5 / 9
    return temp_cel


far = float(input("Enter a temperature in degrees F: "))
print(f"{far:.0f} degrees F = {convert_far_to_cel(far):.2f} degrees C")

cel = float(input("Enter a temperature in degrees C: "))
print(f"{cel:.0f} degrees C = {convert_cel_to_far(cel):.2f} degrees F")
