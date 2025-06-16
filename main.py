# Faulty Python code for SQA error detection demo

def calculate_area(radius)
    area = 3.14159 * radius ** 2
    return area

def print_area():
    r = input("Enter radius: ")
    area = calculate_area(r)
    print("Area of circle is: " + area)

def find_maximum(numbers):
    max = 0
    for i in range(1, len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    return max

def main()
    values = [5, 3, 9, 1, 6]
    print("Maximum value:", find_maximum(values))
    print_area()

main()
