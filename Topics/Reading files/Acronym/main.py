file = open("test.txt", "r")
for line in file:
    print(line[0])
file.close()