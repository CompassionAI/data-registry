# Card: kangyur-tengyur-bert-like-marker-docs

## Purpose

Intended to pretrain AlBERT and other BERT-like monolingual models on cleaned documents from the Kangyur and Tengyur.

## Root datasets

OpenPecha-kangyur-tengyur

## Methodology

After cleaning the OpenPecha volumes in the usual way (see card for raw dataset):

1. Assign volumes of Kangyur and Tengyur into partition numbers, currently by taking volume number modulo 20. This results in 40 partitions - 20 for the Kangyur and 20 for the Tengyur. This is done largely to allow other scripts that use this dataset to run in parallel on each partition.
2. Within each volume, split each section of Tibetan text into its own line.
3. Add newlines whenever the "new document" Tibetan characters ("yig mgo mdun ma" and "yig mgo sgab ma") appear.
4. Add newlines at the end of every volume if needed.

## How to reproduce

See the notebook titled "With Document Boundaries", especially the function _save_partition_to_disk_.

## Comments

The dataset is called BERT-like because it follows the BERT pretraining data rules:

1. One sentence per line.
2. Empty lines designate new document start.

This data is then turned into TFRecords by the AlBERT preprocessing script in pretraining/albert/build_pretraining_data_no_sop.sh.
