# Card: tibetan-english-dictionaries-for-spm

## Purpose

Curated dictionary files intended for training a SentencePiece tokenizer.

## Warnings

Not originally intended to kick start unsupervised machine translation training or data augmentation.

## Root datasets

tibetan-english-dictionaries

## Methodology

The files were hand-picked for relevancy to this task. The criteria were:

- Reasonable file size, not too short.
- Mainly includes individual Tibetan words or short phrases/idioms.
- Not a glossary of esoteric terms.

Also added were two special dictionary-like files:

- The _tshig mdzod chen mo_: this was curated by the Tibetans themselves to help preserve their culture after the Cultural Revolution. It is presumably of high relevance to Tibetan Buddhism.
- The _dag tshig gsar bsgrigs_: another dictionary curated by the Tibetans themselves during the Cultural Revolution.

## How to reproduce

Copy over the hand-picked files from the raw dataset.
