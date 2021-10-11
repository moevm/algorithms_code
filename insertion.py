def insert(arr):
    for index in range(1, len(arr)):
        current = arr[index]
        sorted_index = index-1
        while sorted_index >= 0 and current < arr[sorted_index]:
            arr[sorted_index+1] = arr[sorted_index]
            sorted_index -= 1
        arr[sorted_index+1] = current
    return arr


arr = list(map(int, input().split()))
print(insert(arr))
