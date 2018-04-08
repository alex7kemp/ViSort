import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from .input import Input
import sys

app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file , visort.py

app.config.update(dict(
    SECRET_KEY='development key',
))
app.config.from_envvar('VISORT_SETTINGS', silent=True)

input_class = Input()

noflinesofpsuedocode=12
# Line of psuedocode executed for each list
executingline = [0,1,2,3,4,5,6,7,8,9,10,11] #Line 0 is line 1, line 1 is line 2 and so on+/6

# Changing colour
# If we are comparing 2 with 3, 2 is green and 3 is blue
squarecolourpair=[[2,13],[14,2],[8,10],[12,5],[14,5],[3,14],[2,13],[4,2],[8,1],[2,9],[14,2],[8,10]]

array=[[16,13,11,12,1,6,9,12,9,120,11,12,1,6,9],[1,3,1,2,1,6,9,1,9,0,11,12,1,6,9],[16,4,121,102,11,6,91,12,9,0,11,12,1,6,9],[1,3,1,2,1,6,9,2,9,0,11,12,1,6,9],
       [116,113,111,112,11,16,19,112,91,120,11,12,1,6,9],[116,113,111,112,11,6,9,12,9,12,11,12,1,6,9],[16,13,11,12,1,6,9,12,9,120,11,12,1,6,9],
       [1,3,1,2,1,6,9,1,9,0,11,12,1,6,9],[16,4,121,102,11,6,91,12,9,0,11,12,1,6,9],[1,3,1,2,1,6,9,2,9,0,11,12,1,6,999],
[116,113,111,112,11,6,9,12,9,12,11,12,1,6,9],[16,13,11,12,1,6,9,112,119,120,11,12,21,336,4499]
       ]
steps=12 #vTotal number of lists
squarenumber=15 # Total number of elements in each list

# print "Number of lines of psuedocode :",noflinesofpsuedocode
# print "Executing line array :",executingline
# print "Pair for squaring array :",squarecolourpair
# print "All the sequence of steps :",array
# print "Total number of lists :",steps
# print "Number of elements in each list :", squarenumber

tb=10
sb=10
cb=10
db=10

tc=10
sc=10
cc=10
dc=10

ti=10
si=10
ci=10
di=10

tq=10
sq=10
cq=10
dq=10

tm=0
sm=0
cm=0
dm=0

@app.route('/')
def enter_list():
    errors = []
    data = {}
    return render_template('enter_list.html', error=errors, entries=data)


@app.route('/add_list', methods=['POST'])
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
        errors.append("Please enter information below and hit submit.")
        data.update({'enter_list': request.form.get('enter_list'), 'manual_list': request.form.get('manual_list'),
                     'file_name': request.form.get('file_name'), 'size': request.form.get('size'),
                     'range_min': request.form.get('range_min'), 'range_max': request.form.get('range_max')})
        return render_template('enter_list.html', error=errors, entries=data)


@app.route('/add_algorithm', methods=['POST'])
def add_algorithm():
    errors = []
    input_class.errors = []
    data = {}
    if request.method == 'POST':
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
                return render_template('benchmark.html', error=errors, entries=data, tb=tb, tc=tc, ti =ti,tq =tq,tm=tm,
                                       sb =sb,sc=sc, si=si, sq =sq,sm=sm,cb=cb ,cc=cc, ci=ci ,cq=cq, cm=cm, db=db,
                                       dc=dc,di=di,dq=dq,dm=dm)
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
                        return render_template('visualize.html', error=errors, entries=data, squarenumber=squarenumber,
                                               squarecolourpair=squarecolourpair,array=array,
                                               steps=steps,noflinesofpsuedocode=noflinesofpsuedocode,
                                               executingline=executingline)
                else:
                    errors.extend(input_class.errors)
                    data.update(
                        {'algorithm1': request.form.get('algorithm1'), 'algorithm2': request.form.get('algorithm2'),
                         'algorithm3': request.form.get('algorithm3'), 'algorithm4': request.form.get('algorithm4'),
                         'algorithm5': request.form.get('algorithm5'), 'benchmark': request.form.get('benchmark'),
                         'list': input_class.input_list})
                    return render_template('enter_algorithm.html', error=errors, entries=data)
