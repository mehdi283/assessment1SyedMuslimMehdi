def check_even_odd(number):
    if number % 2 == 0:
        return "number is even"
    else:
        return "number is odd"
    
def main():
    enter_number = int(input("Enter your number"))

    
    result = check_even_odd(enter_number)
    print(result)


main()

