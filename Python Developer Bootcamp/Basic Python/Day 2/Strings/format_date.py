def message(input_dict):
    movie = input_dict.get("movie")
    name = input_dict.get("name")
    role = input_dict.get("role")
    if all([movie, role, name]):
        return f"In {movie}, {name} is a {role}."
    else:
        return None


if __name__ == "__main__":
    input_dict = {
        "name": "Han Solo",
        "role": "smuggler",
        "movie": "Star Wars"
    }
    print(message(input_dict))

    input_dict2 = {
        "name": "Bilbo Baggins",
        "role": "burglar"
    }
    print(message(input_dict2))
