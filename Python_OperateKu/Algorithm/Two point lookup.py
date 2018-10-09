# encoding: utf-8

alist = [0, 1, 10, 88, 19, 9, 1]


def binary_search(arr, start, end, hkey):
    if start > end:
        return -1
    mid = start + (end - start) / 2
    if arr[mid] > hkey:
        return binary_search(arr, start, mid - 1, hkey)
    if arr[mid] < hkey:
        return binary_search(arr, mid + 1, end, hkey)
    return mid


alist = sorted(alist)
print(alist)
print binary_search(alist, 0, 6, 9)
