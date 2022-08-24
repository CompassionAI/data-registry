# Card: 84000-parallel-sentences-raw-no-dict

## Purpose

Train a classical Tibetan to English translation model that follows the style established by 84,000. This dataset is a raw passthrough, with pre- and post-processing but no shuffling or concatenation, or augmentation with the dictionary.

## Root datasets

_84000-parallel-sentences_

## Methodology

The dataset is a processed version of the raw 84,000 parallel sentences. See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/fea0486e8e6b8ea1f5d55a054fc22146ed24e0d1/cai_garland/data/parallel_dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/fea0486e8e6b8ea1f5d55a054fc22146ed24e0d1/cai_garland/data/parallel_dataset_prep.py) for the details.

## How to reproduce

Just run "cai_garland.data.parallel_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> fea0486e8e6b8ea1f5d55a054fc22146ed24e0d1

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/fea0486e8e6b8ea1f5d55a054fc22146ed24e0d1/cai_garland/data/parallel_dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.
