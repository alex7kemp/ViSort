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
        placeholder = 1

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
        placeholder = 1

    def bubble_comparisons(self):
        placeholder = 1
        

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
        placeholder = 1

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
        placeholder = 1

    def insertion_comparisons(self):
        placeholder = 1
