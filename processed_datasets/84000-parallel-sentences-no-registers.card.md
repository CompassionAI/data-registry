# Card: 84000-parallel-sentences-no-registers

## Purpose

Train a classical Tibetan to English translation model that follows the style established by 84,000. This dataset does not include any of the intermediate datasets that include registers.

## Root datasets

In terms of raw datasets, _84000-parallel-sentences_ is the main source. We also used to use the _tibetan-english-dictionaries-for-aug_ dataset to augment the parallel data with dictionary entries but currently do not.

## Methodology

The dataset is a concatenation of different augmentation strategies:

- Concatenation: consecutive short sentences are concatenated to make longer text. A range of different concatenation windows is kept in the final dataset.
- Sequencing: Random sentences are concatenated, except that the English side of the concatenation has to have a high score with a next sentence prediction model.
- Dictionary augmentation: The Tibetan side is a single dictionary entry, with a tsheg (intersyllabic dot) enforced at the end. There is a separate dataset row for each English dictionary entry. NB: this is currently deactivated.

The final dataset is made from 6 concatenated intermediate datasets:

1. _naive-concats_: Consecutive concatenation with no sequencing or any kind of registers.
2. _naive-concats-sequenced_: sequenced concatenation with no registers.
3. _dictionary_: Dictionary augmentation dataset with no concatenation.

See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/a67ca99d3b1725cfbc848a1652054ab6d286540a/cai_garland/data/parallel_dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/a67ca99d3b1725cfbc848a1652054ab6d286540a/cai_garland/data/parallel_dataset_prep.py) for the details of these datasets.

## How to reproduce

Just run "cai_garland.data.parallel_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> a67ca99d3b1725cfbc848a1652054ab6d286540a

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/a67ca99d3b1725cfbc848a1652054ab6d286540a/cai_garland/data/parallel_dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.

The next sentence model is currently an MNLI model. This works OK but large gains may come from improving it.