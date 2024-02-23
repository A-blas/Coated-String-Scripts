from matplotlib.image import pil_to_array
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\230203_Sandra_StringTestsInitial_controls-PDMS\control 02-3-23 11 41 55 AM\DAQ- Crosshead, … - (Timed).txt')
df2 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\230203_Sandra_StringTestsInitial_controls-PDMS\control_1_2 02-3-23 11 41 56 AM\DAQ- Crosshead, … - (Timed).txt')
df3 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\230203_Sandra_StringTestsInitial_controls-PDMS\control_2_1 02-3-23 11 41 56 AM\DAQ- Crosshead, … - (Timed).txt')
df4 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\230203_Sandra_StringTestsInitial_controls-PDMS\control_3_1 02-3-23 11 41 56 AM\DAQ- Crosshead, … - (Timed).txt')
df5 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\230203_Sandra_StringTestsInitial_controls-PDMS\control_4_1 02-3-23 11 41 56 AM\DAQ- Crosshead, … - (Timed).txt')
df6 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_laser_1_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df7 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_laser_2_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df8 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_laser_3_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df9 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_laser_4_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df10 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_laser_5_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df11 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_oven_2_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df12 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_oven_3_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df13 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_oven_4_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df14 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\cbPDMS_5ppm_oven_5_1 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')
df15 = pd.read_csv(r'C:\Users\apk5101\OneDrive - The Pennsylvania State University\50kN Load Frame Data\230210_Sandra_cbPDMS-string_laser-vs-oven\Test Run 2 02-10-23 11 48 47 AM\DAQ- Crosshead, … - (Timed).txt')


x = df['Strain 1 ']
y = df['Load ']

x2 = df2['Strain 1 ']
y2 = df2['Load ']

x3 = df3['Strain 1 ']
y3 = df3['Load ']

x4 = df4['Strain 1 ']
y4 = df4['Load ']

x5 = df5['Strain 1 ']
y5 = df5['Load ']

x6 = df6['Strain 1 ']
y6 = df6['Load ']

x7 = df7['Strain 1 ']
y7 = df7['Load ']

x8 = df8['Strain 1 ']
y8 = df8['Load ']

x9 = df9['Strain 1 ']
y9 = df9['Load ']

x10 = df10['Strain 1 ']
y10 = df10['Load ']

x11 = df11['Strain 1 ']
y11 = df11['Load ']

x12 = df12['Strain 1 ']
y12 = df12['Load ']

x13 = df13['Strain 1 ']
y13 = df13['Load ']

x14 = df14['Strain 1 ']
y14 = df14['Load ']

x15 = df15['Strain 1 ']
y15 = df15['Load ']



fig, axs = plt.subplots(15)

axs[0].scatter(x, y)
axs[1].scatter(x2, y2)
axs[2].scatter(x3, y3)
axs[3].scatter(x4, y4)
axs[4].scatter(x5, y5)
axs[5].scatter(x6, y6)
axs[6].scatter(x7, y7)
axs[7].scatter(x8, y8)
axs[8].scatter(x9, y9)
axs[9].scatter(x10, y10)
axs[10].scatter(x11, y11)
axs[11].scatter(x12, y12)
axs[12].scatter(x13, y13)
axs[13].scatter(x14, y14)
axs[14].scatter(x15, y15)

plt.show()


