#Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [1, 4, 5, 7, 9]
key = 7
result = linear_search(arr, key)
print("Element found at index:", result if result != -1 else "Not found")