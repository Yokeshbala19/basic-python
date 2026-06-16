num = int(input("enter a number: "))
if num > 1:
    for i in range (2, int(num**0.5)):
        if num % i == 0:
            print("not a prime number :")
            break
    else:
        print("is a prime number :")
else:
    print("not a prime number")

