n = 100
print(f'for i in range({n}):')
for i in range(n): print(f'\tif i == {i}:\n\t\tprint(',"\"fizzbuzz\"" if i % 15 == 0 else "\"fizz\"" if i % 3 == 0 else "\"buzz\"" if i % 5 == 0 else i,')',sep='')
