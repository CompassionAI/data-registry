# Card: tokenizer-nllb-variants

This is not a fine-tuned model, these are configuration files for variants of the tokenizer for FaceBook's NLLB-200 model.

## Purpose

Variants on the NLLB-200 model tokenizer.

## Model description

The Hugging Face NLLB-200 tokenizer but with two changes:

1. Fixed the target language token placement to be at the beginning of the sequence.
2. Ability to trim unused languages from the embedding layer and the LM head so as to save on memory.

## Training data

Not fine-tuned.

## Training protocol

Not fine-tuned.

## Notable limitations

Not applicable.

## CompassionAI comments

None.
