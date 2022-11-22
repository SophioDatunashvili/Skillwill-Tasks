# First task
# -----------
count = 0
arr = []

# getting input from user and adding to arr(list)
while count < 5:
    element = input("enter string: ")
    count += 1
    arr.append(element)

# calculating maximum length of arr elements
max_length = 0
for element in arr:
    if max_length < len(element):
        max_length = len(element)

print(f"Length of the longest string is {max_length}")


# Second task
# -------------
def max_num(int_list):
    return max(int_list)


# Third task
# ------------
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
