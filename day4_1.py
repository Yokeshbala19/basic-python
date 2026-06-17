# Store student grades in a dictionary
grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 88
}

# Calculate average grade
total = sum(grades.values())
average = total / len(grades)

print("Student Grades:")

for student, grade in grades.items():
    print(student, ":", grade)

print("Average Grade =", average)











# text = input("Enter a sentence: ")

# words = text.split()

# word_count= {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word]  = 1

# print(word_count)








# colours = ("red","green","blue")
# single_item = ("glass",)

# print(colours[0])
# print(colours[1])

# student = {"name":"alice","age":"25","grade":"A"}
# # print(student["name"])
# # print(student["age"])
# student["subject"] = "math"
# del student["grade"]
# student.pop("name")
# print(student)

# student = {"name":"alice","age":"25","grade":"A"}

# for key, value in student.items():
#     print(key, value)
#     a=student.get('name')

# numbers = {1, 2, 3, 4}
# empty_set = 0
# numbers.add(5)
# print(numbers)
# print(type(a))
# print(type(student))

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {5, 6, 7, 1}

# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2-set3)
# print(set2 - set1)

