# Card: nllb

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of short text fragments. This version is trained _without_ context pooling.

The training commit SHA for CompassionAI/garland is:

> 5278dcf686e941ab368b74ac40a875d66f71b175

## Model description

- The source language encoder is the NLLB encoder, restricted to Tibetan.
- The decoder is NLLB decoder, loaded from Hugging Face, restricted to English with a causal LM head.

The only currently available sizes are the base size of the encoder and the base size for the decoder.

## Training data

See the processed datasets _84000-parallel-sentences-raw-with-context_.

## CompassionAI comments

Adding source context doesn't seem to improve the overall performance of the translation model.
