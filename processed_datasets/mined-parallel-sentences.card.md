# Card: mined-parallel-sentences

## Purpose

A dataset mined from the folio-aligned translations published by 84,000.

## Root datasets

_84000-translations-tei_, _OpenPecha-kangyur_, _Esukhia-derge-tengyur_

## Methodology

See the "Parallel text mining.ipynb" notebook in the CompassionAI/garland repo for experiments justifying the choices.

1. Begin by aligning the Kangyur and Tengyur locations to the locations in the 84,000 data.
2. Segment all Tibetan folios with the segmenter model used in the end-to-end translation CLI.
3. Split the aligned English on punctuation, call this the base English segments.
4. Select eligible English segments using the following rules:
    - The count of base English segments should be equal to the number of preceding Tibetan sections (not segments),
  fudged +/- by a location fudge of 5.
    - Take concatenations of base English segments of width up to and equal to a fudge of 2.
    - Count the tsheg-separated Tibetan syllables in the Tibetan segment, call this syllable count. Filter out all concatenations that don't have at least 0.9 * syllable count or have more than 2.2 * syllable count English words.
5. Score the remaining English concatenations against the Tibetan segment and compute the model loss. Currently we use the olive-cormorant-nllb model for this.

To get the mined aligned segments, start with the segment with the lowest model score. Remove this segment, as well as any candidates whose English concatenations overlap with the English concatenation of the lowest model score. Repeat this until there are no more candidates.

## How to reproduce

Just run "cai_garland.data.mined_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> e3733f8d96406d8698d7c0cb97a034614e4d2ac8

This script has no configuration options.
