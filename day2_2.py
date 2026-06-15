age = int(input("Enter your age: "))
if age > 12:
    if age < 20:
        print("You are a teen.")
    elif age  < 30:
        print("You are a uncle.")
    else:
        print("You are senior citizen.")
else:
    print("You are a child.")