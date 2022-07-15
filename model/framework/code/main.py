# imports
import os
import csv
import sys
import pandas as pd
import numpy as np
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
    output_df = pd.DataFrame(columns=["pka value", "pka stddev"])
    for smi in smiles_list:
        pka_vals = calculate_microstate_pka_values(Chem.MolFromSmiles(smi))
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
print(type(outputs))
print(outputs.head())

# write outputs to file (outputs is a pd dataframe)
outputs.to_csv(output_file, index=False)
