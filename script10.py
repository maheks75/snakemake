import pandas as pd
import sys
# Load the TSV file into a DataFrame
print('script10 start')
tsv_file_path = sys.argv[1]
df = pd.read_csv(tsv_file_path, sep='\t')

# Load the text file with strings
strings_file_path = sys.argv[2]
with open(strings_file_path, 'r') as strings_file:
    umi_strings = [line.strip() for line in strings_file]

# Create a new "umi" column and add strings
df.insert(1, 'umi', umi_strings[:len(df)])

# Keep columns 0 to 54
df = df.iloc[:, :55]


# Select the columns of interest
selected_columns = [0,1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34>

selected_df = df.iloc[:, selected_columns]
#print(selected_df)
# Group by the "sequence_aa" column and aggregate other columns

aggregation_dict = selected_df.groupby('sequence_aa').agg({
                   selected_df.columns[0]: 'sum',
                   selected_df.columns[1]: 'unique',
                   selected_df.columns[4]: 'first',
                   selected_df.columns[5]: 'first',
                   selected_df.columns[6]: 'first',
                   selected_df.columns[7]: 'first',
                   selected_df.columns[8]: 'first',
                   selected_df.columns[9]: 'first',
                   selected_df.columns[10]: 'first',
                   selected_df.columns[11]: 'first',
                   selected_df.columns[12]: 'first',
                   selected_df.columns[13]: 'first',
                   selected_df.columns[14]: 'first',
                   selected_df.columns[15]: 'first',
                   selected_df.columns[16]: 'first',
                   selected_df.columns[17]: 'first',
                   selected_df.columns[18]: 'first',
                   selected_df.columns[19]: 'first',
                   selected_df.columns[20]: 'first',
                   selected_df.columns[21]: 'first',
                   selected_df.columns[22]: 'first',
                   selected_df.columns[23]: 'first',
                   selected_df.columns[24]: 'first',
                   selected_df.columns[25]: 'first',
                   selected_df.columns[26]: 'first',
                   selected_df.columns[27]: 'first',
                   selected_df.columns[28]: 'first',
                   selected_df.columns[29]: 'first',
                   selected_df.columns[30]: 'first',
                   selected_df.columns[31]: 'first',
                   selected_df.columns[32]: 'first',
                   selected_df.columns[33]: 'first',
                   selected_df.columns[34]: 'first',
                   selected_df.columns[35]: 'first',
                   selected_df.columns[36]: 'first',
                   selected_df.columns[37]: 'first',
                   selected_df.columns[38]: 'first',
                   selected_df.columns[39]: 'first',
                   selected_df.columns[40]: 'first',
                   selected_df.columns[41]: 'first',
                   selected_df.columns[42]: 'first',
                   selected_df.columns[43]: 'first',
                   selected_df.columns[44]: 'first',
                   selected_df.columns[45]: 'first',
                   selected_df.columns[46]: 'first',
                   selected_df.columns[47]: 'first',
                   selected_df.columns[48]: 'first',
                   selected_df.columns[49]: 'first',
                   selected_df.columns[50]: 'first',
                   selected_df.columns[51]: 'first',
                   selected_df.columns[52]: 'first',
                   selected_df.columns[53]: 'first',
                   selected_df.columns[54]: 'first'}
).reset_index()


aggregation_dict.to_csv(sys.argv[3], sep='\t', index=False)
# Create a DataFrame with your UMI data
df = pd.read_csv(sys.argv[3], sep='\t')
#print(df.columns)
# Split the UMI strings by space and count the number of strings
df['Number_of_Strings'] = df['umi'].apply(lambda x: len(x.split()))
df.to_csv(sys.argv[4], sep='\t', index = False)
print('script10 finish')

