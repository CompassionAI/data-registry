# Card: segmenter-dataset

## Purpose

Train a Tibetan segmenter model that attempts to reproduce the way 84,000 designed their parallel sentences.

## Root datasets

_84000-parallel-sentences_

## Methodology

The dataset has two parts: 84,000 sentences that are related according to follow-anywhere sequencing, and 84,000 sentences that are not related and are chosen at random instead. For each of the parts, we begin by concatenating two of these sentences with a | character between them.

- We make positive examples by picking a random space after the | character and taking everything before this random space. Note that positive examples always include the | character. We then remove the | character from the positive example and clean up any doubled and trailing spaces.
- We make negative examples by picking a space before the | character.

See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/6df0fe283058706915025597ccfe18ad2390ba75/cai_garland/data/dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/6df0fe283058706915025597ccfe18ad2390ba75/cai_garland/data/segmentation_dataset_prep.py) for the details of these datasets.

## How to reproduce

Just run "cai_garland.data.segmentation_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> 6df0fe283058706915025597ccfe18ad2390ba75

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/6df0fe283058706915025597ccfe18ad2390ba75/cai_garland/data/dataset_prep.config).
