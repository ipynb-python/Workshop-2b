print("Part 2:")

letters = ['a', 'b', 'c', 'D', 'x', 'f', 'g', 'y' ]
# (i)
letters[3] = 'd'
print(letters)
# Output: ['a', 'b', 'c', 'd', 'x', 'f', 'g', 'y']

# (ii)
letters.insert(0, 'z')
print(letters)
# Output: ['z', 'a', 'b', 'c', 'd', 'x', 'f', 'g', 'y']

# (iii)
popped_letter = letters.pop()
print(popped_letter)
# Output: y

# (iv)
print(letters)
# Output: ['z', 'a', 'b', 'c', 'd', 'x', 'f', 'g']

# (v)
letters.append('h')
print(letters)
# Output: ['z', 'a', 'b', 'c', 'd', 'x', 'f', 'g', 'h']

# (vi)
idx = letters.index('x')
print(idx)
# Output: 5

# (vii)
del letters[idx]
print(letters)
# Output: ['z', 'a', 'b', 'c', 'd', 'f', 'g', 'h']

# (viii)
letters.remove('z')
print(letters)
# Output: ['a', 'b', 'c', 'd', 'f', 'g', 'h']