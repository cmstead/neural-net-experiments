from tlu import ThresholdLogicUnit

tlu = ThresholdLogicUnit(weights=[0, 0, 0], threshold=2)
inputs = [1, 1, 1]
target = 1

print("Before training:", tlu.activate(inputs))
print("Starting weights:", tlu.get_weights())
print("Starting threshold:", tlu.get_threshold())
count = 0
while tlu.activate(inputs) != target:
    tlu.train(inputs, target)
    count += 1
print("After training:", tlu.activate(inputs))
print("Number of training iterations:", count)
print("Final weights:", tlu.get_weights())
print("Final threshold:", tlu.get_threshold())