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

       #can't check any files that start with "-[flags]". Program will either not find the file, or worse, give count from
       #from another file, if names are unfortunate enough. Eg: wc "-lmaa.txt" could potentially check file "aa.txt" if it exists, 
       #but it will never check the desired file. More of a problem with argparser than this particular program, but still.
    
    filename = args.filename
    file_with_text = open(filename, "r)
    text = file_with_text.read()
    #reading whole file at once, not lines or a number of bytes, will be a problem if files are bigger than RAM
    file_with_text.close()

    print("   ", end="")

    if args.l:
        print(count_lines(text), end=" ")

    if args.w:
        print(count_words(text), end=" ")

    if args.c:
        print(count_bytes(filename), end=" ")

            #output is pretty ambiguous, can't tell which is the number of lines, which is the number of chars, etc.
            #wc is the same, but it states the order of outputs in help messages.
                          
    if args.m and not args.c:
        print(len(text), end=" ")

    if not (args.l or args.w or args.c or args.m):
        print(count_lines(text), end=" ")
        print(count_words(text), end=" ")
        print(count_bytes(filename), end=" ")
                          
    #this program is pretty poorly optimized, reading the same file potentially 4 times, all of this could easily be done
    #while going through the file once.

    print(filename)
                          
    #can only check one file, original wc works differently, but this wasn't specified in the exercise
