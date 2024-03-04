#final script to separate multiple repeating and strings that are repeating only twice from the total set of repeating strings
import sys
filename_5G = sys.argv[1]
filename_4G = sys.argv[2]
outfile_5G = sys.argv[3]
outfile_4G = sys.argv[4]
final_4g = sys.argv[4]
# Read the strings from the file
with open(filename_5G, 'r') as file_5G:
    count_5G = 0
    twostringlist_5G = []
    multiplestring_5G = []
    strings_5G = [line.strip() for line in file_5G]
    for string_5G in strings_5G:
        parts_5G = string_5G.split(':')
        if int(parts_5G[1]) > 49:
            multiplestring_5G.append(parts_5G[0])
            
        
with open(outfile_5G, 'w') as file_5G:
                for i, stringgg_5G in enumerate(multiplestring_5G):
                    print(stringgg_5G)
                    file_5G.write(f"{stringgg_5G} \n")         
with open(filename_4G, 'r') as file_4G:
    count_4G = 0
    twostringlist_4G = []
    multiplestring_4G = []
    strings_4G = [line.strip() for line in file_4G]
    for string_4G in strings_4G:
        parts_4G = string_4G.split(':')
        if int(parts_4G[1]) > 49:
            multiplestring_4G.append(parts_4G[0])
            
        
with open(outfile_4G, 'w') as file_4G:
                for i, stringgg_4G in enumerate(multiplestring_4G):
                    print(stringgg_4G)
                    file_4G.write(f"{stringgg_4G} \n")         
     
            
