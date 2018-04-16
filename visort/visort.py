import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from input import Input
from algorithm_class import Algorithm_class

app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file , visort.py

app.config.update(dict(
    SECRET_KEY='development key',
))
app.config.from_envvar('VISORT_SETTINGS', silent=True)

input_class = Input()
global algorithm_class
algorithm_class = 0


@app.route('/')
def enter_list():
    errors = []
    data = {}
    return render_template('enter_list.html', error=errors, entries=data)


@app.route('/add_list', methods=['POST', 'GET'])
def add_list():
    errors = []
    input_class.errors = []
    data = {}
    if request.method == 'POST':
        if request.form.get('enter_list') == "manual":
            manual_list = request.form.get('manual_list')
            if not manual_list:
                errors.append("Empty list. Please type in a list.")
                data.update(
                    {'enter_list': request.form.get('enter_list'), 'manual_list': request.form.get('manual_list'),
                     'file_name': request.form.get('file_name'), 'size': request.form.get('size'),
                     'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max')})
                return render_template('enter_list.html', error=errors, entries=data)

            else:
                input_class.manual(manual_list)
                if not input_class.errors:
                    input_class.analyze_list()
                    if input_class.output_type == "benchmark":
                        data.update(
                            {'enter_list': request.form.get('enter_list'),
                             'manual_list': request.form.get('manual_list'),
                             'benchmark': 'true', 'list': input_class.input_list}
                        )
                    else:
                        data.update(
                            {'enter_list': request.form.get('enter_list'),
                             'manual_list': request.form.get('manual_list'),
                             'benchmark': 'false', 'list': input_class.input_list}
                        )
                    return render_template('enter_algorithm.html', error=errors, entries=data)
                else:
                    errors.extend(input_class.errors)
                    data.update(
                        {'enter_list': request.form.get('enter_list'), 'manual_list': request.form.get('manual_list'),
                         'file_name': request.form.get('file_name'), 'size': request.form.get('size'),
                         'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max')})
                    return render_template('enter_list.html', error=errors, entries=data)

        elif request.form.get('enter_list') == "load":
            file_name = request.form.get('file_name')
            file = request.files['file_name']
            if not file:
                errors.append("No list selected. Please select a list.")
                data.update(
                    {'enter_list': request.form.get('enter_list'), 'manual_list': request.form.get('manual_list'),
                     'file_name': request.form.get('file_name'), 'size': request.form.get('size'),
                     'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max')})
                return render_template('enter_list.html', error=errors, entries=data)
            else:
                file = request.files['file_name']
                input_class.load(file)
                if not input_class.errors:
                    input_class.analyze_list()
                    if input_class.output_type == "benchmark":
                        data.update(
                            {'enter_list': request.form.get('enter_list'), 'file_name': request.form.get('file_name'),
                             'benchmark': 'true', 'list': input_class.input_list}
                        )
                    else:
                        data.update(
                            {'enter_list': request.form.get('enter_list'), 'file_name': request.form.get('file_name'),
                             'benchmark': 'false', 'list': input_class.input_list}
                        )
                    return render_template('enter_algorithm.html', error=errors, entries=data)
                else:
                    errors.extend(input_class.errors)
                    data.update(
                        {'enter_list': request.form.get('enter_list'), 'manual_list': request.form.get('manual_list'),
                         'file_name': file_name, 'size': request.form.get('size'),
                         'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max')})
                    return render_template('enter_list.html', error=errors, entries=data)
        elif request.form.get('enter_list') == "generate":
            size = int(request.form.get('size'))
            range_min = int(request.form.get('range_min'))
            range_max = int(request.form.get('range_max'))
            if size == 0 or range_max == 0:
                errors.append("Size and maximum range cannot be 0. Please select larger values.")
                data.update(
                    {'enter_list': request.form.get('enter_list'), 'manual_list': request.form.get('manual_list'),
                     'file_name': request.form.get('file_name'), 'size': request.form.get('size'),
                     'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max')})
                return render_template('enter_list.html', error=errors, entries=data)
            else:
                input_class.generate(range_min, range_max, size)
                if not input_class.errors:
                    input_class.analyze_list()
                    if input_class.output_type == "benchmark":
                        data.update(
                            {'enter_list': request.form.get('enter_list'), 'size': request.form.get('size'),
                             'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max'),
                             'benchmark': 'true', 'list': input_class.input_list}
                        )
                    else:
                        data.update(
                            {'enter_list': request.form.get('enter_list'), 'size': request.form.get('size'),
                             'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max'),
                             'benchmark': 'false', 'list': input_class.input_list}
                        )
                    return render_template('enter_algorithm.html', error=errors, entries=data)
                else:
                    errors.extend(input_class.errors)
                    data.update(
                        {'enter_list': request.form.get('enter_list'), 'manual_list': request.form.get('manual_list'),
                         'file_name': request.form.get('file_name'), 'size': request.form.get('size'),
                         'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max')})
                    return render_template('enter_list.html', error=errors, entries=data)
        else:
            errors.append("Please select the method you are using to enter a list.")
            data.update({'enter_list': request.form.get('enter_list'), 'manual_list': request.form.get('manual_list'),
                         'file_name': request.form.get('file_name'), 'size': request.form.get('size'),
                         'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max')})
            return render_template('enter_list.html', error=errors, entries=data)
    else:
        return render_template('enter_list.html', error=errors, entries=data)


@app.route('/add_algorithm', methods=['POST', 'GET'])
def add_algorithm():
    errors = []
    input_class.errors = []
    data = {}
    if request.method == 'POST':
        global algorithm_class
        if request.form.get('benchmark') == "benchmark":
            algorithms = []
            if request.form.get('algorithm1') == "bubble":
                algorithms.append("bubble")
            if request.form.get('algorithm2') == "counting":
                algorithms.append("counting")
            if request.form.get('algorithm3') == "insertion":
                algorithms.append("insertion")
            if request.form.get('algorithm4') == "merge":
                algorithms.append("merge")
            if request.form.get('algorithm5') == "quick":
                algorithms.append("quick")
            input_class.receive_alg_types(algorithms)
            if not input_class.errors:
                input_class.output_type2 = "benchmark"
                data.update({'algorithms': input_class.alg_types, 'list': input_class.input_list})
                algorithm_class = Algorithm_class(input_class.input_list)
                if "bubble" in input_class.alg_types:
                    tb = algorithm_class.bubble_time()
                    sb = algorithm_class.bubble_memory()
                    cb, db = algorithm_class.bubble_comparisons()
                else:
                    tb = 0
                    sb = 0
                    cb = 0
                    db = 0
                if "counting" in input_class.alg_types:
                    tc = algorithm_class.counting_time()
                    sc = algorithm_class.counting_memory()
                    cc, dc = algorithm_class.counting_comparisons()
                else:
                    tc = 0
                    sc = 0
                    cc = 0
                    dc = 0
                if "insertion" in input_class.alg_types:
                    ti = algorithm_class.insertion_time()
                    si = algorithm_class.insertion_memory()
                    ci, di = algorithm_class.insertion_comparisons()
                else:
                    ti = 0
                    si = 0
                    ci = 0
                    di = 0
                if "merge" in input_class.alg_types:
                    tm = algorithm_class.merge_time()
                    sm = algorithm_class.merge_memory()
                    cm, dm = algorithm_class.merge_comparisons()
                else:
                    tm = 0
                    sm = 0
                    cm = 0
                    dm = 0
                if "quick" in input_class.alg_types:
                    tq = algorithm_class.quick_time()
                    sq = algorithm_class.quick_memory()
                    cq, dq = algorithm_class.quick_comparisons()
                else:
                    tq = 0
                    sq = 0
                    cq = 0
                    dq = 0
                return render_template('benchmark.html', error=errors, entries=data, tb=tb, tc=tc, ti=ti, tq=tq, tm=tm,
                                       sb=sb, sc=sc, si=si, sq=sq, sm=sm, cb=cb, cc=cc, ci=ci, cq=cq, cm=cm, db=db,
                                       dc=dc, di=di, dq=dq, dm=dm)
            else:
                errors.extend(input_class.errors)
                data.update(
                    {'algorithm1': request.form.get('algorithm1'), 'algorithm2': request.form.get('algorithm2'),
                     'algorithm3': request.form.get('algorithm3'), 'algorithm4': request.form.get('algorithm4'),
                     'algorithm5': request.form.get('algorithm5'), 'benchmark': request.form.get('benchmark'),
                     'list': input_class.input_list})
                return render_template('enter_algorithm.html', error=errors, entries=data)
        else:
            algorithms = []
            if request.form.get('algorithm1') == "bubble":
                algorithms.append("bubble")
            if request.form.get('algorithm2') == "counting":
                algorithms.append("counting")
            if request.form.get('algorithm3') == "insertion":
                algorithms.append("insertion")
            if request.form.get('algorithm4') == "merge":
                algorithms.append("merge")
            if request.form.get('algorithm5') == "quick":
                algorithms.append("quick")
            if input_class.output_type == "benchmark":
                errors.append("Benchmark must be selected if list is greater than 120 elements or if any element is 10000 or larger.")
                data.update(
                    {'algorithm1': request.form.get('algorithm1'), 'algorithm2': request.form.get('algorithm2'),
                     'algorithm3': request.form.get('algorithm3'), 'algorithm4': request.form.get('algorithm4'),
                     'algorithm5': request.form.get('algorithm5'), 'benchmark': request.form.get('benchmark'),
                     'list': input_class.input_list})
                return render_template('enter_algorithm.html', error=errors, entries=data)
            else:
                input_class.receive_alg_types(algorithms)
                if not input_class.errors:
                    if input_class.output_type2 == "benchmark":
                        errors.append("Benchmark must be selected if running more than one algorithm.")
                        data.update(
                            {'algorithm1': request.form.get('algorithm1'), 'algorithm2': request.form.get('algorithm2'),
                             'algorithm3': request.form.get('algorithm3'), 'algorithm4': request.form.get('algorithm4'),
                             'algorithm5': request.form.get('algorithm5'), 'benchmark': request.form.get('benchmark'),
                             'list': input_class.input_list})
                        return render_template('enter_algorithm.html', error=errors, entries=data)
                    else:
                        data.update({'algorithms': input_class.alg_types, 'list': input_class.input_list})
                        algorithm_class = Algorithm_class(input_class.input_list)
                        if "bubble" in input_class.alg_types:
                            algorithm_class.bubble_visual()
                            noflinesofpsuedocode = 4  # Length of pseudocode list
                            squarecolourpair = algorithm_class.bubble_indices  # List of the selected indices
                            array = algorithm_class.bubble_steps  # Steps array
                            steps = len(algorithm_class.bubble_steps)  # Total number of lists in steps array
                            squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
                            pseudocode = algorithm_class.bubble_pseudo  # Pseudocode array
                            algorithmnumber = 0
                        elif "counting" in input_class.alg_types:
                            algorithm_class.counting_visual()
                            noflinesofpsuedocode = 9  # Length of psuedocode list
                            squarecolourpair = algorithm_class.counting_indices  # List of the selected indices
                            array = algorithm_class.counting_steps  # Steps array
                            steps = len(algorithm_class.counting_steps)  # Total number of lists in steps array
                            squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
                            pseudocode = algorithm_class.counting_pseudo  # Pseudocode array
                            algorithmnumber = 1
                        elif "insertion" in input_class.alg_types:
                            algorithm_class.insertion_visual()
                            noflinesofpsuedocode = 8  # Length of psuedocode list
                            squarecolourpair = algorithm_class.insertion_indices  # List of the selected indices
                            array = algorithm_class.insertion_steps  # Steps array
                            steps = len(algorithm_class.insertion_steps)  # Total number of lists in steps array
                            squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
                            pseudocode = algorithm_class.insertion_pseudo  # Pseudocode array
                            algorithmnumber = 2
                        elif "merge" in input_class.alg_types:
                            algorithm_class.merge_visual()
                            noflinesofpsuedocode = 24  # Length of psuedocode list
                            squarecolourpair = algorithm_class.merge_indices  # List of the selected indices
                            array = algorithm_class.merge_steps  # Steps array
                            steps = len(algorithm_class.merge_steps)  # Total number of lists in steps array
                            squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
                            pseudocode = algorithm_class.merge_pseudo  # Pseudocode array
                            algorithmnumber = 3
                        elif "quick" in input_class.alg_types:
                            algorithm_class.quick_visual()
                            noflinesofpsuedocode = 21  # Length of psuedocode list
                            squarecolourpair = algorithm_class.quick_indices  # List of the selected indices
                            array = algorithm_class.quick_steps  # Steps array
                            steps = len(algorithm_class.quick_steps)  # Total number of lists in steps array
                            squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
                            pseudocode = algorithm_class.quick_pseudo  # Pseudocode array
                            algorithmnumber = 4
                        return render_template('visualize.html', error=errors, entries=data, squarenumber=squarenumber,
                                               squarecolourpair=squarecolourpair, array=array,
                                               steps=steps, noflinesofpsuedocode=noflinesofpsuedocode,
                                               algorithmnumber=algorithmnumber, pseudocode=pseudocode)
                else:
                    errors.extend(input_class.errors)
                    data.update(
                        {'algorithm1': request.form.get('algorithm1'), 'algorithm2': request.form.get('algorithm2'),
                         'algorithm3': request.form.get('algorithm3'), 'algorithm4': request.form.get('algorithm4'),
                         'algorithm5': request.form.get('algorithm5'), 'benchmark': request.form.get('benchmark'),
                         'list': input_class.input_list})
                    return render_template('enter_algorithm.html', error=errors, entries=data)
    else:
        if input_class.output_type == "benchmark":
            data.update(
                {'benchmark': 'true', 'list': input_class.input_list}
            )
        else:
            data.update(
                {'benchmark': 'false', 'list': input_class.input_list}
            )
        return render_template('enter_algorithm.html', error=errors, entries=data)

@app.route('/visualize', methods=['GET'])
def visualize():
    errors = []
    data = {}
    data.update({'algorithms': input_class.alg_types, 'list': input_class.input_list})
    algorithm_class = Algorithm_class(input_class.input_list)
    if "bubble" in input_class.alg_types:
        algorithm_class.bubble_visual()
        noflinesofpsuedocode = len(algorithm_class.bubble_pseudo)  # Length of pseudocode list
        executingline = []  # Order of execution for psuedocode list
        for x in range(0, noflinesofpsuedocode):
            executingline.append(x)
        squarecolourpair = algorithm_class.bubble_indices  # List of the selected indices
        array = algorithm_class.bubble_steps  # Steps array
        steps = len(algorithm_class.bubble_steps)  # Total number of lists in steps array
        squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
        pseudocode = algorithm_class.bubble_pseudo  # Pseudocode array
    elif "counting" in input_class.alg_types:
        algorithm_class.counting_visual()
        noflinesofpsuedocode = len(algorithm_class.counting_pseudo)  # Length of psuedocode list
        executingline = []  # Order of execution for psuedocode list
        for x in range(0, noflinesofpsuedocode):
            executingline.append(x)
        squarecolourpair = algorithm_class.counting_indices  # List of the selected indices
        array = algorithm_class.counting_steps  # Steps array
        steps = len(algorithm_class.counting_steps)  # Total number of lists in steps array
        squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
        pseudocode = algorithm_class.counting_pseudo  # Pseudocode array
    elif "insertion" in input_class.alg_types:
        algorithm_class.insertion_visual()
        noflinesofpsuedocode = len(algorithm_class.insertion_pseudo)  # Length of psuedocode list
        executingline = []  # Order of execution for psuedocode list
        for x in range(0, noflinesofpsuedocode):
            executingline.append(x)
        squarecolourpair = algorithm_class.insertion_indices  # List of the selected indices
        array = algorithm_class.insertion_steps  # Steps array
        steps = len(algorithm_class.insertion_steps)  # Total number of lists in steps array
        squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
        pseudocode = algorithm_class.insertion_pseudo  # Pseudocode array
    elif "merge" in input_class.alg_types:
        algorithm_class.merge_visual()
        noflinesofpsuedocode = len(algorithm_class.merge_pseudo)  # Length of psuedocode list
        executingline = []  # Order of execution for psuedocode list
        for x in range(0, noflinesofpsuedocode):
            executingline.append(x)
        squarecolourpair = algorithm_class.merge_indices  # List of the selected indices
        array = algorithm_class.merge_steps  # Steps array
        steps = len(algorithm_class.merge_steps)  # Total number of lists in steps array
        squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
        pseudocode = algorithm_class.merge_pseudo  # Pseudocode array
    elif "quick" in input_class.alg_types:
        algorithm_class.quick_visual()
        noflinesofpsuedocode = len(algorithm_class.quick_pseudo)  # Length of psuedocode list
        executingline = []  # Order of execution for psuedocode list
        for x in range(0, noflinesofpsuedocode):
            executingline.append(x)
        squarecolourpair = algorithm_class.quick_indices  # List of the selected indices
        array = algorithm_class.quick_steps  # Steps array
        steps = len(algorithm_class.quick_steps)  # Total number of lists in steps array
        squarenumber = len(algorithm_class.myList)  # Total number of elements in original list
        pseudocode = algorithm_class.quick_pseudo  # Pseudocode array
    return render_template('visualize.html', error=errors, entries=data, squarenumber=squarenumber,
                           squarecolourpair=squarecolourpair, array=array,
                           steps=steps, noflinesofpsuedocode=noflinesofpsuedocode,
                           executingline=executingline, pseudocode=pseudocode)


@app.route('/benchmark', methods=['GET'])
def benchmark():
    errors = []
    data = {}
    input_class.output_type2 = "benchmark"
    data.update({'algorithms': input_class.alg_types, 'list': input_class.input_list})
    if "bubble" in input_class.alg_types:
        tb = algorithm_class.bubble_time()
        sb = algorithm_class.bubble_memory()
        cb, db = algorithm_class.bubble_comparisons()
    else:
        tb = 0
        sb = 0
        cb = 0
        db = 0
    if "counting" in input_class.alg_types:
        tc = algorithm_class.counting_time()
        sc = algorithm_class.counting_memory()
        cc, dc = algorithm_class.counting_comparisons()
    else:
        tc = 0
        sc = 0
        cc = 0
        dc = 0
    if "insertion" in input_class.alg_types:
        ti = algorithm_class.insertion_time()
        si = algorithm_class.insertion_memory()
        ci, di = algorithm_class.insertion_comparisons()
    else:
        ti = 0
        si = 0
        ci = 0
        di = 0
    if "merge" in input_class.alg_types:
        tm = algorithm_class.merge_time()
        sm = algorithm_class.merge_memory()
        cm, dm = algorithm_class.merge_comparisons()
    else:
        tm = 0
        sm = 0
        cm = 0
        dm = 0
    if "quick" in input_class.alg_types:
        tq = algorithm_class.quick_time()
        sq = algorithm_class.quick_memory()
        cq, dq = algorithm_class.quick_comparisons()
    else:
        tq = 0
        sq = 0
        cq = 0
        dq = 0
    return render_template('benchmark.html', error=errors, entries=data, tb=tb, tc=tc, ti=ti, tq=tq, tm=tm,
                           sb=sb, sc=sc, si=si, sq=sq, sm=sm, cb=cb, cc=cc, ci=ci, cq=cq, cm=cm, db=db,
                           dc=dc, di=di, dq=dq, dm=dm)


if __name__ == '__main__':
   app.run()

