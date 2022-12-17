def dogs_age(age):
    first_two_years = 10.5
    two_and_more_years = 4
    dog_age = 0
    if age <= 2:
        dog_age = age * first_two_years
    else:
        dog_age = 2 * first_two_years + (age - 2) * two_and_more_years
    return dog_age


dog_age_to_count = dogs_age(5)
print(f"Dog age = {dog_age_to_count}")
