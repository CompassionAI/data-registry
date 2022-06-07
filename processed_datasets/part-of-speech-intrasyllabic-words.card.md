# Card: part-of-speech-intrasyllabic-words

## Purpose

This dataset is intended to use the SOAS tags to train a part-of-speech tagger model that relies on tsheg pre-tokenization. The SOAS tags have word segmentations that do not respect the tsheg (intersyllabic dot). This dataset is pre-tokenized along the tsheg and the tags are combined when needed, so that all final tags are intersyllabic.

The dataset itself is a pickle file intended to be used by the PyTorch dataset object in the _cai_manas/part_of_speech/pos_intrasyllabic_dataset.py_ file in the CompassionAI/manas repo.

## Warnings

This dataset is sequential with individual tagged words. Each word is a sequence of tokens and the tags may include more than one class. The dataset object uses this to construct long sections of text to feed to the model as needed.

## Root datasets

Two raw datasets are used:

- SOAS-part-of-speech: This is the main dataset with word-segmented and tagged Tibetan books.
- Esukhia-SOAS-pos-simplification: The original SOAS tags are very specific in terms of the parts of speech, for example the separate countable and uncountable nouns and have many kinds of verbs. This dataset is a few files that translate the SOAS tags into simple, universal part-of-speech designations that collapse all the different kinds of nouns and verbs into just NOUN and VERB, respectively.

## Methodology

1. Begin with the original SOAS tags, converted to the simplified part-of-speech format.
2. For each word in the corpus that doesn't end with a tsheg, concatenate with the next word and concatenate the tags. See the algorithm in the notebook under the "Concatenate intra-tsheg tokens" section.
3. Replace all concatenated tags with corpus counts less than 100 with UNK.
4. Tokenize with tsheg pre-tokenization.
5. Remove any resulting empty sections. This is due to bad characters in the corpus, see the table of bad sections in the notebook section "Run tokenization".

## How to reproduce

See the notebook "SOAS PoS preprocess" in the CompassionAI/manas repo.

## Comments

We should investigate the decision by SOAS to make the tags with word segmentations that don't respect the tsheg. This has a number of disadvantages:

- These tags likely confuse the model since there are multiple valid ways to segment. For example, it is likely that sections that can be segmented into two intersyllabic words VERB|PARTICLE or one word VERB+PARTICLE occur very often out-of-sample.
- The tags have to be combined. This means we either have to use multi-label classification or combine the labels. Neither one is a great choice since the dataset is small.
- We already have to use tsheg pre-tokenization to get good intersyllabic word segmentation. This makes the individual tokens small and the segments long, meaning the model has to learn longer dependencies, making the task harder. This is problem since the dataset isn't huge. Making the words intrasyllabic makes the task even more difficult.
