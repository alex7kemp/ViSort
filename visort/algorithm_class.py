import time
import psutil
import os

class Algorithm_class:

    def __init__(self, myList):
        self.myList = myList

    def bubble(self):
        placeholder = 1
    def bubble_memory(self):
        p = psutil.Process(os.getpid())
        bubble(list(self.myList))
        return p.memory_info().peak_wset
    def bubble_time(self):
        start = time.start()
        self.bubble()
        stop = time.stop()
        return stop - start
    def bubble_visual(self):
        placeholder = 1
        placeholder = 1
    def bubble_comparisons(self):
        placeholder = 1

    def quick(self):
        placeholder = 1
    def quick_memory(self):
        p = psutil.Process(os.getpid())
        quick(list(self.myList))
        return p.memory_info().peak_wset
    def quick_time(self):
        start = time.start()
        self.quick()
        stop = time.stop()
        return stop - start
    def quick_visual(self):
        placeholder = 1
    def quick_comparisons(self):
        placeholder = 1

    def merge(self):
        placeholder = 1
    def merge_memory(self):
        p = psutil.Process(os.getpid())
        merge(list(self.myList))
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
                self.myList[index] = value
                index += 1
    def counting_memory(self):
        p = psutil.Process(os.getpid())
        counting(list(self.myList))
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
        insertion(list(self.myList))
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