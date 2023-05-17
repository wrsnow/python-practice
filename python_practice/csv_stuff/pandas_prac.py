import pandas as pd
import os
# Opening JSON file

script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)

read_file = pd.read_csv (r'disney_content.csv')
read_file.to_excel (r'disney_content.xlsx', index = None, header=True)