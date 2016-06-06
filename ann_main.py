# coding:utf8
import neural_net


class AnnMain:
    def __init__(self):
        self.net = neural_net.NeuralNet

    def create_net(self):
        pass

    def train(self):
        pass
    def test(self):
        pass

if __name__ == "__main__":
    num_input = 64
    num_hidden_layer = 1
    num_output = 10

    obj_ann = AnnMain()
    obj_ann.create_net()