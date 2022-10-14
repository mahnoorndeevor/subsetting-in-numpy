# height_in and weight_lb are available as a regular lists
height_in=[128, 140, 160, 170, 190, 50]
weight_lb=[140, 130, 100, 150, 160, 1100]
# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light=bmi<21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[bmi<21])
