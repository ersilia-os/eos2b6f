# Microstate pKa values

This model employs transfer learning with graph neural networks in order to predict micro-state pKa values of small molecules. The model enumerates the molecule's protonation states and predicts its pKa values. It was trained in two phases, first, using a large ChEMBL dataset and then fine-tuning the model for a small training set of molecules with available pKa values. The model in this repository is the pkasolver-light, which does not require an Epik license and is limited to monoprotic molecules.

## Identifiers

* EOS model ID: `eos2b6f`
* Slug: `pkasolver`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Experimental value`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Acidity of a molecule (lower pKa indicates stronger acid)

## References

* [Publication](https://www.biorxiv.org/content/10.1101/2022.01.20.476787v1)
* [Source Code](https://github.com/mayrf/pkasolver)
* Ersilia contributor: [svolk19-stanford ](https://github.com/svolk19-stanford )

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos2b6f)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2b6f.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos2b6f) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.biorxiv.org/content/10.1101/2022.01.20.476787v1) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!