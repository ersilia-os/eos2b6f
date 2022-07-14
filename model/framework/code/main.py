# imports
import os
import csv
import sys
import pandas as pd
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from framework.pkasolver.pkasolver.query import calculate_microstate_pka_values 

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# simplified version of pKa model: only the first pKa value
def my_model(smiles_list):
    outputs = []
    for smi in smiles_list:
        pka_vals = calculate_microstate_pka_values(Chem.MolFromSmiles(smi))
        if len(pka_vals) == 0:
            #TODO: handle no pka case
            outputs.append(-9999.0)
        else:
            #TODO: incorporate pka_stddev and properly formate row csv row vects
            # outputs.append([val.pka for val in pka_vals])
            outputs.append(pka_vals[0].pka)

    return outputs

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]
    
# run model
outputs = my_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"]) # header
    for o in outputs:
        writer.writerow([o])