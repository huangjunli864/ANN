# coding:utf8
import hidden_layer
import input_layer
import output_layer


class NeuralNet:

    def create_net(self, num_input, num_output, num_hidden_layer, num_pre_hiidden_layer):
        self.input_layer.create_input_layer(num_input)

    def train_net(self):
        pass

    def save_net(self):
        pass

    def load_net(self):
        pass

    def test(self):
        pass

    def __init__(self):
        self.num_input = 0
        self.num_output = 0
        self.num_hidden_layer = 0
        # self.neuron_pre_hidden_layer = 1
        # self.input_layer = input_layer.InputLayer
        # self.hidden_layer = hidden_layer.HiddenLayer
        # self.output_layer = output_layer.OutputLayer