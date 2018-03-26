import random

class Input:
    
    def __init__(self):
        self.alg_types = list()
        self.output_type = ""
        self.input_type = ""
        self.input_list = list()

    
    def receive_output_type(self, out_type):
        if (out_type ==  "visualize" or out_type == "benchmark"):
            self.output_type = out_type
        else:
            raise ValueError('Not a valid output type.')
            
    def receive_alg_types(self, algo_types):
        algo_count = 0
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
        if (algo_count > 1):
            self.output_type = "benchmark"
        if (algo_count == 0):
            raise ValueError("No valid algorithms chosen.")
            

    def receive_input_type(self, in_type):
        if (in_type ==  "manual" or in_type == "load" or in_type == "generate"):
            self.input_type = in_type
        else:
            raise ValueError('Not a valid output type.')

    def manual(self, m_list):
        temp_list = m_list.split(',')
        for x in temp_list:
            try:
                x = int(x)
            except:
                raise ValueError("List contains invalid value(s).")
        self.input_list = temp_list
        

    def load(self, file_name):
        try:
            with open(file_name, 'r') as myfile:
                m_list = myfile.read().replace('\n', '')
        except:
            raise ValueError("Unable to open file.")
        temp_list = m_list.split(',')
        for x in temp_list:
            try:
                x = int(x)
            except:
                raise ValueError("List contains invalid value(s).")
        self.input_list = temp_list

    def generate(self, l_min, l_max, l_size):
        if (l_min >= l_max):
            raise ValueError("Invalid range")
        if (l_size < 2):
            raise ValueError("List size is too small")
        for x in range(l_size):
            self.input_list.append(random.randint(l_min, l_max))

    def analyze_list(self):
        if (len(self.input_list) > 20):
            self.output_type = "benchmark"

def main():
    x = "visualize"
    y = "2342, 234234, 234234"
    z = "bubble, , bubble, insertion"
    a = "extext.txt"
    Input1 = Input()
    Input1.receive_output_type(x)
    Input1.manual(y)
    Input1.generate(10,20,50)
    Input1.receive_alg_types(z)
    Input1.load(a)

main()
