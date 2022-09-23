# Card: nllb-augmentation

## Purpose

Augmentation bitext for training NMT models, extracted from NLLB.

## Root datasets

_allenai/nllb_ in the Hugging Face datasets library.

## Methodology

Currently there is only one synthetic augmentation strategy - we pull a language pair from _allenai/nllb_, typically bo-en, and translate the English side to a target language like Italian.

## How to reproduce

Just run "cai_garland.data.synthetic_nllb_data" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> fbb722623146d119a03204550a79f8f6c30cb334

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/fbb722623146d119a03204550a79f8f6c30cb334/cai_garland/data/dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.
