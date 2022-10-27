# Card: olive-cormorant-nllb-frozen-lm-head

The details of the training protocol are in the training results card.

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of short fragments. Trained _without_ context injection. This version of the model has a frozen LM head.

## Model description

- The encoder is a headless _albert-olive-cormorant_ transformer.
- The decoder is Facebook's NLLB-200 decoder, loaded from Hugging Face, with a causal LM head.

The only currently available sizes are the base size of the encoder and the 600M distillation of the decoder.

## Training data

_84000-parallel-sentences-raw-with-context_.

## CompassionAI comments

This is intended as a baseline model without any way of dealing with context and a short encoder.