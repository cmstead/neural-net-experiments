from neuron import Neuron
from listener_dendrite import ListenerDendrite
from synapse import Synapse

inputs = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1]]
layers = [
    [
        Neuron([0.5, 0.5, 0.5], 1),
        Neuron([0.5, 0.5, 0.5], 1),
        Neuron([0.5, 0.5, 0.5], 1)
    ],
    [
        Neuron([0.5, 0.5, 0.5], 1)
    ]
]

neuron_count = 0;

def train(neuron, input, target):
    while neuron.activate(input) != target:
        neuron.train(input, target)

for layer in layers:
    for neuron in layer:
        train(neuron, inputs[neuron_count], 1)
        neuron_count += 1

final_neuron = layers[1][0]

for neuron in layers[0]:
    final_neuron.add_synapse(neuron.get_axon())
    
synapse = Synapse(final_neuron.get_axon(), ListenerDendrite(final_neuron))

for neuron in layers[0]:
    neuron.activate_and_transmit([1, 0, 0])