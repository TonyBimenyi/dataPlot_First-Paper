import numpy as np
import matplotlib.pyplot as plt

# Define parameters

# Path to the file
file_path = 'datascope.txt'  # Replace with your file's path

#Load the content of the data

with open(file_path, 'r') as file:
    file_content = file.read()
