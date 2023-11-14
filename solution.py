array_1 = list(map(int, input().split(',')))
array_2 = list(map(int, input().split(',')))
sum_ = (len(array_1) + len(array_2))
x, y = 0, 0
array = [0] * sum_

for i in range(sum_):
    array[i] = min(array_1[x], array_2[y])

    if array_1[x] < array_2[y]:
        x += 1
    elif array_1[x] > array_2[y]:
        y += 1

print(array)