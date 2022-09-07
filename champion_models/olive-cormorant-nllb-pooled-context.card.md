# Card: olive-cormorant-nllb-pooled-context

The details of the training protocol are in the training results card.

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text. This version is trained with context pooling.

## Model description

- The encoder is a headless _albert-olive-cormorant_ transformer.
- The decoder is Facebook's NLLB-200 decoder, loaded from Hugging Face, with a causal LM head.
- The context encoding algorithm is:
  1. Start with previous target language tokens,
  2. Encode them with the BART encoder,
  3. Transform the BART encodings with another, randomly initialized BART encoder layer,
  4. Pool the transformed encodings by taking the encoding of the BOS token, as in BERT,
  5. And inject this pooled embedding into the second decoder input token position.

The only currently available sizes are the base size of the encoder and the 600M distillation of the decoder.

## Training data

_84000-parallel-sentences-raw-with-context_.

## CompassionAI comments

This is intended as a baseline model without any way of dealing with context and a short encoder.