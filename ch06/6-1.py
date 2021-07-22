num = int(input())

num_list = []
for _ in range(num):
    temp = int(input())
    num_list.append(temp)


def selection_sort(array):
    for i in range(len(array)):
        max_idx = i
        for j in range(i + 1, len(array)):
            if array[j] > array[max_idx]:
                max_idx = j

        array[i], array[max_idx] = array[max_idx], array[i]
        print(array, max_idx)
    return array

print(selection_sort(num_list))
