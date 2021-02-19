elements = [4, -2, 5, 3, -1 , 1, 0, 5, 2]
print(elements)
for i in range(len(elements)):
    for j in range(i, len(elements)):
        if elements[i] > elements[j]:
            temp = elements[i]
            elements[i] = elements[j]
            elements[j] = temp

print(elements)