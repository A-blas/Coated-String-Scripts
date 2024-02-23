import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Define the region of interest
region_start = 0.0001
region_end = 0.0002

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
    df.plot(y='Load ', x='Strain_1 ', kind='line', color=color_mapping[prefix], ax=axs, label=dir_name)

# Plotting the region of interest
x = df['Strain_1 ']
y = df['Load ']
mask = (x >= region_start) & (x <= region_end)
plt.fill_between(x[mask], y[mask], color='gray', alpha=0.3, label='Region of Interest')

# For scatter plots, add s={size} for the size of the dot on the plot
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.title("Stress vs Strain of Samples in Tensile Testing Machine")

plt.legend()

plt.show()

