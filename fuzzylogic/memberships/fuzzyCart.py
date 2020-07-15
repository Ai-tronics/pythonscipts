import skfuzzy as fuz
import numpy as np

data_point = np.arange(0,11)

cart_array1 = fuz.trimf(data_point,[0,0,5])
cart_array2 = fuz.trimf(data_point,[0,5,10])

print("Cartesian PRODUCT Membership Function")
print(fuz.cartprod(cart_array1,cart_array2))