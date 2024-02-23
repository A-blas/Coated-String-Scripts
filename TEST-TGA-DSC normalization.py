# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.signal import find_peaks

# def normalize_dsc_data(data):
#     max_heat_flow = data["W/g"].max()
#     data["DSC W/g_normalized"] = data["W/g"] / max_heat_flow
#     return data["DSC W/g_normalized"]

# def normalize_tga_data(data):
#     max_heat_flow = data["W/g"].max()                
#     data["TGA W/g_normalized"] = data["W/g"] / max_heat_flow
#     return data["TGA W/g_normalized"] 

# def load_tga_dsc_data(file_path):
#     return pd.read_csv(file_path, skiprows=9)

# def downsample_data(data, factor=10):
#     return data.iloc[::factor]

# def plot_dsc_data_with_peaks_troughs(ax, data, label, color, show_lines):
#     ax.plot(data["°C"], data["W/g"], label=label, color=color)
    
#     # # if show_lines:
#     # # Finding peaks and troughs
#     # peaks, _ = find_peaks(data["W/g"])
#     # troughs, _ = find_peaks(-data["W/g"])
#     # print(peaks)

#     # # Marking peaks with vertical lines
#     # for peak in peaks:
#     #     ax.axvline(x=data.iloc[peak]["°C"], color=color, linestyle='--', alpha=0.7)
    
#     # # Marking troughs with vertical lines
#     # for trough in troughs:
#     #     ax.axvline(x=data.iloc[trough]["°C"], color=color, linestyle='--', alpha=0.7)

#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Heat Flow (W/g)")
#     ax.legend()

# def plot_tga_data_with_inflections(ax, data, label, color, show_lines, mass_percent=None):
#     ax.plot(data["°C"], data["%"], label=label, color=color)
    
#     if show_lines:
#         # Calculating the derivative of weight percentage with respect to temperature
#         derivative = np.gradient(data["%"], data["°C"])
        
#         # Finding inflection points (where the derivative changes sign)
#         inflections = np.where(np.diff(np.sign(derivative)))[0]
        
#         # Marking inflection points with vertical lines
#         for inflection in inflections:
#             ax.axvline(x=data.iloc[inflection]["°C"], color=color, linestyle='--', alpha=0.7)
    
#     if mass_percent is not None:
#         ax.axhline(y=mass_percent, color=color, linestyle='--', alpha=0.7)
    
#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Weight (%)")
#     ax.legend()

# def plot_tga_dsc_data(directory, show_dsc_lines=False, show_tga_lines=False,
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
            
#             plot_dsc_data_with_peaks_troughs(ax1, data_downsampled, label, color, show_dsc_lines)
#             if "laser" in file:
#                 plot_tga_data_with_inflections(ax2, data_downsampled, label, color, show_tga_lines, m_laser_paper_percent)
#             elif "oven" in file:
#                 plot_tga_data_with_inflections(ax2, data_downsampled, label, color, show_tga_lines, m_oven_paper_percent)
#             else:
#                plot_tga_data_with_inflections(ax2, data_downsampled, label, color, show_tga_lines)

#     normalized_DSC= normalize_dsc_data(data)
#     normalized_TGA= normalize_tga_data(data)

#     ax1.set_title("DSC Data")
#     ax2.set_title("TGA Data")
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
# plot_tga_dsc_data(directory, show_dsc_lines=True, show_tga_lines=True, m_laser_paper_percent=m_laser_paper_percent, m_oven_paper_percent=m_oven_paper_percent)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# def normalize_dsc_data(data, m_paper_percent):
#     data["DSC W/g_normalized"] = data["W/g"] / m_paper_percent
#     return data

# def normalize_tga_data(data):
#     max_weight_percent = data["%"].max()
#     data["TGA %_normalized"] = data["%"] / max_weight_percent
#     return data

# def load_tga_dsc_data(file_path):
#     return pd.read_csv(file_path, skiprows=9)

# def downsample_data(data, factor=10):
#     return data.iloc[::factor]

# def plot_dsc_data(ax, data, label, color):
#     ax.plot(data["°C"], data["DSC W/g_normalized"], label=label, color=color)

#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Heat Flow (W/g)")
#     ax.legend()

# def plot_tga_data(ax, data, label, color, mass_percent=None):
#     ax.plot(data["°C"], data["TGA %_normalized"], label=label, color=color)

#     if mass_percent is not None:
#         ax.axhline(y=mass_percent, color=color, linestyle='--', alpha=0.7)

#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Weight (%)")
#     ax.legend()

# def plot_tga_dsc_data(directory, show_dsc_lines=False, show_tga_lines=False,
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
#             normalized_dsc = normalize_dsc_data(data_downsampled, m_paper_percent[label])
#             normalized_tga = normalize_tga_data(data_downsampled)

#             plot_dsc_data(ax1, normalized_dsc, label, color)
#             if "laser" in file:
#                 plot_tga_data(ax2, normalized_tga, label, color, m_laser_paper_percent)
#             elif "oven" in file:
#                 plot_tga_data(ax2, normalized_tga, label, color, m_oven_paper_percent)
#             else:
#                 plot_tga_data(ax2, normalized_tga, label, color)

#     ax1.set_title("DSC Data")
#     ax2.set_title("TGA Data")
#     plt.tight_layout()
#     plt.show()

# # Measured mass in grams
# m_laser_paper = 0.0247
# m_laser_total = 0.0515
# m_laser_paper_percent = m_laser_paper / m_laser_total

# m_oven_paper = 0.0279
# m_oven_total = 0.0603
# m_oven_paper_percent = m_oven_paper / m_oven_total

# m_paper_percent = {
#     "Coated laser": m_laser_paper_percent,
#     "Coated oven": m_oven_paper_percent,
#     "Uncoated": 1
# }

# # Specify the directory containing the CSV files
# directory = r"c:\Users\Alessandra Blasone\OneDrive\Desktop\Code\10_27_23 MCL DATA"
# plot_tga_dsc_data(directory, show_dsc_lines=True, show_tga_lines=True, m_laser_paper_percent=m_laser_paper_percent, m_oven_paper_percent=m_oven_paper_percent)





# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy import integrate

# def normalize_dsc_data(data, m_paper_percent):
#     data["DSC W/g_normalized"] = data["W/g"] / m_paper_percent
#     return data

# def normalize_tga_data(data):
#     max_weight_percent = data["%"].max()
#     data["TGA %_normalized"] = data["%"] / max_weight_percent
#     return data

# def load_tga_dsc_data(file_path):
#     return pd.read_csv(file_path, skiprows=9)

# def downsample_data(data, factor=10):
#     return data.iloc[::factor]

# # def calculate_area_under_curve(data):
# #     x = data["°C"]
# #     y = data["DSC W/g_normalized"]
# #     area = integrate.trapz(y, x)
# #     return area

# def calculate_dsc_area_under_curve(data):
#     x = data["°C"]
#     y = data["DSC W/g_normalized"]
#     area = integrate.trapz(y, x)
#     return area

# def calculate_tga_area_under_curve(data):
#     x = data["°C"]
#     y = data["TGA %_normalized"]
#     area = integrate.trapz(y, x)
#     return area

# def plot_dsc_data(ax, data, label, color):
#     ax.plot(data["°C"], data["DSC W/g_normalized"], label=label, color=color)

#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Heat Flow (W/g)")
#     ax.legend()

#     area = calculate_dsc_area_under_curve(data)
#     ax.text(0.05, 0.9, f"Area: {area:.2f}", transform=ax.transAxes)
#     return area

# def plot_tga_data(ax, data, label, color, mass_percent=None):
#     ax.plot(data["°C"], data["TGA %_normalized"], label=label, color=color)

#     if mass_percent is not None:
#         ax.axhline(y=mass_percent, color=color, linestyle='--', alpha=0.7)

#     ax.set_xlabel("Temperature (°C)")
#     ax.set_ylabel("Weight (%)")

#     area = calculate_tga_area_under_curve(data)
#     ax.text(0.05, 0.9, f"Area: {area:.2f}", transform=ax.transAxes)
#     return area

# def plot_tga_dsc_data(directory, show_dsc_lines=False, show_tga_lines=False,
#                       m_laser_paper_percent=None, m_oven_paper_percent=None):
#     files = os.listdir(directory)
#     colors = {
#         "uncoated": "#b0c4b1",
#         "coated-laser": "#3a5a40",
#         "coated-oven": "#f77f00"
#     }

#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
#     areas = []

#     for file in files:
#         if file.endswith(".csv"):
#             label = file.replace(".csv", "").replace("-", " ").capitalize()
#             color = colors.get(file.replace(".csv", ""), "black")
#             data = load_tga_dsc_data(os.path.join(directory, file))
#             data_downsampled = downsample_data(data)
#             normalized_dsc = normalize_dsc_data(data_downsampled, m_paper_percent[label])
#             normalized_tga = normalize_tga_data(data_downsampled)

#             area_dsc = plot_dsc_data(ax1, normalized_dsc, label, color)
#             area_tga = plot_tga_data(ax2, normalized_tga, label, color, m_laser_paper_percent)

#             if area_dsc is not None:
#                 areas.append(f"{label} DSC Area: {area_dsc:.2f}")
#             if area_tga is not None:
#                 areas.append(f"{label} TGA Area: {area_tga:.2f}")

#     ax1.set_title("DSC Data")
#     ax2.set_title("TGA Data")
#     plt.tight_layout()
#     plt.show()

#     print("Areas:")
#     for area in areas:
#         print(area)

# # Measured mass in grams
# m_laser_paper = 0.0247
# m_laser_total = 0.0515
# m_laser_paper_percent = m_laser_paper / m_laser_total

# m_oven_paper = 0.0279
# m_oven_total = 0.0603
# m_oven_paper_percent = m_oven_paper / m_oven_total

# m_paper_percent = {
#     "Coated laser": m_laser_paper_percent,
#     "Coated oven": m_oven_paper_percent,
#     "Uncoated": 1
# }

# # Specify the directory containing the CSV files
# directory = r"c:\Users\Alessandra Blasone\OneDrive\Desktop\Code\10_27_23 MCL DATA"
# plot_tga_dsc_data(directory, show_dsc_lines=True, show_tga_lines=True, m_laser_paper_percent=m_laser_paper_percent, m_oven_paper_percent=m_oven_paper_percent)

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def normalize_dsc_data(data, m_paper_percent):
    data["DSC W/g_normalized"] = data["W/g"] / m_paper_percent
    return data

def normalize_tga_data(data):
    max_weight_percent = data["%"].max()
    data["TGA %_normalized"] = data["%"] / max_weight_percent
    return data

def load_tga_dsc_data(file_path):
    return pd.read_csv(file_path, skiprows=9)

def downsample_data(data, factor=10):
    return data.iloc[::factor]

def calculate_dsc_area_under_curve(data):
    x = data["°C"]
    y = data["DSC W/g_normalized"]

    T_min = 300
    T_max = 500
    # Use .loc to set values outside the specified conditions to 0
    data.loc[(x < T_min) | (x > 500) | (y <= 1), "DSC W/g_normalized"] = 0

    # Integrate the values
    area = integrate.trapz(data["DSC W/g_normalized"], x=data["°C"])
    return area

def calculate_tga_area_under_curve(data):
    x = data["°C"]
    y = data["TGA %_normalized"]

    # Integrate all values
    area = integrate.trapz(y, x=x)
    return area

def plot_dsc_data(ax, data, label, color):
    ax.plot(data["°C"], data["DSC W/g_normalized"], label=label, color=color)

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Normalized Heat Flow (W/g)")
    ax.legend()

    area = calculate_dsc_area_under_curve(data)
    ax.text(0.05, 0.9, f"Area: {area:.2f}", transform=ax.transAxes)
    return area

def plot_tga_data(ax, data, label, color, mass_percent=None):
    ax.plot(data["°C"], data["TGA %_normalized"], label=label, color=color)

    if mass_percent is not None:
        ax.axhline(y=mass_percent, color=color, linestyle='--', alpha=0.7)

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Normalized Weight (%)")

    area = calculate_tga_area_under_curve(data)
    ax.text(0.05, 0.9, f"Area: {area:.2f}", transform=ax.transAxes)
    return area

def plot_tga_dsc_data(directory, show_dsc_lines=False, show_tga_lines=False,
                      m_laser_paper_percent=None, m_oven_paper_percent=None):
    files = os.listdir(directory)
    colors = {
        "uncoated": "#b0c4b1",
        "coated-laser": "#3a5a40",
        "coated-oven": "#f77f00"
    }

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    areas = []

    for file in files:
        if file.endswith(".csv"):
            label = file.replace(".csv", "").replace("-", " ").capitalize()
            color = colors.get(file.replace(".csv", ""), "black")
            data = load_tga_dsc_data(os.path.join(directory, file))
            data_downsampled = downsample_data(data)
            normalized_dsc = normalize_dsc_data(data_downsampled, m_paper_percent[label])
            normalized_tga = normalize_tga_data(data_downsampled)

            area_dsc = plot_dsc_data(ax1, normalized_dsc, label, color)
            area_tga = plot_tga_data(ax2, normalized_tga, label, color, m_laser_paper_percent)

            if area_dsc is not None:
                areas.append(f"{label} DSC Area: {area_dsc:.2f}")
            if area_tga is not None:
                areas.append(f"{label} TGA Area: {area_tga:.2f}")

    ax1.set_title("Normalized DSC Data")
    ax2.set_title("Normalized TGA Data")
    plt.tight_layout()
    plt.show()

    print("Areas:")
    for area in areas:
        print(area)

# Measured mass in grams
m_laser_paper = 0.0247
m_laser_total = 0.0515
m_laser_paper_percent = m_laser_paper / m_laser_total

m_oven_paper = 0.0279
m_oven_total = 0.0603
m_oven_paper_percent = m_oven_paper / m_oven_total

m_paper_percent = {
    "Coated laser": m_laser_paper_percent,
    "Coated oven": m_oven_paper_percent,
    "Uncoated": 1
}

T_min = 300
T_max = 500
rampRate = 10 # °C/min
T_range = T_max - T_min
time_range = (T_range / rampRate) * 60 # seconds
print(time_range)

# Specify the directory containing the CSV files
directory = r"c:\Users\Alessandra Blasone\OneDrive\Desktop\Code\10_27_23 MCL DATA"
plot_tga_dsc_data(directory, show_dsc_lines=True, show_tga_lines=True, m_laser_paper_percent=m_laser_paper_percent, m_oven_paper_percent=m_oven_paper_percent)
