with open("mbox-short.txt", "r") as file:
    for line in file:
        line = line.strip()

        pos = line.find("X-DSPAM-Confidence:")
        
        if pos != -1:
            number = line[pos + len("X-DSPAM-Confidence:"):] #Starts slicing immediately after "X-DSPAM-Confidence:" and continues to the end.
            print(float(number))