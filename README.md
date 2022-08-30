# Pkasolver
## Model identifiers
- Slug: pkasolver   
- Ersilia ID: eos2b6f
- Tags: pKa, physchem, descriptor

# Model description
Short description of the model in one or two sentences.
- Input: SMILES
- Output: first pKa value (measure of aciditiy) and estimate stddev of pKa value
- Model type: Regression
- Training set: 714,906 compounds
- Mode of training: Pretrained

# Source code
This model has been published by Fritz M, Wieder M, Wieder O, Langer T. Improving Small Molecule pKa Prediction Using Transfer Learning with Graph Neural Networks. Frontiers in Chemistry, vol. 10. 2022 May 26. doi: 10.3389/fchem.2022.866585  

- Code: https://github.com/mayrf/pkasolver
- Checkpoints: https://github.com/mayrf/pkasolver/tree/main/pkasolver/trained_model_without_epik

# License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "pkasolver", located at /model and licensed under an [MIT License](https://github.com/ersilia-os/eos2b6f/blob/main/model/LICENSE.md).

# History 
- Model was downloaded on 07/13/2022 from the [pkasolver GitHub repository](https://github.com/mayrf/pkasolver). 
- Use case was inspired by the provided [query notebook](https://github.com/ersilia-os/eos2b6f/blob/main/model/framework/pkasolver/notebooks/query_example.ipynb).
- Edited the imports of the following scripts to ensure compatibility and eliminate setup.py install command: (call_dimorphite_dl.py, dimorphite_dl.py, query.py, constants.py, data.py, ml.py, ml_architecture.py)
- Commented unnecessary visualization code in query.py
- Adapted model to output only the first pKa value. The fully open source pkasolver-light model version was only trained with the first pKa value of a compound. Access to an [Epik](https://www.schrodinger.com/products/epik) license is necessary for use of the pkasolver-epic model trained to deliver multiprotic pKa values (Fritz et al.). 
- Added a new argument (output_path) to dimorphite_dl.py script, changing function calls in call_dimorphite_dl.py and query.py to reflect this difference. This change was made to pipe the output from dimorphite_dl such that it can later be deleted from the user's system. 
- Model was incorporated into Ersilia on 07/13/2022.

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
