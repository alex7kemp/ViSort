from algorithm_class import Algorithm_class

def main():
    list1 = [10,9,8,5,6,9,8,9,10,12,15]
    alg = Algorithm_class(list1)
    alg.merge_visual()
    print(len(alg.merge_steps),len(alg.merge_indices),len(alg.merge_pseudo))

    for each in range(len(alg.merge_steps)):
        print(alg.merge_steps[each])
        print(alg.merge_indices[each])
        print(alg.merge_pseudo[each])

main()