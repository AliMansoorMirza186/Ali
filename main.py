def divide(a, b):
    return a / b if b != 0 else "Error"

def greet_user(user):
    print("Welcome", user.get("name", "Guest"))

def main():
    users = [{"id": 1}, {"name": "Ali"}, {}]
    for user in users:
        greet_user(user)

    print("10 / 0 =", divide(10, 0))

    try:
        result = 100 / int("zero")
    except ValueError:
        print("Caught ValueError")

if __name__ == "__main__":
    main()
