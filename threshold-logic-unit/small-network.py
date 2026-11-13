from tlu import ThresholdLogicUnit

layers = [
    [ThresholdLogicUnit(weights=[0, 0, 0, 0, 0], threshold=2), 
    ThresholdLogicUnit(weights=[0, 0, 0, 0, 0], threshold=0.3),
    ThresholdLogicUnit(weights=[0, 0, 0, 0, 0], threshold=3)],
    [ThresholdLogicUnit(weights=[0, 0, 0, 0, 0], threshold=0.2)]
];

input = [1, 0, 1, 0, 0]
expected = [1]

print("Starting training with input:", input, "and expected output:", expected)

for layer in layers:
    for tlu in layer:
        while tlu.activate(input) != expected[0]:
            tlu.train(input, expected[0])
        print("Trained TLU with final activation:", tlu.activate(input))
    input = [tlu.activate(input) for tlu in layer]
    
next_input = [tlu.activate([1, 0, 1, 0, 1]) for tlu in layers[0]]
print("Next input for second layer:", next_input)
print("Activation of TLU in second layer with next input:", layers[1][0].activate(next_input))