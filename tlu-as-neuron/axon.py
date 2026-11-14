class Axon:
    def __init__(self):
        self.synapse = None
        
    def activate(self, signal):
        if self.synapse:
            return self.synapse.transmit(signal)
    
    def subscribe(self, synapse):
        self.synapse = synapse
