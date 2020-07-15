import numpy as np
import skfuzzy as sfuzz

data_range = np.arange(0,11)

trap_array = sfuzz.trapmf(data_range,[0,0,5,5])

print("Trapizoidal Membership Function")
print(trap_array)

