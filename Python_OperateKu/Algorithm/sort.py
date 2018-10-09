#encoding: utf-8

alist = [-2 , 0, 10, 88, 19, 9, 1]
# 从小到大
print(sorted(alist)) # [-2, 0, 1, 9, 10, 19, 88]

# 从大到小
print(sorted(alist, reverse=True)) # [88, 19, 10, 9, 1, 0, -2]

# 将alist按从大到小的顺序排序后输出
alist.sort(reverse=True)
print(alist) #[88, 19, 10, 9, 1, 0, -2]
