import time

def quickSortsteps(stepslist):
    alist = list(stepslist[0])
    quickSortHelperSteps(alist,0,len(alist)-1,stepslist)

def quickSortHelperSteps(alist,first,last,stepslist):
    if first<last:
        
        splitpoint = partitionSteps(alist,first,last,stepslist)
        
        quickSortHelperSteps(alist,first,splitpoint-1,stepslist)
        quickSortHelperSteps(alist,splitpoint+1,last,stepslist)

def partitionSteps(alist,first,last,stepslist):
    pivotvalue = alist[first]
    
    leftmark = first+1
    rightmark = last
    
    done = False
    while not done:
        
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
            
        if rightmark < leftmark:
            done = True
        else:
            
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            stepslist.append(list(alist))
            ##print("else", alist)
            
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    stepslist.append(list(alist))
    ##print(alist)
    
    return rightmark

def quickSortTime(alist):
    start = time.clock()
    quickSortHelperTime(alist,0,len(alist)-1)
    stop = time.clock()
    return stop - start

def quickSortHelperTime(alist,first,last):
    if first<last:
        
        splitpoint = partitionTime(alist,first,last)
        
        quickSortHelperTime(alist,first,splitpoint-1)
        quickSortHelperTime(alist,splitpoint+1,last)

def partitionTime(alist,first,last):
    pivotvalue = alist[first]
    
    leftmark = first+1
    rightmark = last
    
    done = False
    while not done:
        
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
            
        if rightmark < leftmark:
            done = True
        else:
            
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    
    return rightmark

def main():
    myList = [9,5,7,6,5,4,3,2,1,0]
    myStepsList = [list(myList)]
    quickSortsteps(myStepsList)
    for each in myStepsList:
        print(each)
    print(myList)
    print("runtime:","%f" % quickSortTime(myList),"\n", myList)
main()
