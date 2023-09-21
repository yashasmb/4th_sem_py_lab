import os.path  # Import the os.path module for working with file paths.
import sys  # Import the sys module for system-related functionality.

# Ask the user to input the filename they want to work with.
fname = input("Enter the filename: ")

# Check if the entered filename exists.
if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)  # Exit the program if the file doesn't exist.

# Open the specified file for reading ("r" mode).
infile = open(fname, "r")

# Ask the user to input the number of lines they want to read from the file.
n = int(input('Enter the number of lines to be read: '))

# Read all lines from the file into a list called 'lineList'.
lineList = infile.readlines()

# Loop through the first 'n' lines of the file and print them with line numbers.
for i in range(n):
    print(i + 1, ":", lineList[i])

# Ask the user to input a word to search for in the file.
word = input("Enter a word: ")

# Initialize a variable 'cnt' to count the occurrences of the word.
cnt = 0

# Loop through each line in 'lineList' and count the occurrences of the word.
for line in lineList:
    cnt += line.count(word)

# Print the count of occurrences of the word in the file.
print("The word", "\"", word, "\"", "appears", cnt, "times in the file")
