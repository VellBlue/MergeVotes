import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)
first_file = pd.read_excel('first_excel_path')
second_file = pd.read_excel('second_excel_path')
merged_data = pd.merge(first_file, second_file, on='Compared_Column', how='inner')
merged_data['First_Column'] = pd.to_numeric(merged_data['First_Column'], errors='coerce')
merged_data['Second_Column'] = pd.to_numeric(merged_data['Second_Column'], errors='coerce')

# Sum the 'First_Column' and 'Second_Column' columns from both files.
merged_data['Sum_Column'] = merged_data['First_Column'] + merged_data['Second_Column']
merged_data = merged_data.sort_values(by='Sum_Column', ascending=False)
position_number = len(merged_data)
merged_data['Position Number'] = range(1, position_number + 1)
print (merged_data)
