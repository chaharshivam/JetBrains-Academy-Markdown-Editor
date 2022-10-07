file = open("./data/dataset/input.txt", "r")
counter = 0
for line in file:
    line_list = line.split("\n")
    if line_list[0] == "summer":
        counter += 1

print(counter)
file.close()
