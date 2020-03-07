num=[67,88,44,33,44,88,77,44]
unique=[]
for n in num:
    if n not in unique:
        unique.append(n)
print(unique)