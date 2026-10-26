
def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

numbers = [12, 5, 8, 20, 3, 15]

print("Original Array:", numbers)
print("Sorted Array:", insertion_sort_descending(numbers))