# Homework2
# task1
#-------
with open("numbers.txt") as file:
    lines = file.readlines()[:10]
    maximum = int(lines[0])
    for line in lines:
        if int(line) > maximum:
            maximum = int(line)

with open("numbers.txt", "a") as file:
    file.write(str(maximum))

# task 2
#----------
def min_value(dictionary):
    return min(dictionary.values())

# task3
#---------
def unique_set(file_name):
    set1 = set()
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            set1.add(line)

    return set1