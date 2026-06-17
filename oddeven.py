# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# def display_result(n):
#     result = check_even_odd(n)
#     print(f"{n} is {result}")

# display_result(7)

# word = input("Enter a word: ")

# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

word = input("Enter a word: ")

count = len(word)

print("Number of count", count)

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")