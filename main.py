def add_numbers(a, b):
    return a + b

def get_user_input():
    a = float(input("first number:"))
    b = float(input("second number:"))
    return a, b

if __name__ == "__main__":
    num1, num2 = get_user_input()
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")