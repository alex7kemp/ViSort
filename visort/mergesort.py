import time

def merge_sort_helper(alist, first, last):
    if first < last:
        midpoint = (first + last) // 2
        merge_sort_helper(alist, first, midpoint)
        merge_sort_helper(alist, midpoint + 1, last)
        merge_partition(alist, first, midpoint, last)

def merge_partition(alist, first, midpoint, last):
    n1 = midpoint - first + 1
    n2 = last - midpoint
    right= []
    left = []
    for i in range(n1):
        left.append(alist[first + i])
    for j in range(n2):
        right.append(alist[midpoint + j + 1])
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(first, last + 1):
        if left[i] <= right[j]:
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
    return alist

def merge_visual (alist):
    stepsList = list(alist)
    merge_helper_visual (alist, 0, (len(stepsList)-1))

def merge_helper_visual(alist, first, last):
    if first < last:
        midpoint = (first + last) // 2
        merge_helper_visual(alist, first, midpoint)
        merge_helper_visual(alist, midpoint + 1, last)
        merge_partition_visual(alist, first, midpoint, last)

def merge_partition_visual(alist, first, midpoint, last):
    stepsList = list (alist[0])
    indiciesList = list()
    indiciesList.append([0,0])
    pseudoList = list()
    pseudoList.append ("Unsorted list.")
    n1 = midpoint - first + 1
    n2 = last - midpoint
    right= []
    left = []
    for i in range(n1):
        left.append(alist[first + i])
    for j in range(n2):
        right.append(alist[midpoint + j + 1])
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(first, last + 1):
        copyList = list (alist)
        if left[i] <= right[j]:
            alist[k] = left[i]
            indiciesList.append([k,i])
            
            i += 1
        else:
            alist[k] = right[j]
            indiciesList.append([k,j])
            j += 1
    return alist
    
def merge_comparisons (alist):
    stepsList = list (alist)
    data_movements = 0
    comparisons = 0
    merge_helper_comparisons (alist, 0, len(alist)-1)
    return (comparisons, data_movements)

def merge_helper_comparisons (alist, first, last):
    comparisons +=1
    if first < last:
        midpoint = (first + last) // 2
        merge_helper_comparisons(alist, first, midpoint)
        merge_helper_comparisons(alist, midpoint + 1, last)
        merge_partition_comparisons(alist, first, midpoint, last)

def merge_partition_comparisons(alist, first, midpoint, last):
    n1 = midpoint - first + 1
    n2 = last - midpoint
    right= []
    left = []
    for i in range(n1):
        left.append(alist[first + i])
    for j in range(n2):
        right.append(alist[midpoint + j + 1])
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(first, last + 1):
        if left[i] <= right[j]:
            comparisons +=1
            alist[k] = left[i]
            data_movements +=1
            i += 1
        else:
            comparisons +=1
            alist[k] = right[j]
            data_movements += 1
            j += 1
    return alist

def main():
    list1 = [25, 42, 14, 57, 111, 3, 72, 96]
    list2 = list (list1)
    stepsList = list(list1)
    merge_sort_helper(list1, 0, len(list1) - 1)
    print (list1)
    print (stepsList)
main()
