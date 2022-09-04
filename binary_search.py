def binary_search(arr,element):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == element:
            return f'Element found at index {middle}'
        elif element < arr[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return 'NOT FOUND!'

arr = [10,20,30,40,45,50,55,60,100,1000]
element = 12
print(binary_search(arr,element))