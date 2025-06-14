def divide(a, b):
    return a / b  # ❌ No ZeroDivisionError handling

def greet_user(user):
    print("Welcome", user["name"])  # ❌ KeyError if 'name' missing

def main():
    users = [{"id": 1}, {"name": "Ali"}, {}]
    for user in users:
        greet_user(user)

    print("10 / 0 =", divide(10, 0))  # ❌ Division by zero

    try:
        result = 100 / int("zero")  # ❌ ValueError
    except:
        print("Caught error.")

if __name__ == "__main__":
    main()
