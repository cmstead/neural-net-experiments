class ListenerDendrite:
    def __init__(self, neuron):
        self.neuron = neuron

    def receive(self, signal):
        print("Received signal: ", signal)
    