import random
import sys

class Input:
    
    def __init__(self):
        self.alg_types = list()
        self.output_type = ""
        self.output_type2 = ""
        self.input_type = ""
        self.input_list = list()
        self.errors = []

    def receive_output_type(self, out_type):
        if out_type == "visualize" or out_type == "benchmark":
            self.output_type = out_type
        else:
            self.errors.append('Not a valid output type.')
            
    def receive_alg_types(self, algo_types):
        algo_count = 0
        self.alg_types = []
        if 'bubble' in algo_types:
            algo_count += 1
            self.alg_types.append("bubble")
        if 'counting' in algo_types:
            algo_count += 1
            self.alg_types.append("counting")
        if 'merge' in algo_types:
            algo_count += 1
            self.alg_types.append("merge")
        if 'quick' in algo_types:
            algo_count += 1
            self.alg_types.append("quick")
        if 'insertion' in algo_types:
            algo_count += 1
            self.alg_types.append("insertion")
        if algo_count > 1:
            self.output_type2 = "benchmark"
        else:
            self.output_type2 = "visualize"
        if algo_count == 0:
            self.errors.append("No valid algorithm(s) chosen.")

    def receive_input_type(self, in_type):
        if in_type == "manual" or in_type == "load" or in_type == "generate":
            self.input_type = in_type
        else:
            self.errors.append('Not a valid output type.')

    def manual(self, m_list):
        self.input_list = []
        m_list = "".join(m_list.split())
        temp_list = m_list.split(',')
        i = 0
        for x in temp_list:
            try:
                temp_list[i] = int(x)
                i += 1
            except:
                self.errors.append("List contains invalid character(s).")
        self.input_list = temp_list

    def load(self, file_name):
        self.input_list = []
        try:
            m_list = file_name.read()
            try:
                m_list = str(m_list, 'utf-8')
            except TypeError:
                file_name.seek(0)  # offset of 0
                m_list = file_name.read()  # read again
            m_list = "".join(m_list.split())
            temp_list = m_list.split(',')
            i = 0
            for x in temp_list:
                try:
                    temp_list[i] = int(x)
                    i += 1
                except:
                    self.errors.append("List contains invalid value(s).")
            self.input_list = temp_list
        except:
            self.errors.append("Unable to read file.")

    def generate(self, l_min, l_max, l_size):
        self.input_list = []
        if l_min >= l_max:
            self.errors.append("Invalid range.")
        if l_size < 2:
            self.errors.append("List size is too small.")
        for x in range(l_size):
            self.input_list.append(random.randint(l_min, l_max))

    def analyze_list(self):
        if len(self.input_list) > 100:
            self.output_type = "benchmark"
        elif len(self.input_list) == 1:
            self.errors.append("List needs to be more than 1 element.")
        else:
            count = 0
            for each in self.input_list:
                if int(each) > 99:
                    count += 1
            if count >= 1:
                self.output_type = "benchmark"
            else:
                self.output_type = "visualize"
