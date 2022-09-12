# Card: segmenter-dataset

## Purpose

Train a Tibetan segmenter model that attempts to reproduce the way 84,000 designed their parallel sentences.

## Root datasets

_84000-parallel-sentences_

## Methodology

The dataset has two parts: 84,000 sentences that are related according to follow-anywhere sequencing, and 84,000 sentences that are not related and are chosen at random instead. For each of the parts, we make positive examples by taking two sentences from the 84,000 dataset. We make negative examples by taking a positive example, concatenating the two sentences with a | character between them, picking a random space, and splitting into a new example along that space.

See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/a86f27342e1cb8d474798efa158600eac868c2b0/cai_garland/data/dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/a86f27342e1cb8d474798efa158600eac868c2b0/cai_garland/data/segmentation_dataset_prep.py) for the details of these datasets.

## How to reproduce

Just run "cai_garland.data.segmentation_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> a86f27342e1cb8d474798efa158600eac868c2b0

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/a86f27342e1cb8d474798efa158600eac868c2b0/cai_garland/data/dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.
