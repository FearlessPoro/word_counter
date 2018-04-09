# word_counter

# Description
Simple python program emulating wc cmd tool 

# Usage
python3 word_counter.py filename [-cmlw]


# Code review
#### General overview
There is no documentation, but the code is written cleanly, the names of functions are clear and you don't actually need comments to understand what each part of the code does. Classes make code cleaner too, although they seem to divide one task into four very similar tasks for no reason. 

#### Is it working?
Program serves it's intended function, can output number of bytes, lines, chars and words from a file, when specific flags are present. The original WC allows the user to input multiple files to check, this implementation doesn't. That however wasn't really specified in the instruction.

#### Optimization
Program loads whole file into memory at once, which is a disaster waiting to happen, when reading large files.

Each instance of counting is done separately, which means that file can be potentially read 4 times when all flags are present, when all of that could be done while only reading file once. Very poor optimization, which can be pretty apparent when reading large files.

#### Problems and errors
The program won't work on files with names starting like flags, eg. "-lmaa.txt". It will load flags -l and -m, and then attempt to open file "aa.txt". This could have been prevented, if, for example, file names had to be put in quotation marks.

No exception handling in the event of wrong file name. Only exeption handling is done by argparser, which is decent enough for such short program.

The order of outputs is not specified anywhere, and they are not named. Original wc states in help the order of outputs, at least.


