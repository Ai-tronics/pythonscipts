import skfuzzy as fuz
import numpy as np

data_points = np.arange(0,11)

not_array1 = fuz.trimf(data_points,[0,0,5])
not_array2 = fuz.trimf(data_points,[0,5,10])

print("Fuzzy NOT - Compliment Membership Function")
print("Array 1: ",fuz.fuzzy_not(not_array1))
print("Array 2: ",fuz.fuzzy_not(not_array2))