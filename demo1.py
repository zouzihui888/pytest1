def find_max_min(arr):
    if not arr:  # 检查数组是否为空
       return None, None
    
    max_val = arr[0]
    min_val = arr[0]
    
    for num in arr[1:]:  # 从第二个元素开始遍历
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

arr = [3, 1, 4, 1, 5, 9, 2, 6]
max_val, min_val = find_max_min(arr)
print(f"Max: {max_val}, Min: {min_val}")