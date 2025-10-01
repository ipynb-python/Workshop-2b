print("Part 3:")
letters = ['f', 'g', 'd', 'c', 'e', 'a', 'b']
# (i)
print(len(letters))
# Output: 7

# (ii)
letters.reverse()
print(letters)
# Output: ['b', 'a', 'e', 'c', 'd', 'g', 'f']

# (iii)
print(sorted(letters))
# Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# (iv)
print(letters)
# Output: ['b', 'a', 'e', 'c', 'd', 'g', 'f']

# (v)
letters.sort(reverse=True)
print(letters)
# Output: ['g', 'f', 'e', 'd', 'c', 'b', 'a']