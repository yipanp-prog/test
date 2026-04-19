#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
冒泡排序算法实现
 author: yipanp-prog
"""


def bubble_sort(arr):
    """
    冒泡排序
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果一轮比较中没有发生交换，说明已经有序，提前结束
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    # 测试用例
    data = [64, 34, 25, 12, 22, 11, 90, 1, 55, 78]
    print(f"排序前: {data}")
    result = bubble_sort(data)
    print(f"排序后: {result}")
