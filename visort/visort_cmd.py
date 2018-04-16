import sys
from input import Input
from algorithm_class import Algorithm_class

# Command-Line arguments found at https://gist.github.com/dideler/2395703
def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    errors = []
    if argv[0].startswith('-m'):
        temp_str = ""
        try:
            argv = argv[1:]
            if argv[0][0] == "-":
                errors.append("Invalid use of manual input. See instructions.")
            else:
                try:
                    while argv[0][0] != "-":
                        temp_str += argv[0]
                        argv = argv[1:]
                    opts['manual'] = temp_str  # Add key and value to the dictionary.
                except IndexError:
                    errors.append("No algorithm provided. See instructions.")
        except IndexError:
            errors.append("No list provided. Invalid use of manual input. See instructions.")
    elif argv[0].startswith('-f'):
        temp_str = ""
        try:
            argv = argv[1:]
            if argv[0][0] == "-":
                errors.append("Invalid use of file input. See instructions.")
            else:
                try:
                    while argv[0][0] != "-":
                        temp_str += argv[0]
                        argv = argv[1:]
                        if argv[0][0] != "-":
                            temp_str += " "
                    opts['load'] = temp_str  # Add key and value to the dictionary.
                except IndexError:
                    errors.append("No algorithm provided. See instructions.")
        except IndexError:
            errors.append("No file provided. Invalid use of file input. See instructions.")
    elif argv[0].startswith('-r'):
        try:
            argv = argv[1:]
            if argv[0][0] == "-":
                errors.append("Invalid use of randomly generated input. See instructions.")
            else:
                try:
                    opts['generate'] = True
                    opts['size'] = int(argv[0])
                    opts['range_min'] = int(argv[1])
                    opts['range_max'] = int(argv[2])
                except (IndexError, ValueError):
                    errors.append("Invalid use of randomly generated input. See instructions.")
                try:
                    argv = argv[3:]
                    if argv[0][0] != "-":
                        errors.append("")  # Just trying to raise exception if no algorithms were provided
                except IndexError:
                    errors.append("No algorithm provided. See instructions.")
        except IndexError:
            errors.append("No size or range provided. Invalid use of randomly generated input. See instructions.")
    else:
        errors.append("Invalid command structure. See instructions.")
        argv = []
    while argv:  # While there are arguments left to parse...
        if argv[0].startswith('-b'):
            opts["bubble"] = True
            argv = argv[1:]
        elif argv[0].startswith('-c'):
            opts["counting"] = True
            argv = argv[1:]
        elif argv[0].startswith('-i'):
            opts["insertion"] = True
            argv = argv[1:]
        elif argv[0].startswith('-mg'):
            opts["merge"] = True
            argv = argv[1:]
        elif argv[0].startswith('-q'):
            opts["quick"] = True
            argv = argv[1:]
        else:
            errors.append("Invalid command structure. See instructions.")
            argv = []
    return opts, errors


def benchmark():
    algorithm_class = Algorithm_class(input_class.input_list)
    if "bubble" in input_class.alg_types:
        tb = algorithm_class.bubble_time()
        sb = algorithm_class.bubble_memory()
        cb, db = algorithm_class.bubble_comparisons()
        print("========================================")
        print("BUBBLE SORT:")
        print("----------------------------------------")
        print("Time Complexity: " + str(tb))
        print("Space Complexity: " + str(sb))
        print("Comparisons: " + str(cb))
        print("Data Movements: " + str(db))
        print("========================================")
    if "counting" in input_class.alg_types:
        tc = algorithm_class.counting_time()
        sc = algorithm_class.counting_memory()
        cc, dc = algorithm_class.counting_comparisons()
        print("COUNTING SORT:")
        print("----------------------------------------")
        print("Time Complexity: " + str(tc))
        print("Space Complexity: " + str(sc))
        print("Comparisons: " + str(cc))
        print("Data Movements: " + str(dc))
        print("========================================")
    if "insertion" in input_class.alg_types:
        ti = algorithm_class.insertion_time()
        si = algorithm_class.insertion_memory()
        ci, di = algorithm_class.insertion_comparisons()
        print("INSERTION SORT:")
        print("----------------------------------------")
        print("Time Complexity: " + str(ti))
        print("Space Complexity: " + str(si))
        print("Comparisons: " + str(ci))
        print("Data Movements: " + str(di))
        print("========================================")
    if "merge" in input_class.alg_types:
        tm = algorithm_class.merge_time()
        sm = algorithm_class.merge_memory()
        cm, dm = algorithm_class.merge_comparisons()
        print("MERGE SORT:")
        print("----------------------------------------")
        print("Time Complexity: " + str(tm))
        print("Space Complexity: " + str(sm))
        print("Comparisons: " + str(cm))
        print("Data Movements: " + str(dm))
        print("========================================")
    if "quick" in input_class.alg_types:
        tq = algorithm_class.quick_time()
        sq = algorithm_class.quick_memory()
        cq, dq = algorithm_class.quick_comparisons()
        print("QUICK SORT:")
        print("----------------------------------------")
        print("Time Complexity: " + str(tq))
        print("Space Complexity: " + str(sq))
        print("Comparisons: " + str(cq))
        print("Data Movements: " + str(dq))
        print("========================================")
    user_input = input("Rerun (Y/N): ")
    if user_input == "y" or user_input == "Y":
        benchmark()


def algorithm():
    algorithms = []
    if "bubble" in myargs:
        algorithms.append("bubble")
    if "counting" in myargs:
        algorithms.append("counting")
    if "insertion" in myargs:
        algorithms.append("insertion")
    if "merge" in myargs:
        algorithms.append("merge")
    if "quick" in myargs:
        algorithms.append("quick")
    input_class.receive_alg_types(algorithms)
    if not input_class.errors:
        input_class.output_type2 = "benchmark"
        benchmark()
    else:
        error_list.extend(input_class.errors)
        for each_item in error_list:
            print(each_item)


if __name__ == '__main__':
    myargs, error_list = getopts(sys.argv[1:])
    if not error_list:
        input_class = Input()
        if 'manual' in myargs:
            manual_list = myargs['manual']
            input_class.manual(manual_list)
            if not input_class.errors:
                algorithm()
            else:
                error_list.extend(input_class.errors)
                for item in error_list:
                    print(item)
        elif 'load' in myargs:
            file_name = myargs['load']
            file = open(file_name, "r")
            input_class.load(file)
            if not input_class.errors:
                algorithm()
            else:
                error_list.extend(input_class.errors)
                for item in error_list:
                    print(item)
        elif 'generate' in myargs:
            size = myargs['size']
            range_min = myargs['range_min']
            range_max = myargs['range_max']
            if size == 0 or range_max == 0:
                error_list.append("Size and maximum range cannot be 0. Please select larger values.")
                for item in error_list:
                    print(item)
            else:
                input_class.generate(range_min, range_max, size)
                if not input_class.errors:
                    algorithm()
                else:
                    error_list.extend(input_class.errors)
                    for item in error_list:
                        print(item)
        else:
            print(myargs)
            print("Error: No valid input type chosen. See instructions.")
    else:
        for item in error_list:
            print(item)
