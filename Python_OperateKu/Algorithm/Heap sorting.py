#encoding: utf-8

def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        print "root %d start %d end %d"%(root, start, end)
        while True:
            child = 2 * root + 1
            #print "child index: %d" % child

            #终止条件，孩子的索引值超过数组最大长度
            if child > end:
                break
            #print "lst child value:%d" % lst[child]

            #确定最大的孩子节点的索引值
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
                #print "child+1 index: %d" % child

            #孩子节点最大值和根节点交换
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                #print "lstroot %d" % lst[root], "lstchild %d" % lst[child]
                root = child
                #print "root %d" % root
            else:
                break

    print("-----------------创建最大堆------------------")
    # 创建最大堆
    print(xrange((len(lst) - 2) // 2, -1, -1))
    for start in xrange((len(lst) - 2) // 2, -1, -1):
        print "---->Loop start %d" % start
        sift_down(start, len(lst) - 1)
        print(lst)

    print("-----------------排序过程------------------")
    # 堆排序
    for end in xrange(len(lst) - 1, 0, -1):
        #首尾交换
        lst[0], lst[end] = lst[end], lst[0]
        #剩余重新堆排序
        sift_down(0, end - 1)
        print(lst)
    return lst


alist = [70, 60, 12, 40, 30, 8, 10]
print(heap_sort(alist))
