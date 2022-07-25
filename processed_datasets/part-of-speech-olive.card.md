# Card: part-of-speech-olive

## Purpose

This dataset is intended to use the SOAS tags to train a part-of-speech tagger model that does not rely on tsheg pre-tokenization. The SOAS tags have word segmentations that do not respect the tsheg (intersyllabic dot). This is because Tibetan has intrasyllabic postfixes (mostly particles) that are natural for Tibetan speakers to classify as separate words.

This current dataset is pre-tokenized with the raw SentencePiece tokenizer _olive_ and the tags are combined when needed, so that all final tags are intersyllabic.

The dataset itself is a pickle file intended to be used by the PyTorch TokenTagDataset object in the _cai_common/datasets/token_tag_dataset.py_ file in the CompassionAI/common repo.

## Warnings

This dataset is sequential with individual tagged tokens, not words. The tags may include more than one class. The BOS and EOS tokens are included. The dataset object is intended to use this as a raw passthrough.

## Root datasets

Two raw datasets are used:

- SOAS-part-of-speech: This is the main dataset with word-segmented and tagged Tibetan books.
- Esukhia-SOAS-pos-simplification: The original SOAS tags are very specific in terms of the parts of speech, for example the separate countable and uncountable nouns and have many kinds of verbs. This dataset is a few files that translate the SOAS tags into simple, universal part-of-speech designations that collapse all the different kinds of nouns and verbs into just NOUN and VERB, respectively.

## Methodology

1. Begin with the original SOAS tags, converted to the simplified part-of-speech format.
2. For each segment, tokenize the entire concatenated segment first.
3. Scan through the tokens and, for each token, take tags for words that overlap the decoded value of this token in the original section. Include WORD_END tags.
4. Replace all concatenated tags with corpus counts less than 200 with UNK.

## How to reproduce

See the notebook "SOAS non-tsheg dataset" in the CompassionAI/manas repo.

## Comments

We should investigate if there is a better way to design token classifiers for Tibetan. The current approach has a number of disadvantages:

- These tags likely confuse the model since there are multiple valid ways to segment. For example, it is likely that sections that can be segmented into two intersyllabic words VERB|PARTICLE or one word VERB+PARTICLE occur very often out-of-sample.
- The tags have to be combined. This means we either have to use multi-label classification or combine the labels. Neither one is a great choice since the dataset is small.
