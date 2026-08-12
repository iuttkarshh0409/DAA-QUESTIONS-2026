"""
with open("sample.txt", "r") as file:
    for line in file:
        line = line.strip()

        # Get the last word of the line
        last_word = line.split()[-1]

        try:
            number = float(last_word)
            print(number)
        except ValueError:
            pass
"""


#This code snippet reads a text file named "sample.txt" line by line,
#strips any leading or trailing whitespace from each line,
#and attempts to extract the last word of each line.
#It then tries to convert that last word into a float.
#If the conversion is successful, it prints the number; if it fails (due to a ValueError),
#it simply passes without printing anything.

with open("sample.txt", "r") as file:
    for line in file:
        try:
            line = line.strip()
            pos = line.find(">")
            number = line[pos + 1:]
            print(float(number))
        except ValueError:
            pass

#This code snippet reads a text file named "sample.txt" line by line,
#strips any leading or trailing whitespace from each line,
#finds the position of the first occurrence of the colon character (":"),
#and extracts the substring that comes after the colon.
#It then converts that substring into a float and prints the number.