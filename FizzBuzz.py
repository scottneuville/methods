n = int(input("Enter a number: "))
s = ""

for i in range(n):
    if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        s = "FizzBuzz"
    elif (i + 1) % 3 == 0:
        s = "Fizz"
    elif (i + 1) % 5 ==0:
        s = "Buzz"
    else:
        s = i + 1
    print(s)
    i += 1
