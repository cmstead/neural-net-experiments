from axon import Axon
from synapse import Synapse
from dendrite import Dendrite

class Neuron:
    def __init__(self, weights, threshold):
        self.dendrites = []
        self.synapses = []
        self.weighted_signals = []
        self.weights = weights
        self.weight_index = 0
        self.axon = Axon()
        self.threshold = threshold

    def get_axon(self):
        return self.axon

    def add_synapse(self, axon):
        if len(self.weights) > len(self.dendrites):
            dendrite = Dendrite(self.weights[self.weight_index], self)
            self.dendrites.append(dendrite)
            self.synapses.append(Synapse(axon, dendrite))
            self.weight_index += 1
        else:
            raise ValueError("Cannot add more synapses than there are weights.")
        
    def receive(self, weighted_signal):
        self.weighted_signals.append(weighted_signal)
        if sum(self.weighted_signals) >= self.threshold:
            self.transmit(1)
            self.weighted_signals = []
            return
        
        if len(self.weighted_signals) >= len(self.weights):
            self.transmit(0)
            self.weighted_signals = []
            return
        
    def transmit(self, signal):
        self.axon.activate(signal)

    def activate_and_transmit(self, inputs):
        signal = self.activate(inputs)
        self.transmit(signal)

    def activate(self, inputs):
        inputs = self.normalize_inputs(inputs)
        total = sum(w * i for w, i in zip(self.weights, inputs))
        signal = 1 if total >= self.threshold else 0
        return signal

    def normalize_inputs(self, values):
        return list(map(lambda x: 1 if x >= 1 else 0, values))
    
    def train(self, inputs, target, learning_rate=0.1):
        output = self.activate(inputs)
        error = target - output
        self.weights = [w + learning_rate * error * i for w, i in zip(self.weights, inputs)]
        self.threshold -= learning_rate * error