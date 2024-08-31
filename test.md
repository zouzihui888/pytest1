# <center><font face="仿宋" font color = black>复杂度分析</font>
**1.最好情况复杂度**
即使数组是有序的，代码还是需要遍历整个数组来确认最大值和最小值。即复杂度是O(n)。
**2.最坏情况复杂度**
当数组完全无序时，代码需要遍历整个数组来找到最大值和最小值。即复杂度是O(n)。
**3.平均情况复杂度**
由于算法的时间复杂度不依赖于数组元素的特定顺序，无论数组如何排列，算法都需要遍历每个元素一次。即复杂度是O(n)。
**4.代码**
```
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
```