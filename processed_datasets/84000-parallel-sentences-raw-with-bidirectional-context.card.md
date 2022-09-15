# Card: 84000-parallel-sentences-raw-with-bidirectional-context

## Purpose

Train a classical Tibetan to English translation model that follows the style established by 84,000. This dataset is a raw passthrough, with pre- and post-processing but no shuffling or concatenation, or augmentation with the dictionary. It does include context embeddings for the English that precedes the parallel sentence fragment, as well as source language context in the form of future tokens to the right of the source text.

## Root datasets

_84000-parallel-sentences_

## Methodology

The dataset is a processed version of the raw 84,000 parallel sentences. See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/f3fd78b5a2e58680a4aa1563feae4af345aea266/cai_garland/data/dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/f3fd78b5a2e58680a4aa1563feae4af345aea266/cai_garland/data/parallel_dataset_prep.py) for the details.

The target context embeddings consist of the BART encoder embeddings of the last 50 words preceding the English translation of the current sentence fragment in a full text of any of the published 84,000 translations. If multiple translations match, one is selected at random.

The source context embeddings are one additional 84,000 segment, sequenced with the follows-anywhere sequencing strategy and separated with the source text to be translated with a <mask> token.

## How to reproduce

Just run "cai_garland.data.parallel_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> f3fd78b5a2e58680a4aa1563feae4af345aea266

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/f3fd78b5a2e58680a4aa1563feae4af345aea266/cai_garland/data/dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.
