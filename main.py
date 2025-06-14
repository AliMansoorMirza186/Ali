

def divide(a, b):
    return a / b  # ❌ Fault: No ZeroDivisionError handling

def greet_user(user):
    print("Welcome", user["name"])  # ❌ Fault: KeyError if 'name' missing

def calculate_discount(price, discount=0.2):
    discounted_price = price - (price * discount)
    return discounted_price

def main():
    users = [
        {"id": 1, "age": 25},
        {"id": 2, "name": "Ali", "age": 30},
        {"id": 3, "name": "Zara"},
        {},  # ❌ Missing keys
    ]

    for user in users:
        greet_user(user)  # ❌ May crash

    prices = [100, 200, 300, "four hundred"]  # ❌ String in numeric list

    for price in prices:
        try:
            print("Discounted price:", calculate_discount(price))
        except TypeError:
            print("❌ Error: Invalid price value:", price)

    print("10 divided by 0 is:", divide(10, 0))  # ❌ Division by zero

    # ❌ Unused variable
    x = 5

    # ❌ Duplicate code
    print("Goodbye Ali")
    print("Goodbye Zara")
    print("Goodbye Ahmed")

    # ❌ Bad practice: bare except
    try:
        result = 100 / int("zero")
    except:
        print("Caught an error but don't know what it was.")

    # ❌ Long function
    def do_everything():
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6
        g = 7
        h = 8
        i = 9
        j = 10
        return a + b + c + d + e + f + g + h + i + j

    print("Result:", do_everything())

if __name__ == "__main__":
    main()
