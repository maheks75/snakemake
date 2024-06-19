import sys
from Bio import SeqIO
import subprocess
print('script 9 start')
input_fasta = sys.argv[1]
output_fasta = sys.argv[2]
igblast_cmd = [
     'igblastn',
     '-query', input_fasta,
     '-out', output_fasta,
     '-germline_db_V', 'IGBLAST/AlpacaV',
     '-germline_db_J', 'IGBLAST/AlpacaJ',
     '-germline_db_D', 'IGBLAST/AlpacaD',
     '-auxiliary_data','IGBLAST/camelid_gl.aux',
     '-num_threads', '32',
     '-outfmt', '19',
]
try:
    subprocess.run(igblast_cmd, check=True)
    print("IgBLAST analysis complete. Output saved to:", output_fasta)
except subprocess.CalledProcessError as e:
    print("Error running IgBLAST:", e)
print('script 9 finish')


