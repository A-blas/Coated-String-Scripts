import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

matches = []
for root, dirs, files in os.walk(r"C:\Users\Alessandra Blasone\OneDrive\Desktop\Code\Paper Tensile Stuff\24-01-22", topdown=False):
    for filename in files:
        if filename.endswith('.txt'):
            matches.append(os.path.join(root, filename))

matches.sort()  # Sort the matches list to ensure consistent order

fig, axs = plt.subplots()

color_list = ['#cd6155', '#1C53DD', '#18E52E', '#E5EF1E', '#000000']
color_mapping = {}  # Create a dictionary to map prefixes to colors
i = 0

# Define the linear region of interest
linear_region_start = 0.0001
linear_region_end = 0.0009

for index, path in enumerate(matches):
    df = pd.read_csv(path, skiprows=6, header=0, delimiter='\t')
    df.drop([0], axis=0, inplace=True)

    # Convert 'Strain 1 ' column to numeric, handling errors with coerce
    df['Load '] = pd.to_numeric(df['Load '], errors='coerce')
    df['Strain_1 '] = pd.to_numeric(df['Strain 1 '], errors='coerce')  
    df['Time '] = pd.to_numeric(df['Time '], errors='coerce')

    # Drop rows with NaN values in 'Strain_1 ' column
    df = df.dropna(subset=['Strain_1 '])

    # Get the prefix from the directory name
    dir_name = os.path.basename(os.path.dirname(path))
    prefix = "_".join(dir_name.split('_')[:2])

    # If the prefix is not in the color_mapping dictionary, add it and assign a color
    if prefix not in color_mapping:
        color_mapping[prefix] = color_list[i % len(color_list)]
        i += 1

    # Use the color from the color_mapping dictionary
    axs.plot(df['Strain_1 '], df['Load '], color=color_mapping[prefix], label=dir_name)

    # Fit linear regression to the specified linear region
    mask_linear = (df['Strain_1 '] >= linear_region_start) & (df['Strain_1 '] <= linear_region_end)
    slope, intercept, _, _, _ = linregress(df['Strain_1 '][mask_linear], df['Load '][mask_linear])
    linear_fit = slope * df['Strain_1 '] + intercept
    axs.plot(df['Strain_1 '], linear_fit, linestyle='--', color=color_mapping[prefix], alpha=0.7)

# For scatter plots, add s={size} for the size of the dot on the plot
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.title("Stress vs Strain of Samples in Tensile Testing Machine")

plt.legend()

plt.show()





import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

matches = []
for root, dirs, files in os.walk(r"C:\Users\Alessandra Blasone\OneDrive\Desktop\Code\Paper Tensile Stuff\24-01-22", topdown=False):
    for filename in files:
        if filename.endswith('.txt'):
            matches.append(os.path.join(root, filename))

matches.sort()  # Sort the matches list to ensure consistent order

fig, axs = plt.subplots()

color_list = ['#cd6155', '#1C53DD', '#18E52E', '#E5EF1E', '#000000']
color_mapping = {}  # Create a dictionary to map prefixes to colors
i = 0

# Define the linear region of interest
linear_region_start = 0.0001
linear_region_end = 0.0009

# Dictionary to store slopes for each category
category_slopes = {}

for index, path in enumerate(matches):
    df = pd.read_csv(path, skiprows=6, header=0, delimiter='\t')
    df.drop([0], axis=0, inplace=True)

    # Convert 'Strain 1 ' column to numeric, handling errors with coerce
    df['Load '] = pd.to_numeric(df['Load '], errors='coerce')
    df['Strain_1 '] = pd.to_numeric(df['Strain 1 '], errors='coerce')  
    df['Time '] = pd.to_numeric(df['Time '], errors='coerce')

    # Drop rows with NaN values in 'Strain_1 ' column
    df = df.dropna(subset=['Strain_1 '])

    # Get the prefix from the directory name
    dir_name = os.path.basename(os.path.dirname(path))
    prefix = "_".join(dir_name.split('_')[:2])

    # If the prefix is not in the color_mapping dictionary, add it and assign a color
    if prefix not in color_mapping:
        color_mapping[prefix] = color_list[i % len(color_list)]
        i += 1

    # Fit linear regression to the specified linear region
    mask_linear = (df['Strain_1 '] >= linear_region_start) & (df['Strain_1 '] <= linear_region_end)
    slope, intercept, _, _, _ = linregress(df['Strain_1 '][mask_linear], df['Load '][mask_linear])

    # Store the slope in the category_slopes dictionary
    category_slopes.setdefault(prefix, []).append(slope)

# Plot the average line for each category
for category, slopes in category_slopes.items():
    avg_slope = np.mean(slopes)
    avg_linear_fit = avg_slope * df['Strain_1 '] + intercept
    axs.plot(df['Strain_1 '], avg_linear_fit, linestyle='--', color=color_mapping[category], label=f'{category} (Average)')

# For scatter plots, add s={size} for the size of the dot on the plot
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.title("Average Linear Region of Stress vs Strain of Samples in Tensile Testing Machine")

plt.legend()

plt.show()



import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

matches = []
for root, dirs, files in os.walk(r"C:\Users\Alessandra Blasone\OneDrive\Desktop\Code\Paper Tensile Stuff\24-01-22", topdown=False):
    for filename in files:
        if filename.endswith('.txt'):
            matches.append(os.path.join(root, filename))

matches.sort()  # Sort the matches list to ensure consistent order

fig, axs = plt.subplots()

color_list = ['#cd6155', '#1C53DD', '#18E52E', '#E5EF1E', '#000000']
color_mapping = {}  # Create a dictionary to map prefixes to colors
i = 0

# Define the linear region of interest
linear_region_start = 0.0001
linear_region_end = 0.0009

# Dictionary to store slopes for each category
category_slopes = {}

for index, path in enumerate(matches):
    df = pd.read_csv(path, skiprows=6, header=0, delimiter='\t')
    df.drop([0], axis=0, inplace=True)

    # Convert 'Strain 1 ' column to numeric, handling errors with coerce
    df['Load '] = pd.to_numeric(df['Load '], errors='coerce')
    df['Strain_1 '] = pd.to_numeric(df['Strain 1 '], errors='coerce')  
    df['Time '] = pd.to_numeric(df['Time '], errors='coerce')

    # Drop rows with NaN values in 'Strain_1 ' column
    df = df.dropna(subset=['Strain_1 '])

    # Get the prefix from the directory name
    dir_name = os.path.basename(os.path.dirname(path))
    prefix = "_".join(dir_name.split('_')[:2])

    # If the prefix is not in the color_mapping dictionary, add it and assign a color
    if prefix not in color_mapping:
        color_mapping[prefix] = color_list[i % len(color_list)]
        i += 1

    # Fit linear regression to the specified linear region
    mask_linear = (df['Strain_1 '] >= linear_region_start) & (df['Strain_1 '] <= linear_region_end)
    slope, intercept, _, _, _ = linregress(df['Strain_1 '][mask_linear], df['Load '][mask_linear])

    # Store the slope in the category_slopes dictionary
    category_slopes.setdefault(prefix, []).append(slope)

# Plot the average line and shaded region for each category
for category, slopes in category_slopes.items():
    avg_slope = np.mean(slopes)
    avg_linear_fit = avg_slope * df['Strain_1 '] + intercept
    
    # Calculate standard deviation of slopes
    std_slope = np.std(slopes)
    
    # Plot the average line
    axs.plot(df['Strain_1 '], avg_linear_fit, linestyle='--', color=color_mapping[category], label=f'{category} (Average)')
    
    # Plot shaded region around the average line
    axs.fill_between(df['Strain_1 '], avg_linear_fit - std_slope, avg_linear_fit + std_slope, color=color_mapping[category], alpha=0.15)

# For scatter plots, add s={size} for the size of the dot on the plot
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.title("Average Linear Region with Standard Deviation of Stress vs Strain of Samples in Tensile Testing Machine")

plt.legend()

plt.show()
