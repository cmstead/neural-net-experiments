class Dendrite:
    def __init__(self, weight, neuron):
        self.weight = weight
        self.neuron = neuron

    def receive(self, signal):
        self.neuron.receive(signal * self.weight)
    
    def set_weight(self, weight):
        self.weight = weight