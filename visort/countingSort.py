import time

def countingSortSteps(stepsList,countList):
    aList = stepsList[0]
    maxplus = max(aList) + 1
    count = [0] * maxplus
    countList.append(list(count))
    
    for number in aList:
        count[number] += 1
        countList.append(list(count))

    
    index = 0
    for value in range(maxplus):
        for number in range(count[value]): 
            aList[index] = value
            stepsList.append(list(aList))
            index += 1

def countingSortTime(aList):
    start = time.clock()
    maxplus = max(aList) + 1
    count = [0] * maxplus
    
    for number in aList:
        count[number] += 1

    
    index = 0
    for value in range(maxplus):
        for c in range(count[value]): 
            aList[index] = value
            index += 1
    stop = time.clock()
    return stop - start


def main():
    mylist = [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1]
    mylist2 = list(mylist)
    stepsList = [mylist]
    countList = []
    countingSortSteps(stepsList, countList)
    
    for each in stepsList:
        print(each)

    for each in countList:
        print(each)

    print()
    print(countingSortTime(mylist2))
    print(mylist2)
main()
