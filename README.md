# Microstate pKa values

This model employs transfer learning with graph neural networks in order to predict micro-state pKa values of small molecules. The model enumerates the molecules protonation states and predicts its pKa values. It was trained in two phases, first, using a large ChEMBL dataset and then fine-tuning the model for a small training set of molecules with available pKa values. The model in this repository is the pkasolver-light, which does not require an Epik license and is limited to monoprotic molecules.

This model was incorporated on 2022-07-13.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2b6f`
- **Slug:** `pkasolver`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Not Applicable`
- **Tags:** `pKa`, `ADME`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Acidity of a molecule (lower pKa indicates stronger acid)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| pka_value | float | high | Predicted pKa value of the compound |
| pka_stddev | float | low | Standard deviation of the predicted pKa value |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2b6f](https://hub.docker.com/r/ersiliaos/eos2b6f)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2b6f.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2b6f.zip)

### Resource Consumption
- **Model Size (Mb):** `213`
- **Environment Size (Mb):** `5658`


### References
- **Source Code**: [https://github.com/mayrf/pkasolver](https://github.com/mayrf/pkasolver)
- **Publication**: [https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2022.866585/full](https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2022.866585/full)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [svolk19-stanford ](https://github.com/svolk19-stanford )

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2b6f
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2b6f
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
