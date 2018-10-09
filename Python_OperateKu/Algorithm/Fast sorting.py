#encoding: utf-8
# 快速排序
def quick_sort(lists, left, right):
    #递归过程中，发现left和right一致时，停止递归，直接返回列表
    if left >= right:
        return lists
    #定义游标
    low = left
    high = right

    #取参考标志，最左边的元素
    key = lists[low]
    while low < high:
        #从最右侧向左，依次和标志元素对比，如果右侧的元素大于标志元素
        while low < high and lists[high] >= key:
            #右侧减1
            high -= 1
        #否则low赋high值
        lists[low] = lists[high]

        #从最左侧向右，依次和标志元素对比，如果左侧的元素小于标志元素
        while low < high and lists[low] <= key:
            #左侧加1
            low += 1
        #否则high赋low值
        lists[high] = lists[low]

    #最后给high位置赋值
    lists[high] = key

    #处理左侧元素
    quick_sort(lists, left, low - 1)
    #处理右侧元素
    quick_sort(lists, low + 1, right)
    return lists

alist = [0, 10, 88, 19, 9, 1, 7]
print(quick_sort(alist, 0, 6))
