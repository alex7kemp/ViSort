import time


def insertionSortSteps(stepsList):
    aList = list(stepsList[0])    
    
    for index in range(1, len(aList)):
        value = aList[index]
        location = index

        while location > 0 and aList[location - 1] > value:
            aList[location] = aList[location - 1]
            location -= 1
            
        aList[location] = value
        stepsList.append(list(aList))

    aList[location] = value

def insertionSortTime(aList):
    start = time.clock()
    
    for index in range(1, len(aList)):
        value = aList[index]
        location = index

        while location > 0 and aList[location - 1] > value:
            aList[location] = aList[location - 1]
            location -= 1
            
        aList[location] = value

    aList[location] = value
    
    stop = time.clock()
    return stop-start

def main():
    list1 = [6,5,4,3,2,1]
    list2 = list(list1)
    stepsList = [list1]

    insertionSortSteps(stepsList)    
    
    for array in stepsList:
        for each in array:
            print(each, end = ' ')
        print()

    print(insertionSortTime(list2))
    print(list2)
    
main()
