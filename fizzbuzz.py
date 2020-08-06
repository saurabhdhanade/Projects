n = int(input("Enter range at which you want FizzBuzz: ")) +1
for number in range(1,n):
    if number % 3 ==0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)
