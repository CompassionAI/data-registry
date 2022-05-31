# Card: 84000-translations-tei

## Summary

Raw English translations from 84,000 in Tei XML format.

## Source

<https://github.com/84000/data-tei.git> master branch.

## Ingestion tools

Use the TeiLoader class in the CompassionAI/common repo, in the file _/cai_common/data/tei_loader.py_.

Code sample:

```python
# You need a local Dask cluster for all CompassionAI datasets
from dask.distributed import Client, LocalCluster
dask_cluster = LocalCluster(n_workers=10, threads_per_worker=1)
dask_client = Client(dask_cluster)

# Data location comes from the CAI_DATA_BASE_PATH environment variable
from cai_common.data import TeiLoader
kangyur_df = TeiLoader("kangyur").dataframe
```

## CompassionAI comments

There is some Chinese mixed in, but currently it is very little.

There are duplicate translations in the data set, meaning multiple files for the same text with the same Tohoku number. They have different titles but it is unclear how different the content of the individual files is, why they were ultimately discarded, or why their Tei files were kept. We currently manually ignore all duplicate files except the ones in the official 84,000 reading room. Depending on why the duplicates are there, they may be useful for experiments such as deliberate insertion of ambiguity during training.
