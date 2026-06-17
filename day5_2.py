# import re
# text = "call me at 770-877-0380"
# digits = re.findall(r"\d+", text)
# print(digits)

# update_text = re.sub(r"\d", "X", text)
# print(update_text)


# import re

# def clean_text(text):
#     # Remove punctuation
#     text = re.sub(r"[^\w\s]", "", text)

#     # Remove extra spaces
#     text = " ".join(text.split())

#     # Convert to lowercase
#     return text.lower()

# input_text = " Hello, World.!!! Welcome to Python, Programming..... "
# cleaned_text = clean_text(input_text)

# print("Cleaned Text:", cleaned_text)

# def is_palindrome(text):
#     return text == text[::-1]

# input_text = input("Enter a string: ")

# if is_palindrome(input_text):
#     print(f'"{input_text}" is a palindrome.')
# else:
#     print(f'"{input_text}" is not a palindrome.')


# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0

#     for char in text:
#         if char in vowels:
#             count += 1

#     return count

# string = input("Enter a string: ")
# print("Number of vowels:", count_vowels(string))


# import re

# text = "My email is test@gmail.com"

# emails = re.findall(r'\S+@\S+', text)

# print("Emails found:", emails)


sentence = input("Enter a sentence: ")

words = sentence.split()      # Split sentence into words
reversed_words = words[::-1]  # Reverse the order of words

result = " ".join(reversed_words)

print("Reversed Sentence:", result)