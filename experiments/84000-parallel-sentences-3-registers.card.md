# Card: 84000-parallel-sentences-3-registers

## Purpose

Train a classical Tibetan to English translation model that follows the style established by 84,000. This version of the dataset is intended for training encoders with 3 registers.

## Warnings

This version of the dataset includes the [eor] register break tokens on the Tibetan side. Depending on what you're doing, if you're not trying a register-enabled encoder, you may need to remove these tokens or remove entries with these tokens.

## Root datasets

The raw datasets used are:

- _84000-parallel-sentences_ is the main source.
- _84000-translations-tei_ is joined to _OpenPecha-kangyur-old_ to get folio-level translations.

We also use the _tibetan-english-dictionaries-for-aug_ dataset to augment the parallel data with dictionary entries.

## Methodology

The dataset is a concatenation of different augmentation strategies:

- Concatenation: consecutive short sentences are concatenated to make longer text. A range of different concatenation windows is kept in the final dataset.
- Shuffling: Random sentences are concatenated, except that the English side of the concatenation has to have a high score with a next sentence prediction model.
- Segmentation into registers: The Tibetan side can be lengthened by segmenting long text into registers. The current segmentation uses 3 registers. Register break is marked with the [eor] token, there are n-1 of these tokens for n registers. The default segmentation is greedy. We also add non-greedy augmented register segmentations that use random splits for the register breaks that are required to contain no more than "model_length" (currently 128) tokens.
- Dictionary augmentation: The Tibetan side is a single dictionary entry, with a tsheg (intersyllabic dot) enforced at the end. There is a separate dataset row for each English dictionary entry.

The final dataset is made from 3 concatenated intermediate datasets:

1. _naive-concats_: Consecutive concatenation with no shuffling or any kind of registers.
2. _concatted-registers-shuffled_: Shuffled concatenation with registers.
3. _dictionary_: Dictionary augmentation dataset with no concatenation.

See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/aadd502bb08e1bac20794b26d91d5fd3f1e5a084/cai_garland/data/dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/aadd502bb08e1bac20794b26d91d5fd3f1e5a084/cai_garland/data/parallel_dataset_prep.py) for the details of these datasets.

## How to reproduce

Just run "cai_garland.data.parallel_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> aadd502bb08e1bac20794b26d91d5fd3f1e5a084

The tokenizer is in the CompassionAI/manas repo, commit SHA:

> c8864943348ed821a4ddd11869d360158f54966b

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/aadd502bb08e1bac20794b26d91d5fd3f1e5a084/cai_garland/data/dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.

The current detection of locators in the loader for the _84000-translations-tei_ dataset (TeiLoader object) is dirty for texts with multiple Tohoku numbers. There is a work item to fix this. The dataset will need to be regenerated after.

The next sentence model is currently the BERT-base secondary pretraining task. This doesn't seem to work very well. We may get a large improvement from using a better model for this.
