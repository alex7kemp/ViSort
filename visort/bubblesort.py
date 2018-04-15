
def bubble(alist):
    data_movements = 0
    comparisons = 0
    
    for i in range(len(alist)):
        value = alist [i]
        location = i
        for j in range(0, len(alist)-i-1):
            if input_list[j]>alist[j+1]:
                alist[location] = alist[location-1]
                comparisons += 1
                data_movements += 1
                alist[j],alist[j+1]=alist[j+1],alist[j]
        alist[location] = value
    alist[location] = value
    return (comparisons, data_movements)

def bubble_steps(stepsList):
    aList = list (stepsList[0])
    indiciesList = list()
    indiciesList.append ([0,0])
    pseudocodeList = list()
    pseudocodeList.append ("Unsorted list.")
    
    for index in range( 1, len( aList ) ):
        value = aList[index]
        location = index
        copyaList = list( aList )

        while location > 0 and aList[location - 1] > value:
            aList[location] = aList[location - 1]
            location -= 1

        aList[location] = value
        stepsList.append( list( aList ) )
        indiciesList.append( [index, location] )
        pseudocodeList.append( str("Data value " + str( copyaList[index] ) + " from position " + str( index ) + " inserted at position " + str(location ) ) )

    aList[location] = value
    print("noflinesofpsuedocode",(len(pseudocodeList)))
    print("executingline",(list(range(len(pseudocodeList)))))
    print("squarecolourpair",(indiciesList))
    print("array",(stepsList))
    print("steps",(len(stepsList)))
    print("squarenumber",(len(aList)))
    #return (len( aList ),indiciesList,stepsList,len( stepsList ),len( pseudocodeList ),list( range( len( pseudocodeList ) ) ))

    
def main():
    alist = [200, 3, 86, 75, 16, 54, 38, 100]
    
    alist2 = list(alist)
    stepsList = [alist]
    print (stepsList)
    bubble(stepsList)
    
main()

    
