x = [['1', 'a'], ['2', 'b'], ['3', 'c']]
z = list(zip(*x))
print(z)  # [('1', '2', '3'), ('a', 'b', 'c')]