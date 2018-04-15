import time
import psutil
import os


class Algorithm_class:

    def __init__(self, myList):
        self.myList = myList
        
        self.bubble_sorted = []
        self.bubble_steps = [self.myList]
        self.bubble_indices = []
        self.bubble_psuedo = []
        
        self.quick_sorted = []
        self.quick_steps = [self.myList]
        self.quick_indices = []
        self.quick_psuedo = []

        self.merge_sorted = []
        self.merge_steps = [self.myList]
        self.merge_indices = []
        self.merge_psuedo = []

        self.counting_sorted = []
        self.counting_steps = [self.myList]
        self.counting_indices = []
        self.counting_psuedo = []

        self.insertion_sorted = []
        self.insertion_steps = [self.myList]
        self.insertion_indices = []
        self.insertion_psuedo = []

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
        self.quickSortHelper(self.quick_sorted, 0, len(self.quick_sorted) - 1)
        
    def quick_helper(self, first, last):
        if first < last:
            splitpoint = self.quick_partition(self.quick_sorted, first, last)

            self.quick_helper(self.quick_sorted, first, splitpoint - 1)
            self.quick_helper(self.quick_sorted, splitpoint + 1, last)

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
        placeholder = 1
    
    def quick_helper_visual(self, first, last):
        placeholder = 1
        
    def quick_partition_visual(self, first, last):
        placeholder = 1
    
    def quick_comparisons(self):
        placeholder = 1
        
    def quick_helper_comparisons(self, first, last):
        placeholder=1
        
    def quick_partition_comparisons(self, first, last):
        placeholder = 1
        

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
        placeholder = 1

    def counting_comparisons(self):
        placeholder = 1
        

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
