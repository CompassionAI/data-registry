# Card: segmenter-olive-cormorant

The details of the training protocol are in the training results card.

## Purpose

Segmentation of long text into segments to be fed to the translation model.

## Model description

Fine-tuned AlBERT-olive-cormorant transformer with a sequence classification head.

## Training data

Directly ingests the training data from segmenter-dataset.

## Training protocol

See the training results below.

## Notable limitations (optional)

Due to resource constraints, currently this is a base-sized model of width 128.
