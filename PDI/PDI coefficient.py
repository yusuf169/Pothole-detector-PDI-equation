import numpy as np  # Importing numpy for numerical calculations
import pandas as pd  # Importing pandas to work with data in tabular form

# Mount Google Drive to access files stored in it
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/My Drive/data.csv'
df = pd.read_csv(file_path)  # Read the CSV into a pandas DataFrame

# Extracting the important columns (zacc, xgyro, ygyro) from the pandas DataFrame

zacc = df['zacc']  # Z-axis acceleration values
xgyro = df['xgyro']  # X-axis gyroscope data along the X-axis
ygyro = df['ygyro']  # Y-axis gyroscope data along the Y-axis

# A is the matrix where each row is [xgyro^2, ygyro^2] for each data point
A = np.column_stack((xgyro**2, ygyro**2))  # Stack xgyro^2 and ygyro^2 as columns to form matrix A

# b is the vector containing zacc^2 for each data point
b = zacc**2

# This finds the best-fit values of k1 and k2 that minimize the error in the equation:
# equaion used is zacc^2 = k1 * xgyro^2 + k2 * ygyro^2
k1, k2 = np.linalg.lstsq(A, b, rcond=None)[0]  # Solving using least squares

# Print the optimal values of k1 and k2
print(f"Optimal k1: {k1}")
print(f"Optimal k2: {k2}")