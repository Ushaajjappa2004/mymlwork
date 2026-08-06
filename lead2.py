def find_2_max(arr):
    large = float('-inf')
    s_large = float('-inf')
    for num in arr:
        if num>large:
            s_large = large
            large= num
        elif num>s_large:
            s_large = num
    return s_large
print(find_2_max([3,2,4,6,7,8]))