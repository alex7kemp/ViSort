#algorithm sourced from interactive python.org
#url: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

def mergeSort (stepsList):
    alist = list (stepsList[0])
    indiciesList = list()
    indiciesList.append([0,0])
    pseudocodeList = list()
    pseudocodeList.append ("Unsorted list.")

    for index in range( 1, len( alist ) ):
        value = alist[index]
        location = index
        copyaList = list( alist )

        while location > 0 and alist[location - 1] > value:
            alist[location] = alist[location - 1]
            location -= 1

        alist[location] = value
        stepsList.append( list( alist ) )
        indiciesList.append( [index, location] )
        pseudocodeList.append( str("Data value " + str( copyaList[index] ) + " from position " + str( index ) + " inserted at position " + str(location ) ) )

    alist[location] = value
    print("noflinesofpsuedocode",(len(pseudocodeList)))
    print("executingline",(list(range(len(pseudocodeList)))))
    print("squarecolourpair",(indiciesList))
    print("array",(stepsList))
    print("steps",(len(stepsList)))
    print("squarenumber",(len(alist)))


    #return (len( aList ),indiciesList,stepsList,len( stepsList ),len( pseudocodeList ),list( range( len( pseudocodeList ) ) ))

def mergeSortComparisons (alist):
    data_movements = 0
    comparisons = 0

    for index in range( 1, len( aList ) ):
        value = aList[index]
        location = index

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                comparisons +=1
                data_movements +=1
                i=i+1
            else:
                alist[k]=righthalf[j]
                comparisons +=1
                data_movements +=1
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            comparisons +=1
            data_movements +=1
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            comparisons +=1
            data_movements +=1
            j=j+1
            k=k+1
        alist[location] = value
    alist[location] = value
    return (comparisons, data_movements)

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    alist2 = list (alist)
    stepsList = [alist]
    print (stepsList)
    mergeSort(stepsList)
main()
