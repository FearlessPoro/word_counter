#!/usr/bin/python

import argparse
from counters import *



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-c", action="store_true", help="count bytes in file")
    parser.add_argument("-l", action="store_true", help="count lines in file")
    parser.add_argument("-m", action="store_true",  help="count characters in file")
    parser.add_argument("-w", action="store_true", help="count words in file")
    args = parser.parse_args()


    filename = args.filename
    file_with_text = open(filename, "r")
    text = file_with_text.read()
    file_with_text.close()

    print("   ", end="")

    if args.l:
        print(count_lines(text), end=" ")

    if args.w:
        print(count_words(text), end=" ")

    if args.c:
        print(count_bytes(filename), end=" ")

    if args.m and not args.c:
        print(len(text), end=" ")

    if not (args.l or args.w or args.c or args.m):
        print(count_lines(text), end=" ")
        print(count_words(text), end=" ")
        print(count_bytes(filename), end=" ")

    print(filename)
