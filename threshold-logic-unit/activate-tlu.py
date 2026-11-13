from tlu import ThresholdLogicUnit

tlu1 = ThresholdLogicUnit(weights=[1], threshold=0.5)
tlu2 = ThresholdLogicUnit(weights=[0.6], threshold=0.5)

tlu3 = ThresholdLogicUnit(weights=[0.4, 0.5], threshold=0.5)

inputs1 = [1]

output1 = tlu1.activate(inputs1)
output2 = tlu2.activate(inputs1)
output3 = tlu3.activate([output1, output2])

print(output3)