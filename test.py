# import numpy as np
import matplotlib.pyplot as plt
import re

# Define parameters

# Path to the file
file_path = 'datascope.txt'  # Replace with your file's path

#Load the content of the data

with open(file_path, 'r') as file:
    file_content = file.read()


#Extract the CH3 data

ch3_data_match = re.search(r'CH3_Data_OutPut\[\d+\]=\{(.*?)\};',  file_content,re.DOTALL)
ch1_data_match = re.search(r'CH1_Data_OutPut\[\d+\]=\{(.*?)\};',  file_content,re.DOTALL)
ch2_data_match = re.search(r'CH2_Data_OutPut\[\d+\]=\{(.*?)\};',  file_content,re.DOTALL)
ch4_data_match = re.search(r'CH4_Data_OutPut\[\d+\]=\{(.*?)\};',  file_content,re.DOTALL)


if ch3_data_match and ch1_data_match and ch2_data_match and ch4_data_match:
    #Convert the extracted data to a list of floats
    ch3_data = list(map(float, ch3_data_match.group(1).split(',')))
    ch1_data = list(map(float, ch1_data_match.group(1).split(',')))
    ch2_data = list(map(float, ch2_data_match.group(1).split(',')))
    ch4_data = list(map(float, ch4_data_match.group(1).split(',')))

    # Calculate distributed errors
    error1 = [ref - m1 for ref, m1 in zip(ch2_data, ch1_data)]
    error2 = [ref - m2 for ref, m2 in zip(ch2_data, ch3_data)]
    error3 = [ref - m3 for ref, m3 in zip(ch2_data, ch4_data)]

     # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(ch2_data,'-o', label='Reference Trajectory', color='blue', markersize=4.5)
    plt.plot(ch1_data, '-*', label='Motor1', color='green', markersize=5.5)
    plt.plot(ch3_data, '-', label='Motor 2', color='red', markersize=2.5)
    plt.plot(ch4_data, '--', label='Motor 3', color='orange', markersize=0.5)


    plt.title('DC-Motors Tracking Performance', fontweight='bold')
    plt.xlabel('Steps')
    plt.ylabel('Value')
    # Adding multiple grids
    plt.grid(True, which='major', color='black', linestyle='-', linewidth=0.8)  # Major grid
    plt.grid(True, which='minor', color='gray', linestyle='--', linewidth=0.5)  # Minor grid
    plt.minorticks_on()  # Enable minor ticks for better detai
    plt.legend()
    plt.show()
else:
    print("CH3_Data_OutPut[1707] not found in the file.")