def wc(filename):
    with open(filename, 'r') as f:
        text = f.read()

    number_of_characters = len(text)
    list_of_words = text.split()
    number_of_words = len(list_of_words)
    number_of_lines = text.count('\n')
    return number_of_characters, number_of_words, number_of_lines


def main():
    filename = input("Enter the name of the file: ")
    try:
        chars, words, lines = wc(filename)
        print(f"Characters: {chars}, Words: {words}, Lines: {lines}")
    except FileNotFoundError:
        print(f"File {filename} was not found")


# main()

# from tkinter.filedialog import askopenfilename
# file_name = askopenfilename()
# print(file_name)
