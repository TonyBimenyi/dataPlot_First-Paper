import numpy as np
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
if ch3_data_match:
    #Convert the extracted data to a list of floats
    ch3_data = list(map(float, ch3_data_match.group(1).split(',')))

     # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(ch3_data, label='CH3_Data_OutPut[1707]', color='blue')
    plt.title('CH3_Data_OutPut[1707] Plot')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid()
    plt.legend()
    plt.show()
else:
    print("CH3_Data_OutPut[1707] not found in the file.")