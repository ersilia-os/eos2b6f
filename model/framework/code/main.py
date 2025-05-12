# imports
from genericpath import isfile
import os
import csv
import sys
import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt
from pathlib import Path

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(root))
sys.path.append(os.path.join(root, "pkasolver"))
from pkasolver.query import calculate_microstate_pka_values 

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]


dimorph_file = os.path.abspath(os.path.join(root, "dimorphite_dl.pkl")) 

# simplified version of pKa model: only the first pKa value
def my_model(smiles_list):
    output_df = pd.DataFrame(columns=["pka_value", "pka_stddev"])
    for smi in smiles_list:
        pka_vals = calculate_microstate_pka_values(Chem.MolFromSmiles(smi), output_path=dimorph_file)
        if len(pka_vals) == 0:
            output_df.loc[len(output_df.index)] = [np.NaN, np.NaN]
        else:
            output_df.loc[len(output_df.index)] = [pka_vals[0].pka, pka_vals[0].pka_stddev]

    return output_df

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]
    
# run model
outputs = my_model(smiles_list)

# write outputs to file (outputs is a pd dataframe)
outputs.to_csv(output_file, index=False)

# # remove dimorphite_dl output pkl file
if os.path.isfile(dimorph_file):
    os.remove(dimorph_file)
