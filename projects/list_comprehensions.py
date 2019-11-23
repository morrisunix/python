### List comprehension

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = [y for y in a if not y % 2]

print(x)
