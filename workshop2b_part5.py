print("Part 5:")

# (i)
list_one = ['h', 'i', 'j', 'k', 'l']
for i in range(4):
    print(list_one[i])
# Output:
# h
# i
# j
# k

# (ii)
list_two = ['m', 'n', 'o']
for letter in list_two:
    print(letter)
# Output:
# m
# n
# o

# (iii)
list_three = ['p', 'q', 'r', 's']
for index, letter in enumerate(list_three):
    print(f"{index}: {letter}")
# Output:
# 0: p
# 1: q
# 2: r
# 3: s