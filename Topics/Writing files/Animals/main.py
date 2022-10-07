# read animals.txt
animals_file = open("animals.txt", "r", encoding="utf-8")
# and write animals_new.txt
new_animal_file = open("animals_new.txt", "w", encoding="utf-8")
for line in animals_file:
    new_animal_file.write(line.rstrip("\n") + " ")
animals_file.close()
new_animal_file.close()
