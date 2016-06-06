# coding:utf8

class Neuron:

    def create_input_neuron(self,num_input):
        for i in range(num_input):
            pass


    def __init__(self, num_input):
        self.num_input = num_input
        self.input = [0 for i in range(num_input)]
        self.weight = [1 for i in range(num_input)]
        self.output = 0