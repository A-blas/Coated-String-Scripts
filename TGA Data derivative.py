# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.signal import find_peaks

# def load_tga_dsc_data(file_path):
#     return pd.read_csv(file_path, skiprows=9)

# def downsample_data(data, factor=10):
#     return data.iloc[::factor]

# def plot_tga_data_with_derivative(ax, data, label, color, show_lines, derivative_range):
#     ax.plot(data["°C"], data["%"], label=label, color=color)

#     if show_lines:
#         # Find the indices corresponding to the specified temperature range
#         range_indices = np.where((data["°C"] >= derivative_range[0]) & (data["°C"] <= derivative_range[1]))[0]
        
#         # Calculate the derivative of weight percentage within the specified range
#         derivative = np.gradient(data["%"].iloc[range_indices], data["°C"].iloc[range_indices])
        
#         # Find inflection points (where the derivative changes sign) within the specified range
#         inflections = np.where(np.diff(np.sign(derivative)) != 0)[0] + range_indices[0]
        
#         # Mark inflection points with vertical lines
#         for inflection in inflections:
#             ax.axvline(x=data.iloc[inflection]["°C"], color=color, linestyle='--', alpha=0.7)
    
#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Weight (%)")
#     ax.legend()

# def plot_derivative(ax, data, color, derivative_range):
#     # Find the indices corresponding to the specified temperature range
#     range_indices = np.where((data["°C"] >= derivative_range[0]) & (data["°C"] <= derivative_range[1]))[0]
    
#     # Calculate the derivative of weight percentage within the specified range
#     derivative = np.gradient(data["%"].iloc[range_indices], data["°C"].iloc[range_indices])
    
#     ax.plot(data["°C"].iloc[range_indices], derivative, color=color, label="Derivative")
#     ax.axhline(0, color='black', linestyle='--', alpha=0.7)  # Add horizontal line at y=0 for reference
    
#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Derivative")
#     ax.legend()

# def plot_tga_dsc_data(directory, show_tga_lines=False, derivative_range=None,
#                       m_laser_paper_percent=None, m_oven_paper_percent=None):
#     files = os.listdir(directory)
#     colors = {
#         "uncoated": "#b0c4b1",
#         "coated-laser": "#3a5a40",
#         "coated-oven": "#f77f00"
#     }

#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

#     for file in files:
#         if file.endswith(".csv"):
#             label = file.replace(".csv", "").replace("-", " ").capitalize()
#             color = colors.get(file.replace(".csv", ""), "black")
#             data = load_tga_dsc_data(os.path.join(directory, file))
#             data_downsampled = downsample_data(data)

#             if "laser" in file:
#                 plot_tga_data_with_derivative(ax1, data_downsampled, label, color, show_tga_lines, derivative_range)
#                 plot_derivative(ax2, data_downsampled, color, derivative_range)
#             elif "oven" in file:
#                 plot_tga_data_with_derivative(ax1, data_downsampled, label, color, show_tga_lines, derivative_range)
#                 plot_derivative(ax2, data_downsampled, color, derivative_range)
#             else:
#                 plot_tga_data_with_derivative(ax1, data_downsampled, label, color, show_tga_lines, derivative_range)
#                 plot_derivative(ax2, data_downsampled, color, derivative_range)

#     ax1.set_title("TGA Data")
#     ax2.set_title("Derivative of TGA Data")
#     plt.tight_layout()
#     plt.show()

# # measured mass in grams
# m_laser_paper = 0.0247
# m_laser_total = 0.0515
# m_laser_paper_percent = m_laser_paper / m_laser_total * 100

# m_oven_paper = 0.0279
# m_oven_total = 0.0603
# m_oven_paper_percent = m_oven_paper / m_oven_total * 100

# # Specify the directory containing the CSV files
# directory = r"c:\Users\Alessandra Blasone\OneDrive\Desktop\Code\10_27_23 MCL DATA"
# # Specify the temperature range for derivative calculation (from x = 285 to x = 332)
# derivative_range = (1, 500)
# plot_tga_dsc_data(directory, show_tga_lines=True, derivative_range=derivative_range)



# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.signal import find_peaks

# def load_tga_dsc_data(file_path):
#     return pd.read_csv(file_path, skiprows=9)

# def downsample_data(data, factor=10):
#     return data.iloc[::factor]

# def plot_tga_data_with_derivative(ax, data, label, color, show_lines, derivative_range):
#     ax.plot(data["°C"], data["%"], label=label, color=color)

#     if show_lines:
#         # Find the indices corresponding to the specified temperature range
#         range_indices = np.where((data["°C"] >= derivative_range[0]) & (data["°C"] <= derivative_range[1]))[0]
        
#         # Calculate the derivative of weight percentage within the specified range
#         derivative = np.gradient(data["%"].iloc[range_indices], data["°C"].iloc[range_indices])
        
#         # Find inflection points (where the derivative changes sign) within the specified range
#         inflections = np.where(np.diff(np.sign(derivative)) != 0)[0] + range_indices[0]
        
#         # Mark inflection points with vertical lines
#         for inflection in inflections:
#             ax.axvline(x=data.iloc[inflection]["°C"], color=color, linestyle='--', alpha=0.7)
    
#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Weight (%)")
#     ax.legend()

# def plot_derivative(ax, data, color, derivative_range):
#     # Find the indices corresponding to the specified temperature range
#     range_indices = np.where((data["°C"] >= derivative_range[0]) & (data["°C"] <= derivative_range[1]))[0]
    
#     # Take the absolute value of the data
#     data["%"] = np.abs(data["%"])
    
#     # Calculate the derivative of weight percentage within the specified range
#     derivative = np.gradient(data["%"].iloc[range_indices], data["°C"].iloc[range_indices])
    
#     ax.plot(data["°C"].iloc[range_indices], derivative, color=color, label="Derivative")
#     ax.axhline(0, color='black', linestyle='--', alpha=0.7)  # Add horizontal line at y=0 for reference
    
#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Derivative")
#     ax.legend()

# def plot_tga_dsc_data(directory, show_tga_lines=False, derivative_range=None,
#                       m_laser_paper_percent=None, m_oven_paper_percent=None):
#     files = os.listdir(directory)
#     colors = {
#         "uncoated": "#b0c4b1",
#         "coated-laser": "#3a5a40",
#         "coated-oven": "#f77f00"
#     }

#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

#     for file in files:
#         if file.endswith(".csv"):
#             label = file.replace(".csv", "").replace("-", " ").capitalize()
#             color = colors.get(file.replace(".csv", ""), "black")
#             data = load_tga_dsc_data(os.path.join(directory, file))
#             data_downsampled = downsample_data(data)
            
#             # Adjust data according to coating type
#             # if "uncoated" in label:
#             #     data_downsampled["%"] /= 2.512
#             # elif "coated-laser" in label:
#             #     data_downsampled["%"] /= 0.851
#             # elif "coated-oven" in label:
#             #     data_downsampled["%"] /= 0.818
#             print(label, np.max(data_downsampled["%"]))

#             plot_tga_data_with_derivative(ax1, data_downsampled, label, color, show_tga_lines, derivative_range)
#             plot_derivative(ax2, data_downsampled, color, derivative_range)

#     ax1.set_title("TGA Data")
#     ax2.set_title("Derivative of TGA Data")
#     plt.tight_layout()

# # Specify the directory containing the CSV files
# directory = r"c:\Users\Alessandra Blasone\OneDrive\Desktop\Code\10_27_23 MCL DATA"
# # Specify the temperature range for derivative calculation (from x = 285 to x = 332)
# derivative_range = (285, 332)
# plot_tga_dsc_data(directory, show_tga_lines=True, derivative_range=derivative_range)

