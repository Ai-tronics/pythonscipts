import numpy as np
import skfuzzy as fuzzy

bell_points = np.arange(0,11)
bell_array = fuzzy.gbellmf(bell_points,0.5,0.5,0.5)

print("Bell Membership Function")
print(bell_array)
