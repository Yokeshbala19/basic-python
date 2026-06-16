import string_functions

text = input("Enter a string: ")

print("Reversed String:", string_functions.reverse_string(text))
print("Character Count:", string_functions.count_characters(text))

if string_functions.is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")