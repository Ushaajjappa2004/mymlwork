def min_val(arr):
    min_val=arr[0]
    for num in arr:
        if num <min_val:
            min_val=num
    return min_val
print(min_val([3,2,4,6,7,8]))
    