import pandas as pd

# Prompt the user for the number of files
num_files = int(input("Enter the number of files to merge: "))

# Initialize an empty list to store the file names
file_names = []

# Ask the user for the file names
for i in range(num_files):
    file_name = input(f"Enter the filename for file {i+1}: ")
    file_names.append(file_name)

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Read each file and merge its data into the merged_data DataFrame
for file_name in file_names:
    data = pd.read_csv(file_name)
    merged_data = pd.concat([merged_data, data], ignore_index=True)

# Sort the merged data alphabetically
merged_data.sort_values(by=list(merged_data.columns), inplace=True)

# Write the merged data to a CSV file
merged_data.to_csv('merged_data.csv', index=False)

print("Merged data has been saved to 'merged_data.csv'.")