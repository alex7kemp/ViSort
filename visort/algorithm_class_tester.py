from algorithm_class import Algorithm_class

def main():
    list1 = [12,12,12,12,21]
    alg = Algorithm_class(list1)
    alg.counting_visual()
    for each in range(len(alg.counting_steps)):
        print(alg.counting_steps[each])
        print(alg.counting_indices[each])
        print(alg.counting_pseudo[each])

main()