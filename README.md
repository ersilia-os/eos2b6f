# Pkasolver
## Model identifiers
- Slug: pkasolver   
- Ersilia ID: eos2b6f
- Tags: pKa, physchem, descriptor

# Model description
Short description of the model in one or two sentences.
- Input: SMILES
- Output: pKa value (measure of aciditiy)
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
- Model was incorporated into Ersilia on 07/13/2022.

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
