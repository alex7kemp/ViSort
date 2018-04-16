from algorithm_class import Algorithm_class

def main():
    list1 = [10,9,8,5,6,9,8,9,10,12,15]
    alg = Algorithm_class(list1)
    alg.quick_visual()
    for each in range(len(alg.quick_steps)):
        print(alg.quick_steps[each])
        print(alg.quick_indices[each])
        print(alg.quick_pseudo[each])

main()