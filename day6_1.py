# try:
#     with open("sample.text", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File Not Found!")


def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split())for line in lines)

            print(f"number of line: {line_count}")
            print(f"number of word: {word_count}")
    except FileNotFoundError:
        print(f"file {filename} not found!")

count_words_and_lines("sample.text")


