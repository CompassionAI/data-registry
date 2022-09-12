# Card: 84000-parallel-sentences-raw

## Purpose

Train a classical Tibetan to English translation model that follows the style established by 84,000. This dataset is a raw passthrough, with pre- and post-processing but no shuffling or concatenation.

## Root datasets

In terms of raw datasets, _84000-parallel-sentences_ is the main source. We also use the _tibetan-english-dictionaries-for-aug_ dataset to augment the parallel data with dictionary entries.

## Methodology

The dataset is a concatenation of the raw 84,000 parallel sentences with the dictionary augmentation:

- Dictionary augmentation: The Tibetan side is a single dictionary entry, with a tsheg (intersyllabic dot) enforced at the end. There is a separate dataset row for each English dictionary entry.

See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/a86f27342e1cb8d474798efa158600eac868c2b0/cai_garland/data/dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/a86f27342e1cb8d474798efa158600eac868c2b0/cai_garland/data/parallel_dataset_prep.py) for the details of these datasets.

## How to reproduce

Just run "cai_garland.data.parallel_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> a86f27342e1cb8d474798efa158600eac868c2b0

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/a86f27342e1cb8d474798efa158600eac868c2b0/cai_garland/data/dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.
