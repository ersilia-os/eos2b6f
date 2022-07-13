from pkasolver.query import calculate_microstate_pka_values 
from rdkit import Chem
import pandas as pd

#  calculate microstate pka values from SMILES
mol = Chem.MolFromSmiles("O=C([O-])C[NH+](CCN(CC(=O)[O-])CC(=O)[O-])CC(=O)[O-]")
# predict pka values
protonation_states = calculate_microstate_pka_values(mol)
pka_vals = [i.pka for i in protonation_states]
pka_stddevs = [i.pka_stddev for i in protonation_states]
pka_df = pd.DataFrame({"pka": pka_vals, "pka_stddev":pka_stddevs})
print(pka_df.head())