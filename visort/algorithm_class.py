import time
import psutil
import os


class Algorithm_class:

    def __init__(self, myList):
        self.myList = myList

        self.bubble_sorted = []
        self.bubble_steps = [self.myList]
        self.bubble_indices = []
        self.bubble_pseudo = []

        self.quick_sorted = []
        self.quick_steps = [self.myList]
        self.quick_indices = []
        self.quick_pseudo = []
        self.quickcomp = 0 #quick sort is recursive, so I just I didnt' want to mess with it's return statements
        self.quickdata = 0 #quick sort is recursive, so I just I didnt' want to mess with it's return statements

        self.merge_sorted = []
        self.merge_steps = [self.myList]
        self.merge_indices = []
        self.merge_pseudo = []

        self.counting_sorted = []
        self.counting_steps = [self.myList]
        self.counting_indices = []
        self.counting_pseudo = []

        self.insertion_sorted = []
        self.insertion_steps = [self.myList]
        self.insertion_indices = []
        self.insertion_pseudo = []

    def bubble(self):

        self.bubble_sorted = list(self.myList)
        
        for i in range(len(self.bubble_sorted)):
            value = self.bubble_sorted[i]
            location = i
            for j in range(0, len(self.bubble_sorted) - i - 1):
                if self.bubble_sorted[j] > self.bubble_sorted[j + 1]:
                    self.bubble_sorted[location] = self.bubble_sorted[location - 1]
                    self.bubble_sorted[j], self.bubble_sorted[j + 1] = self.bubble_sorted[j + 1], self.bubble_sorted[j]
            self.bubble_sorted[location] = value
        self.bubble_sorted[location] = value

    def bubble_memory(self):
        p = psutil.Process(os.getpid())
        self.bubble()
        return p.memory_info().peak_wset

    def bubble_time(self):
        start = time.start()
        self.bubble()
        stop = time.stop()
        return stop - start

    def bubble_visual(self):
        self.bubble_sorted = list(self.myList)
        self.bubble_indices = list()
        self.bubble_indices.append([0, 0])
        self.bubble_pseudo = list()
        self.bubble_pseudo.append("Unsorted list.")

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
                "Data value " + str(copy_bubble_sorted[index]) + " from position " + str(index) + " inserted at position " + str(
                    location)))

        self.bubble_sorted[location] = value

    def bubble_comparisons(self):
        self.bubble_sorted = list(self.myList)
        data_movements = 0
        comparisons = 0

        for i in range(len(self.bubble_sorted)):
            value = self.bubble_sorted[i]
            location = i
            for j in range(0, len(self.bubble_sorted) - i - 1):
                comparisons += 1
                if self.bubble_sorted[j] > self.bubble_sorted[j + 1]:
                    self.bubble_sorted[location] = self.bubble_sorted[location - 1]
                    data_movements += 1
                    self.bubble_sorted[j], self.bubble_sorted[j + 1] = self.bubble_sorted[j + 1], self.bubble_sorted[j]
            self.bubble_sorted[location] = value
        self.bubble_sorted[location] = value
        
        return (comparisons, data_movements)
        

    def quick(self):
        self.quick_sorted = list(self.myList)
        self.quick_helper(0, len(self.quick_sorted) - 1)

    def quick_helper(self, first, last):
        if first < last:
            splitpoint = self.quick_partition(first, last)

            self.quick_helper(first, splitpoint - 1)
            self.quick_helper(splitpoint + 1, last)

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

        temp = self.quick_sorted[first]
        self.quick_sorted[first] = self.quick_sorted[rightmark]
        self.quick_sorted[rightmark] = temp

        return rightmark

    def quick_memory(self):
        p = psutil.Process(os.getpid())
        self.quick()
        return p.memory_info().peak_wset

    def quick_time(self):
        start = time.start()
        self.quick()
        stop = time.stop()
        return stop - start

    def quick_visual(self):
        self.quick_sorted = list(self.myList)
        self.quick_helper_visual(0, (len(self.quick_sorted) - 1))

    def quick_helper_visual(self, first, last):
        if first < last:
            self.quick_pseudo.append("create a partition")
            splitpoint = self.quick_partition_visual(first, last)

            self.quick_helper_visual(first, splitpoint - 1)
            self.quick_helper_visual(splitpoint + 1, last)
        
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
                self.quick_indices.append([rightmark,leftmark])
                temp = self.quick_sorted[leftmark]
                self.quick_sorted[leftmark] = self.quick_sorted[rightmark]
                self.quick_sorted[rightmark] = temp
                self.quick_steps.append(list(self.quick_sorted))

        self.quick_indices.append([rightmark, first])
        temp = self.quick_sorted[first]
        self.quick_sorted[first] = self.quick_sorted[rightmark]
        self.quick_sorted[rightmark] = temp
        self.quick_steps.append(list(self.quick_sorted))

        return rightmark
    
    def quick_comparisons(self):
        self.quick_sorted = list(self.myList)
        self.quickdata = 0
        self.quickcomp = 0
        self.quick_helper_comparisons(0, len(self.quick_sorted) - 1)
        return  self.quickdata, self.quickcomp
        
    def quick_helper_comparisons(self, first, last):
        self.quickcomp +=1
        if first < last:
            splitpoint = self.quick_partition_comparisons(first, last)

            self.quick_helper_comparisons(first, splitpoint - 1)
            self.quick_helper_comparisons(splitpoint + 1, last)
        
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

        temp = self.quick_sorted[first]
        self.quick_sorted[first] = self.quick_sorted[rightmark]
        self.quick_sorted[rightmark] = temp
        self.quickdata += 1

        return rightmark
        

    def merge(self):
        placeholder = 1

    def merge_memory(self):
        p = psutil.Process(os.getpid())
        self.merge()
        return p.memory_info().peak_wset

    def merge_time(self):
        start = time.start()
        self.merge()
        stop = time.stop()
        return stop - start

    def merge_visual(self):
        placeholder = 1

    def merge_comparisons(self):
        placeholder = 1
        

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

    def counting_memory(self):
        p = psutil.Process(os.getpid())
        self.counting()
        return p.memory_info().peak_wset

    def counting_time(self):
        start = time.start()
        self.counting()
        stop = time.stop()
        return stop - start

    def counting_visual(self):

        changedIndices = [0, 0]
        self.counting_sorted = list(self.myList)  # creating a copy of the list
        maxplus = max(self.counting_sorted) + 1  # this is used to get the correct range of numbers to iterate through
        count = [0] * maxplus  # prefilling count list

        self.counting_pseudo.append("insert pseudocode step 1 here")
        self.counting_steps.append(list(self.counting_sorted))
        self.counting_indices.append(list(changedIndices))

        for number in self.counting_sorted:
            count[number] += 1  # creating count list

            self.counting_pseudo.append("insert pseudocode step 2 here")
            self.counting_steps.append(list(self.counting_sorted))
            self.counting_indices.append(list(changedIndices))

        index = 0
        for value in range(maxplus):

            self.counting_pseudo.append("insert pseudocode step 3 here")
            self.counting_steps.append(list(self.counting_sorted))
            self.counting_indices.append(list(changedIndices))

            for number in range(count[value]):

                self.counting_sorted[index] = value  # actual sorting

                self.counting_pseudo.append("insert pseudocode step 4 here")
                self.counting_steps.append(list(self.counting_sorted))  # creating steps list
                if index > 0:  # creating index list
                    changedIndices = [index - 1, index]
                    self.counting_indices.append(list(changedIndices))
                else:
                    changedIndices = [0, 0]
                    self.counting_indices.append(list(changedIndices))

                index += 1  # this is for iterating through count list

                self.counting_pseudo.append("insert pseudocode step 5 here")
                self.counting_steps.append(list(self.counting_sorted))
                self.counting_indices.append(list(changedIndices))

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
        

    def insertion(self):
        self.insertion_sorted = list(self.myList)

        for index in range(1, len(self.insertion_sorted)):
            value = self.insertion_sorted[index]
            location = index

            while location > 0 and self.insertion_sorted[location - 1] > value:
                self.insertion_sorted[location] = self.insertion_sorted[location - 1]
                location -= 1

            self.insertion_sorted[location] = value
        self.insertion_sorted[location] = value

    def insertion_memory(self):
        p = psutil.Process(os.getpid())
        self.insertion()
        return p.memory_info().peak_wset

    def insertion_time(self):
        start = time.start()
        self.insertion()
        stop = time.stop()
        return stop - start

    def insertion_visual(self):
        self.insertion_sorted = list(self.myList)
        self.insertion_indices = list()
        self.insertion_indices.append([0, 0])
        self.insertion_pseudo = list()
        self.insertion_pseudo.append("Unsorted list.")

        for index in range(1, len(self.insertion_sorted)):
            value = self.insertion_sorted[index]
            location = index
            copy_insertion_sorted = list(self.insertion_sorted)

            while location > 0 and self.insertion_sorted[location - 1] > value:
                self.insertion_sorted[location] = self.insertion_sorted[location - 1]
                location -= 1
                self.insertion_steps.append(list(self.insertion_sorted))
                self.insertion_indices.append([index, location])

            self.insertion_sorted[location] = value

            self.insertion_pseudo.append(str(
                "Data value " + str(copy_insertion_sorted[index]) + " from position " + str(index) + " inserted at position " + str(
                    location)))

        self.insertion_sorted[location] = value

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
