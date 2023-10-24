i = [1, 2, 3, 4, 5, 6, 7]
j = [8, 9, 10, 11, 30, 20, 15, 18, 40]
k = i+j
print(k)
print(len(k))
z = j*3
print(z)
print(sorted(k))
for x in k:
    print(x**2)
k.append(20)
k.sort()
print(k)
i.pop(6)
print(i)
