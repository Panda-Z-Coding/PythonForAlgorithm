"""

编程拓展课实验作业

时间: 9/18

"""


# ? 1.About the sort
# 1.1 bubble_sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        #? Flag whether this data has been exchanged or not.If it's True which means exchanged.
        swapped = False
        #? After each traversal,the biggest element form this time arr will go to the end.
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  #the exchange grammar in python
                swapped = True
            # if the arr ont exchanged,that means arr already orderly
        if not swapped:
            break
    return arr

# Example use

if __name__ == "__main__":
    print("冒泡排序:")
    U_list = [12,11,56,7,98,77,66]
    print("Original list:", U_list)
    sort_list = bubble_sort(U_list)
    print("sorted list:",sort_list)

# 1.2 堆排序

def heapify(arr, n, i):
    largest = i  # 初始化最大值为根节点
    left = 2 * i + 1  # 左子节点
    right = 2 * i + 2  # 右子节点

    # 如果左子节点比根节点大
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点比当前最大的还大
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根节点
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)  # 递归调用

def heap_sort(arr):
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)

    # 一个个取出元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)

    return arr

# 示例使用
if __name__ == "__main__":
    print("堆排序:")
    sample_list = [12, 11, 13, 5, 6, 7]
    print("原始列表:", sample_list)
    sorted_list = heap_sort(sample_list)
    print("排序后列表:", sorted_list)



# 1.3 插入排序

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 当前待插入的元素
        j = i -1
        # 将arr[i]插入到已排序部分的正确位置
        while j >=0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 移动元素
            j -=1
        arr[j + 1] = key  # 插入

    return arr

# 示例使用
if __name__ == "__main__":
    print("插入排序:")
    sample_list = [31, 41, 59, 26, 41, 58]
    print("原始列表:", sample_list)
    sorted_list = insertion_sort(sample_list)
    print("排序后列表:", sorted_list)


# 1.4 选择排序

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 假设当前索引为最小值
        min_idx = i
        # 在剩下的元素中寻找最小值
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 交换找到的最小值与当前位置的值
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 示例使用
if __name__ == "__main__":
    print("选择排序:")
    sample_list = [64, 25, 12, 22, 11]
    print("原始列表:", sample_list)
    sorted_list = selection_sort(sample_list)
    print("排序后列表:", sorted_list)