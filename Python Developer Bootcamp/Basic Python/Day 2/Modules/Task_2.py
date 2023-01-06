from datetime import timedelta, datetime


def tomorrow():
    return datetime.now() + timedelta(days=1)


if __name__ == "__main__":
    print(tomorrow())
    