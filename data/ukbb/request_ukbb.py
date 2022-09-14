# simple script to download ukbb summary stats by phenotype code
import re
import sys
import os

phecode = sys.argv[1]
print(phecode)


file = open('ukbb_manifest.tsv', "r")

keys = [
    'Phenotype Code',
    'Phenotype Description', 
    'UK Biobank Data Showcase Link',
    'Sex',
    'File',
    'wget command',
    'AWS File',
    'Dropbox File',
    'md5s']																	

relevant_keys = [
    'Phenotype Code',
    'Phenotype Description',
    'Sex',
    'AWS File'
]


def proc_line(line):
    line = {k: v for k, v in zip(keys, line.strip().split('\t'))}
    res = {k: line[k] for k in relevant_keys}
    return res

lines = []
idx = 1
for line in file:
     if re.search(sys.argv[1], line):
         phe = proc_line(line)
         file_name = phe['AWS File'].split('/')[-1]

         file_path = f'{phe["Phenotype Code"]}/{file_name}'
         phe['file_path'] = file_path 

         wget_command = f'wget {phe["AWS File"]} -O {file_path}'
         phe['wget_command'] = wget_command

         lines.append(phe)
         print(
             f'{idx}) Phenotype Code: {phe["Phenotype Code"]}, Description: {phe["Phenotype Description"]}, Sex: {phe["Sex"]}',
         )
         idx += 1

dowload_idx = input("Which do you want to download? (enter a number, e.g. 1): ")

donwload_idx = int(dowload_idx) - 1
phe = lines[donwload_idx]

# download
if not os.path.exists(phe['Phenotype Code']):
    os.makedirs(phe['Phenotype Code'])
if not os.path.exists(phe['file_path']):
    print(f'Saving to {phe["file_path"]}')
    os.system(phe['wget_command'])
else:
    print('Already downloaded!')