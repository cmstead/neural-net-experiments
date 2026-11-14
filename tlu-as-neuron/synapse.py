class Synapse:
    def __init__(self, axon, dendrite):
        self.dendrite = dendrite
        axon.subscribe(self)

    def transmit(self, signal):
        return self.dendrite.receive(signal)