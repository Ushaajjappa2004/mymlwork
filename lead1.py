def find_max(arr):
    max_val= arr[0]
    for num in arr:
        if num>max_val:
            max_val=num
    return max_val
print(find_max([3,9,5,6,7,8]))