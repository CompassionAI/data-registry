# Card: 84000-parallel-sentences-3-registers-only

## Purpose

Train a classical Tibetan to English translation model that follows the style established by 84,000. This dataset is a concatenation into 3 registers.

## Root datasets

_84000-parallel-sentences_ is the main source.

## Methodology

The dataset is a shuffled concatenation of the raw 84,000 parallel sentences into 3 registers, with no augmentation.

- Concatenation: consecutive short sentences are concatenated to make longer text. A range of different concatenation windows is kept in the final dataset.
- Shuffling: Consecutive English examples in the full English translations corpus are concatenated.

See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/2e438bbed1333fedf40e62654ad6ebfc20f17be2/cai_garland/data/parallel_dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/2e438bbed1333fedf40e62654ad6ebfc20f17be2/cai_garland/data/parallel_dataset_prep.py) for the details of these datasets.

## How to reproduce

Just run "cai_garland.data.parallel_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> 2e438bbed1333fedf40e62654ad6ebfc20f17be2

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/2e438bbed1333fedf40e62654ad6ebfc20f17be2/cai_garland/data/parallel_dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.
