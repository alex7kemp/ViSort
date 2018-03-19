import time
import copy

def bubble(input_list):
    output_list =[]
    for i in range(len(input_list)):
        for j in range(0, len(input_list)-i-1):
            if input_list[j]>input_list[j+1]:
                output_list.append(copy.deepcopy(input_list))
                input_list[j],input_list[j+1]=input_list[j+1],input_list[j]
    return output_list

def bubble_time_func(input_list):
    start_time = time.clock()
    for i in range(len(input_list)):
        for j in range(0, len(input_list)-i-1):
            if input_list[j]>input_list[j+1]:
                input_list[j],input_list[j+1]=input_list[j+1],input_list[j]
    stop_time = time.clock()
    
    bubble_time = stop_time - start_time
    return bubble_time
    
def main():
    alist = [200, 3, 86, 75, 16, 54, 38, 100]
    print ("Sorted array is "+str(bubble(alist)))
    print ("Time: "+str(bubble_time_func(alist)))
    

main()
    
