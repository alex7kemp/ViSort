def insertionSort(stepsList):
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
    
def insertionSortSteps(stepsList):
    aList = list(stepsList[0])
    indiciesList = list()
    
    for index in range(1, len(aList)):
        value = aList[index]
        location = index

        while location > 0 and aList[location - 1] > value:
            aList[location] = aList[location - 1]
            location -= 1
            indiciesList.append([location, location + 1])
            stepsList.append(aList)
            
            
        aList[location] = value

    aList[location] = value
    print(indiciesList)
    print()
    print(stepsList)
    print()
    return(indiciesList, stepsList)

def insertionSortComparisons(aList):
    data_movements = 0
    comparisons = 0
    
    for index in range(1, len(aList)):
        value = aList[index]
        location = index

        while location > 0 and aList[location - 1] > value:
            aList[location] = aList[location - 1]
            location -= 1
            comparisons += 1
            data_movements += 1
            
            
        aList[location] = value

    aList[location] = value

    return(comparisons, data_movements)
    

def main():
    list1 = [6,5,4,3,2,1]
    list2 = list(list1)
    stepsList = [list1]

    insertionSort(stepsList)
    insertionSortSteps(stepsList) 
    
    for array in stepsList:
        for each in array:
            print(each, end = ' ')
        print()

    print(insertionSortComparisons(list2))
    print(list2)
    
main()
