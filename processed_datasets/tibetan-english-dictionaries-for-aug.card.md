# Card: tibetan-english-dictionaries-for-aug

## Purpose

Curated dictionary files intended for augmenting machine translation training datasets with contextless dictionary entries.

## Warnings

Not originally intended to kick start unsupervised machine translation training.

## Root datasets

tibetan-english-dictionaries

## Methodology

The files were hand-picked for relevancy to this task. Two dictionaries were selected:

- Rangjung Yeshe translator dictionary, due to relevance to the translation task.
- 84,000 Sanskrit glossary. This was included because the 84,000 parallel sentences dataset includes many Sanskrit terms. The hope is that this glossary can be used to train a model to learn these terms.

## How to reproduce

Copy over the hand-picked files from the raw dataset.
