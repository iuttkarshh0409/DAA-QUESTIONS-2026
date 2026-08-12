import os

filename = input("Enter file name: ")
count = 0
total = 0

if os.path.exists(filename):

    with open(filename, "r") as file:

        for line in file:
            line = line.strip()

            pos = line.find("X-DSPAM-Confidence:")

            if pos != -1:
                number = line[pos + len("X-DSPAM-Confidence:"):]
                total = total + float(number)
                count = count + 1

    print("No of lines with X-DSPAM-Confidence:", count)
    print("Average:", total / count)

else:
    print("File not found.")