import os

def count_words(text):
    words = text.split()
    return len(words)

def count_lines(text):
    number_of_lines = text.count("\n")
    return number_of_lines

def count_bytes(filename):
    st = os.stat(filename)
    return st.st_size