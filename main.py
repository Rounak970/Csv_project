import numpy as np

# Create 20 rows and 5 columns
data = np.arange(20 * 5).reshape(20, 5)

# Save in the same folder as your Python file
np.savetxt("./Rounak.csv", data, delimiter=",", fmt="%d")

print("CSV file created successfully!")