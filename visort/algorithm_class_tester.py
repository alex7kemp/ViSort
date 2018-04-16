from algorithm_class import Algorithm_class

def main():
    list1 = [10,9,8,5,6,9,8,9,10,12,15]
    alg = Algorithm_class(list1)
    alg.bubble_visual()
    for each in range(len(alg.bubble_steps)):
        print(alg.bubble_steps[each])
        print(alg.bubble_indices[each])
        print(alg.bubble_pseudo[each])

main()