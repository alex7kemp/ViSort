import time
import psutil
import os
import copy

# the first index of steps list should contain the list you want to sort
def countingSortSteps(stepsList,indexList,pseudoList):

    changedIndices = [0,0]
    aList = list(stepsList[0]) #creating a copy of the list
    maxplus = max(aList) + 1 #this is used to get the correct range of numbers to iterate through
    count = [0] * maxplus #prefilling count list

    
    pseudoList.append("insert pseudocode step 1 here")
    stepsList.append(list(aList))
    indexList.append(list(changedIndices))
    
    for number in aList:
        count[number] += 1 #creating count list
        
        pseudoList.append("insert pseudocode step 2 here")
        stepsList.append(list(aList))
        indexList.append(list(changedIndices))
    
    index = 0
    for value in range(maxplus):
        
        pseudoList.append("insert pseudocode step 3 here")
        stepsList.append(list(aList))
        indexList.append(list(changedIndices))
        
        for number in range(count[value]):

            aList[index] = value #actual sorting
            
            pseudoList.append("insert pseudocode step 4 here")
            stepsList.append(list(aList))  #creating steps list
            if index > 0:  # creating index list
                changedIndices = [index-1,index]
                indexList.append(list(changedIndices))
            else:
                changedIndices = [0,0]
                indexList.append(list(changedIndices))
                
            index += 1  #this is for iterating through count list
            
            pseudoList.append("insert pseudocode step 5 here")
            stepsList.append(list(aList))
            indexList.append(list(changedIndices))
                
def countingSort(aList):
    
    maxplus = max(aList) + 1
    count = [0] * maxplus
    
    for number in aList:
        count[number] += 1

    index = 0
    for value in range(maxplus):
        for c in range(count[value]): 
            aList[index] = value
            index += 1

def countingSortTime(aList):
    start = time.start()
    countingSort(aList)
    stop = time.stop()
    return stop-start

def countingSortMemory(aList):
    p = psutil.Process(os.getpid())
    countingSort(aList)
    return p.memory_info().peak_wset


