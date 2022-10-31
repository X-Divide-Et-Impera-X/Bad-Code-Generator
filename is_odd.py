n = 100
print("def is_odd(n):",*[f"\tif n == {i}:\n\t\treturn {i%2==0}" for i in range(n)],sep="\n")
