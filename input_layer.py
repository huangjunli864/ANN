# coding:utf8
import neuron


class InputLayer:

    def create_input_layer(self, num_input):
        self.neuron.create_input_neuron(num_input)

    def _sNeuron(self):
        pass

    def __init__(self):
        self.neuron = neuron.Neuron