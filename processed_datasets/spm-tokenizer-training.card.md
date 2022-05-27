# Card: spm-tokenizer-training

## Purpose

Train a SentencePiece tokenizer model, or something similar like WordPiece.

## Root datasets

tibetan-english-dictionaries-for-spm

## Methodology

This dataset is a concatenation of two preprocessed sets of strings, derived from the root dataset:

1. All distinct Unicode characters that appear in the root dataset, corresponding to the Tibetan letters.
2. All words with less than 5 morphemes (delimited by the tseg), ending with a tseg.

## How to reproduce

See the notebook "Dictionary Tokenizers".

## Comments

The letters are included to ensure that any word can be tokenized, including Sanskrit and other purely phonetic text. Some drawbacks of this approach are:

- Just because everything can be tokenized, doesn't mean the model embeddings of it will mean anything. A more subtle issue is that the tokenizations will be very long, so the models will need to learn long dependencies and memorize long sequences, which degrades their performance.
- The shads are tokenized separately. This is to keep the number of tokens, and consequently the monolingual model size, down. The downside is that some Tibetan letters act as a shad, so the tokenization is inconsistent. This is unlikely to make much difference.

An alternative could be to tokenize the named entities and Sanskrit separately.
