class ThresholdLogicUnit:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def normalize_inputs(self, inputs):
        return list(map(lambda x: 1 if x >= 1 else 0, inputs))

    def activate(self, inputs):
        inputs = self.normalize_inputs(inputs)
        total = sum(w * i for w, i in zip(self.weights, inputs))
        return 1 if total >= self.threshold else 0
        
    def get_weights(self):
        return self.weights

    def get_threshold(self):
        return self.threshold
        
    def train(self, inputs, target, learning_rate=0.1):
        output = self.activate(inputs)
        error = target - output
        self.weights = [w + learning_rate * error * i for w, i in zip(self.weights, inputs)]
        self.threshold -= learning_rate * error