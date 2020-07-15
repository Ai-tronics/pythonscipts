import skfuzzy as fuz
import numpy as np

data_array = np.arange(0,11)

tri_and_array1 = fuz.trimf(data_array,[0,0,5])
tri_and_arrayy2 = fuz.trimf(data_array,[0,5,10])

print("Fuzzy AND Intersection of two arrays")
print(fuz.fuzzy_and(data_array,tri_and_array1,data_array,tri_and_arrayy2))