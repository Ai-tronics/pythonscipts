import skfuzzy as fuz
import numpy as np

data_points = np.arange(0,11)

triangle_array1 = fuz.trimf(data_points,[0,0,5])
triangle_array2 = fuz.trimf(data_points,[0,5,10])

#Find the maximum between two arrays as a union
fuz.fuzzy_or(data_points,triangle_array1,data_points,triangle_array2)
print("Fuzzy OR Union:")
print(fuz.fuzzy_or(data_points,triangle_array1,data_points,triangle_array2))