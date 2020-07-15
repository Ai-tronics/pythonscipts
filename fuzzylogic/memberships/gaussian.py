import numpy as np
import skfuzzy as sfuzz

print("Gaussian Membership Function")
data_range = np.arange(0,11)
gaus_array = sfuzz.gaussmf(data_range,np.mean(data_range),np.std(data_range)) #calculate mean and standard deviation for the data points
print(gaus_array)