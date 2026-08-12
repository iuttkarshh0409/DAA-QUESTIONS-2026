wordList = []

with open("romeo.txt", "r") as file:
    for line in file:
        line = line.strip()
        split_contents = line.split()

        for word in split_contents:
            if word not in wordList:
                wordList.append(word)

wordList.sort()
print(wordList)