for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0 and numbers % 13 == 0:
        print("FizzFezzBuzz")
    elif numbers % 3 == 0 and numbers % 7 == 0 and numbers % 13 == 0:
        print("FizzFezzBang")
    elif numbers % 5 == 0 and numbers % 7 == 0 and numbers % 13 == 0:
        print("FezzBuzzBang")
    elif numbers % 7 == 0 and numbers % 11 == 0 and numbers % 13 == 0:
        print("FezzBangBong")
    elif numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0 and numbers % 7 == 0:
        print("FizzBang")
    elif numbers % 3 == 0 and numbers % 13 == 0:
        print("FizzFezz")
    elif numbers % 5 == 0 and numbers % 7 == 0:
        print("BuzzBang")
    elif numbers % 5 == 0 and numbers % 13 == 0:
        print("FezzBuzz")
    elif numbers % 7 == 0 and numbers % 13 == 0:
        print("FezzBang")
    elif numbers % 11 == 0 and numbers % 13 == 0:
        print("FezzBong")
    elif numbers % 13 == 0:
        print("Fezz")
    elif numbers % 11 == 0:
        print("Bong")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    elif numbers % 7 == 0:
        print("Bang")
    else:
        print(numbers)