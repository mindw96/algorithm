array_1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array_2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array_3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

result = sorted(array_1)
print(result)

array_2.sort()
print(array_2)

def settings(data):
    return data[1]

result_2 = sorted(array_3, key=settings)
print(result_2)
