import time
import psutil
import os

#code for quick, merge, bubble, and insertion adapted from interactivepython.org, counting sort from learntosolveit.com

class Algorithm_class:

    def __init__(self, myList):
        self.myList = myList

        self.bubble_sorted = []
        self.bubble_steps = [self.myList]
        self.bubble_indices = [[0, 0]]
        self.bubble_pseudo = ["Unsorted list."]

        self.quick_sorted = []
        self.quick_steps = [self.myList]
        self.quick_indices = [[0, 0]]
        self.quick_pseudo = ["Unsorted list."]


        self.merge_sorted = []
        self.merge_steps = [self.myList]
        self.merge_indices = [[0, 0]]
        self.merge_pseudo = ["Unsorted list."]

        self.counting_sorted = []
        self.counting_steps = [self.myList]
        self.counting_indices = [[0, 0]]
        self.counting_pseudo = ["Unsorted list."]

        self.insertion_sorted = []
        self.insertion_steps = [self.myList]
        self.insertion_indices = [[0, 0]]
        self.insertion_pseudo = ["Unsorted list."]

    #this function just sorts the list. the sorted list is stored in self.bubble_sorted
    def bubble(self):
        self.bubble_sorted = list(self.myList)

        for index in range(1, len(self.bubble_sorted)):
            value = self.bubble_sorted[index]
            location = index

            while location > 0 and self.bubble_sorted[location - 1] > value:
                self.bubble_sorted[location] = self.bubble_sorted[location - 1]
                location -= 1

            self.bubble_sorted[location] = value
        self.bubble_sorted[location] = value

    #this function returns the amount of bytes used to sort the list
    def bubble_memory(self):
        p = psutil.Process(os.getpid())
        self.bubble()
        return p.memory_info().peak_wset

    #this function returns the amount of time taken to sort the list
    def bubble_time(self):
        start = time.time()
        self.bubble()
        stop = time.time()
        return stop - start

    #this function sorts the list and writes data to the associated steps, indices, and pseduo variables
    def bubble_visual(self):
        self.bubble_sorted = list(self.myList)

        for index in range(1, len(self.bubble_sorted)):
            value = self.bubble_sorted[index]
            location = index
            copy_bubble_sorted = list(self.bubble_sorted)

            while location > 0 and self.bubble_sorted[location - 1] > value:
                self.bubble_sorted[location] = self.bubble_sorted[location - 1]
                location -= 1

            self.bubble_sorted[location] = value
            self.bubble_steps.append(list(self.bubble_sorted))
            self.bubble_indices.append([index, location])
            self.bubble_pseudo.append(str(
                "Data value " + str(copy_bubble_sorted[index]) + " from index " + str(index) + " inserted at index " + str(
                    location)))

        self.bubble_sorted[location] = value

    #this function returns the amount of comparisons and data movements used to sort the list
    def bubble_comparisons(self):
        self.bubble_sorted = list(self.myList)
        data_movements = 0
        comparisons = 0

        self.bubble_sorted = list(self.myList)

        for index in range(1, len(self.bubble_sorted)):
            value = self.bubble_sorted[index]
            location = index
            comparisons += 1

            while location > 0 and self.bubble_sorted[location - 1] > value:
                self.bubble_sorted[location] = self.bubble_sorted[location - 1]
                location -= 1
                data_movements +=1

            self.bubble_sorted[location] = value
        self.bubble_sorted[location] = value
        
        return (comparisons, data_movements)


    #this function just sorts the list. the sorted list is stored in self.quick_sorted
    def quick(self):
        self.quick_sorted = list(self.myList)
        self.quick_helper(0, len(self.quick_sorted) - 1)

    #this is a helper funciton, it shouldn't be used outside this class
    def quick_helper(self, first, last):
        if first < last:
            splitpoint = self.quick_partition(first, last)

            self.quick_helper(first, splitpoint - 1)
            self.quick_helper(splitpoint + 1, last)

    # this is a helper funciton, it shouldn't be used outside this class
    def quick_partition(self, first, last):
        pivotvalue = self.quick_sorted[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and self.quick_sorted[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while self.quick_sorted[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:

                temp = self.quick_sorted[leftmark]
                self.quick_sorted[leftmark] = self.quick_sorted[rightmark]
                self.quick_sorted[rightmark] = temp
        if first != rightmark:
            temp = self.quick_sorted[first]
            self.quick_sorted[first] = self.quick_sorted[rightmark]
            self.quick_sorted[rightmark] = temp

        return rightmark

    # this function returns the amount of bytes taken to sort the list
    def quick_memory(self):
        p = psutil.Process(os.getpid())
        self.quick()
        return p.memory_info().peak_wset

    # this function returns the amount of time taken to sort the list
    def quick_time(self):
        start = time.time()
        self.quick()
        stop = time.time()
        return stop - start

    # this function sorts the list and writes data to the associated steps, indices, and pseduo variables
    def quick_visual(self):
        self.quick_sorted = list(self.myList)
        self.quick_helper_visual(0, (len(self.quick_sorted) - 1))

    # this is a helper funciton, it shouldn't be used outside this class
    def quick_helper_visual(self, first, last):
        if first < last:
            splitpoint = self.quick_partition_visual(first, last)

            self.quick_helper_visual(first, splitpoint - 1)
            self.quick_helper_visual(splitpoint + 1, last)

    # this is a helper funciton, it shouldn't be used outside this class
    def quick_partition_visual(self, first, last):
        pivotvalue = self.quick_sorted[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and self.quick_sorted[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while self.quick_sorted[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True

            else:

                temp = self.quick_sorted[leftmark]
                self.quick_sorted[leftmark] = self.quick_sorted[rightmark]
                self.quick_sorted[rightmark] = temp
                self.quick_indices.append([rightmark, leftmark])
                self.quick_steps.append(list(self.quick_sorted))
                self.quick_pseudo.append("Data value "+str(self.quick_sorted[leftmark])+" at index "+str(rightmark)+" swapped with data value "+str(self.quick_sorted[rightmark])+" at index "+str(leftmark))

        if first != rightmark:
            temp = self.quick_sorted[first]
            self.quick_sorted[first] = self.quick_sorted[rightmark]
            self.quick_sorted[rightmark] = temp
            self.quick_indices.append([rightmark, first])
            self.quick_steps.append(list(self.quick_sorted))
            self.quick_pseudo.append("Data value " + str(self.quick_sorted[first]) + " at index " + str(rightmark) + " swapped with data value " + str(self.quick_sorted[rightmark])+" at index "+str(first))

        return rightmark

    # this function returns the amount of comparisons and data movements used to sort the list
    def quick_comparisons(self):
        self.quick_sorted = list(self.myList)
        self.quickdata = 0
        self.quickcomp = 0
        self.quick_helper_comparisons(0, len(self.quick_sorted) - 1)
        return  self.quickcomp, self.quickdata

    # this is a helper funciton, it shouldn't be used outside this class
    def quick_helper_comparisons(self, first, last):
        self.quickcomp +=1
        if first < last:
            splitpoint = self.quick_partition_comparisons(first, last)

            self.quick_helper_comparisons(first, splitpoint - 1)
            self.quick_helper_comparisons(splitpoint + 1, last)

    # this is a helper funciton, it shouldn't be used outside this class
    def quick_partition_comparisons(self, first, last):
        pivotvalue = self.quick_sorted[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and self.quick_sorted[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
                self.quickcomp += 1

            while self.quick_sorted[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1
                self.quickcomp += 1

            if rightmark < leftmark:
                done = True
                self.quickcomp += 1

            else:

                temp = self.quick_sorted[leftmark]
                self.quick_sorted[leftmark] = self.quick_sorted[rightmark]
                self.quick_sorted[rightmark] = temp
                self.quickdata += 1
        if first != rightmark:
            temp = self.quick_sorted[first]
            self.quick_sorted[first] = self.quick_sorted[rightmark]
            self.quick_sorted[rightmark] = temp
            self.quickdata += 1

        return rightmark


    #this function just sorts the list. the sorted list is stored in self.merge_sorted
    def merge(self):
        self.merge_sorted = list(self.myList)
        self.merge_helper(list(self.merge_sorted))

    # this is a helper funciton, it shouldn't be used outside this class
    def merge_helper(self, paraList):
        if len(paraList) > 1:
            mid = len(paraList) // 2
            lefthalf = paraList[:mid]
            righthalf = paraList[mid:]

            self.merge_helper(lefthalf)
            self.merge_helper(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    paraList[k] = lefthalf[i]
                    self.merge_sorted[k] = lefthalf[i]
                    i = i + 1
                else:
                    paraList[k] = righthalf[j]
                    self.merge_sorted[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                paraList[k] = lefthalf[i]
                self.merge_sorted[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                paraList[k] = righthalf[j]
                self.merge_sorted[k] = righthalf[j]
                j = j + 1
                k = k + 1

    # this function returns the amount of bytes taken to sort the list
    def merge_memory(self):
        p = psutil.Process(os.getpid())
        self.merge()
        return p.memory_info().peak_wset

    # this function returns the amount of time taken to sort the list
    def merge_time(self):
        start = time.time()
        self.merge()
        stop = time.time()
        return stop - start

    # this function sorts the list and writes data to the associated steps, indices, and pseduo variables --- this one only sort of works
    def merge_visual(self):
        self.merge_sorted = list(self.myList)
        self.merge_visual_helper(list(self.merge_sorted))

    # this is a helper funciton, it shouldn't be used outside this class
    def merge_visual_helper(self, paraList):
        if len(paraList) > 1:
            mid = len(paraList) // 2
            lefthalf = paraList[:mid]
            righthalf = paraList[mid:]

            self.merge_visual_helper(lefthalf)
            self.merge_visual_helper(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    paraList[k] = lefthalf[i]
                    self.merge_sorted[k] = lefthalf[i]
                    self.merge_steps.append(list(self.merge_sorted))
                    self.merge_indices.append([k, k])
                    self.merge_pseudo.append(
                        "Data value " + str(lefthalf[i]) + " from index " + str(i) + " in left sublist " + str(
                            lefthalf) + " overwrites data at index " + str(k))
                    i = i + 1
                else:
                    paraList[k] = righthalf[j]
                    self.merge_sorted[k] = righthalf[j]
                    self.merge_steps.append(list(self.merge_sorted))
                    self.merge_indices.append([k, k])
                    self.merge_pseudo.append(
                        "Data value " + str(righthalf[j]) + " from index " + str(j) + " in right sublist " + str(
                            righthalf) + " overwrites data at index " + str(k))
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                paraList[k] = lefthalf[i]
                self.merge_sorted[k] = lefthalf[i]
                self.merge_steps.append(list(self.merge_sorted))
                self.merge_indices.append([k, k])
                self.merge_pseudo.append(
                    "Data value " + str(lefthalf[i]) + " from index " + str(i) + " in left sublist " + str(
                        lefthalf) + " overwrites data at index " + str(k))
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                paraList[k] = righthalf[j]
                self.merge_sorted[k] = righthalf[j]
                self.merge_steps.append(list(self.merge_sorted))
                self.merge_indices.append([k, k])
                self.merge_pseudo.append(
                    "Data value " + str(righthalf[j]) + " from index " + str(j) + " in right sublist " + str(
                        righthalf) + " overwrites data at index " + str(k))
                j = j + 1
                k = k + 1

    # this function returns the amount of comparisons and data movements used to sort the list
    def merge_comparisons(self):
        self.merge_sorted = list(self.myList)
        self.merge_comp = 0
        self.merge_data = 0
        self.merge_comparisons_helper(list(self.merge_sorted))
        return self.merge_comp, self.merge_data

    # this is a helper funciton, it shouldn't be used outside this class
    def merge_comparisons_helper(self, paraList):
        if len(paraList) > 1:
            mid = len(paraList) // 2
            lefthalf = paraList[:mid]
            righthalf = paraList[mid:]

            self.merge_comparisons_helper(lefthalf)
            self.merge_comparisons_helper(righthalf)

            i = 0
            j = 0
            k = 0

            while i < len(lefthalf) and j < len(righthalf):
                self.merge_comp += 1

                if lefthalf[i] < righthalf[j]:
                    paraList[k] = lefthalf[i]
                    self.merge_sorted[k] = lefthalf[i]
                    i = i + 1
                    self.merge_data += 1
                else:
                    paraList[k] = righthalf[j]
                    self.merge_sorted[k] = righthalf[j]
                    j = j + 1
                    self.merge_data += 1
                k = k + 1

            self.merge_comp += 1
            while i < len(lefthalf):
                paraList[k] = lefthalf[i]
                self.merge_sorted[k] = lefthalf[i]
                i = i + 1
                k = k + 1
                self.merge_data += 1
                self.merge_comp += 1

            self.merge_comp += 1
            while j < len(righthalf):
                paraList[k] = righthalf[j]
                self.merge_sorted[k] = righthalf[j]
                j = j + 1
                k = k + 1
                self.merge_data += 1
                self.merge_comp += 1


    # this function just sorts the list. the sorted list is stored in self.counting_sorted
    def counting(self):
        maxplus = max(self.myList) + 1
        count = [0] * maxplus
        for number in self.myList:
            count[number] += 1
        index = 0
        for value in range(maxplus):
            for c in range(count[value]):
                self.counting_sorted[index] = value
                index += 1

    # this function returns the amount of bytes taken to sort the list
    def counting_memory(self):
        p = psutil.Process(os.getpid())
        self.counting()
        return p.memory_info().peak_wset

    def counting_time(self):
        start = time.time()
        self.counting()
        stop = time.time()
        return stop - start

    # this function returns the amount of comparisons and data movements used to sort the list
    def counting_visual(self):

        changedIndices = [0, 0]
        self.counting_sorted = list(self.myList)  # creating a copy of the list
        maxplus = max(self.counting_sorted) + 1  # this is used to get the correct range of numbers to iterate through
        count = [0] * maxplus  # prefilling count list

        # this is for formating the pseudo list nicely
        SUFFIXES = {1: "st", 2: "nd", 3: "rd"}
        suffix = "th"

        for number in self.counting_sorted:
            count[number] += 1  # creating count list

        index = 0
        for value in range(maxplus):
            ordinal = count[value]  #this is for formating the pseudo list nicely

            for number in range(count[value]):

                self.counting_sorted[index] = value  # actual sorting
                self.counting_steps.append(list(self.counting_sorted))  # creating steps list
                if index > 0:  # creating index list
                    changedIndices = [index - 1, index]
                    self.counting_indices.append(list(changedIndices))
                else:
                    changedIndices = [0, 0]
                    self.counting_indices.append(list(changedIndices))

                index += 1  # this is for iterating through count list

                # this is for formating the pseudo list nicely
                if 10 <= ordinal %100 <=20:
                    suffix = "th"
                else:
                    suffix = SUFFIXES.get(ordinal % 10, "th")
                self.counting_pseudo.append(str(ordinal)+suffix+" data value from count index " + str(value) + " inserted at position " + str(index))
                ordinal -= 1

    # this function just sorts the list. the sorted list is stored in self.insertion_sorted
    def counting_comparisons(self):
        comparisons = 0
        data_movements = 0
        maxplus = max(self.myList) + 1
        count = [0] * maxplus
        for number in self.myList:
            count[number] += 1
        index = 0
        for value in range(maxplus):
            for c in range(count[value]):
                self.counting_sorted[index] = value
                index += 1
                comparisons += 1
                data_movements += 1
        return comparisons, data_movements


    # this function just sorts the list. the sorted list is stored in self.insertion_sorted
    def insertion(self):
        self.insertion_sorted = list(self.myList)

        for index in range(1, len(self.insertion_sorted)):
            value = self.insertion_sorted[index]
            location = index
            #print("for, index, value, location", index, value, location)

            while location > 0 and self.insertion_sorted[location - 1] > value:
                self.insertion_sorted[location] = self.insertion_sorted[location - 1]
                location -= 1

            self.insertion_sorted[location] = value

        self.insertion_sorted[location] = value

    # this function returns the amount of bytes taken to sort the list
    def insertion_memory(self):
        p = psutil.Process(os.getpid())
        self.insertion()
        return p.memory_info().peak_wset

    # this function returns the amount of time taken to sort the list
    def insertion_time(self):
        start = time.time()
        self.insertion()
        stop = time.time()
        return stop - start

    # this function sorts the list and writes data to the associated steps, indices, and pseduo variables
    def insertion_visual(self):
        self.insertion_sorted = list(self.myList)
        index1 = 0
        for index in range(1, len(self.insertion_sorted)):
            index1 = index
            value = self.insertion_sorted[index]
            location = index

            while location > 0 and self.insertion_sorted[location - 1] > value:
                self.insertion_sorted[location] = self.insertion_sorted[location - 1]
                location -= 1


            self.insertion_sorted[location] = value
            self.insertion_steps.append(list(self.insertion_sorted))
            self.insertion_indices.append([index, location])
            self.insertion_pseudo.append(str("Data value " + str(self.insertion_sorted[index]) + " from index " + str(
                index) + " inserted at index " + str(location)))


        self.insertion_sorted[location] = value

    # this function returns the amount of comparisons and data movements used to sort the list
    def insertion_comparisons(self):
        data_movements = 0
        comparisons = 0

        for index in range(1, len(self.insertion_sorted)):
            value = self.insertion_sorted[index]
            location = index

            while location > 0 and self.insertion_sorted[location - 1] > value:
                self.insertion_sorted[location] = self.insertion_sorted[location - 1]
                location -= 1
                comparisons += 1
                data_movements += 1

            self.insertion_sorted[location] = value

        self.insertion_sorted[location] = value

        return (comparisons, data_movements)
