import numpy as np
import skfuzzy as fuz

data_points = np.arange(0,11)
sigmoid_array = fuz.sigmf(data_points,0.5,0.5)

print("Sigmoid Membership Function")
print(sigmoid_array)