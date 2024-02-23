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

# Sort matches by name
matches.sort()

# Create subplots for each category
fig, axs = plt.subplots(5, 1, figsize=(10, 5 * 5), sharex=True)

color_list = ['#cd6155', '#1C53DD', '#18E52E', '#E5EF1E', '#000000']
color_mapping = {}  # Create a dictionary to map prefixes to colors

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
        color_mapping[prefix] = color_list[len(color_mapping) % len(color_list)]

    # Use the color from the color_mapping dictionary
    category_index = list(color_mapping.keys()).index(prefix)
    axs[category_index].plot(df['Strain_1 '], df['Load '], color=color_mapping[prefix], label=dir_name)

    # Plotting the region of interest
    x = df['Strain_1 ']
    y = df['Load ']
    mask = (x >= region_start) & (x <= region_end)
    axs[category_index].fill_between(x[mask], y[mask], color='gray', alpha=0.3, label='Region of Interest')

for ax, category in zip(axs, color_mapping.keys()):
    ax.set_xlabel("Strain")
    ax.set_ylabel("Stress")
    ax.set_title(f"Stress vs Strain - {category}")
    ax.legend()

plt.tight_layout()
plt.show()



# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# matches = []
# for root, dirs, files in os.walk(r"C:\Users\Alessandra Blasone\OneDrive\Desktop\Code\Paper Tensile Stuff\24-01-22", topdown=False):
#     for filename in files:
#         if filename.endswith('.txt'):
#             matches.append(os.path.join(root, filename))

# matches.sort()  # Sort the matches list to ensure consistent order

# # Sort matches by name
# matches.sort()

# # Create subplots for each category
# fig, axs = plt.subplots(5, 1, figsize=(10, 5 * 5), sharex=True)

# color_list = ['#cd6155', '#1C53DD', '#18E52E', '#E5EF1E', '#000000']
# color_mapping = {}  # Create a dictionary to map prefixes to colors

# # Plot lines for the trials with "_2" from each category on separate graphs
# for path in matches:
#     df = pd.read_csv(path, skiprows=6, header=0, delimiter='\t')
#     df.drop([0], axis=0, inplace=True)

#     # Convert 'Strain 1 ' column to numeric, handling errors with coerce
#     df['Load '] = pd.to_numeric(df['Load '], errors='coerce')
#     df['Strain_1 '] = pd.to_numeric(df['Strain 1 '], errors='coerce')
#     df['Time '] = pd.to_numeric(df['Time '], errors='coerce')

#     # Drop rows with NaN values in 'Strain_1 ' column
#     df = df.dropna(subset=['Strain_1 '])

#     # Get the prefix from the directory name
#     dir_name = os.path.basename(os.path.dirname(path))
#     prefix = "_".join(dir_name.split('_')[:2])

#     # If the prefix is not in the color_mapping dictionary, add it and assign a color
#     if prefix not in color_mapping:
#         color_mapping[prefix] = color_list[len(color_mapping) % len(color_list)]

#     # Use the color from the color_mapping dictionary
#     category_index = list(color_mapping.keys()).index(prefix)

#     # Plot lines for the trials with "_2" from each category
#     if "_2" in dir_name:
#         axs[category_index].plot(df['Strain_1 '], df['Load '], color=color_mapping[prefix], label=dir_name)
#         axs[category_index].set_xlabel("Strain")
#         axs[category_index].set_ylabel("Stress")
#         axs[category_index].set_title(f"Stress vs Strain - {prefix}")
#         axs[category_index].legend()

# plt.tight_layout()
# plt.show()

import os
import pandas as pd
import matplotlib.pyplot as plt

matches = []
for root, dirs, files in os.walk(r"C:\Users\Alessandra Blasone\OneDrive\Desktop\Code\Paper Tensile Stuff\24-01-22", topdown=False):
    for filename in files:
        if filename.endswith('.txt'):
            matches.append(os.path.join(root, filename))

matches.sort()  # Sort the matches list to ensure consistent order

# Sort matches by name
matches.sort()

color_list = ['#cd6155', '#1C53DD', '#18E52E', '#E5EF1E', '#000000']
color_mapping = {}  # Create a dictionary to map prefixes to colors

# Plot lines for the trials with "_2" from each category on separate graphs
for path in matches:
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
        color_mapping[prefix] = color_list[len(color_mapping) % len(color_list)]

    # Use the color from the color_mapping dictionary
    category_index = list(color_mapping.keys()).index(prefix)

    # Plot lines for the trials with "_2" from each category
    if "_2" in dir_name:
        plt.figure()  # Create a new figure for each graph
        plt.plot(df['Strain_1 '], df['Load '], color=color_mapping[prefix], label=dir_name)
        plt.xlabel("Strain")
        plt.ylabel("Stress")
        plt.title(f"Stress vs Strain - {prefix}")
        plt.legend()
        plt.show()  # Display the current graph














