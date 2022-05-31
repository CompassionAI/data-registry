# Card: 84000-parallel-sentences

## Summary

Parallel Tibetan-English sentences from the 84,000 translations, curated by the translators themselves. from 84,000 in Tei XML format.

## Source

<https://github.com/84000/data-translation-memory.git> master branch.

## Ingestion tools

Use the ParallelTMXLoader class in the CompassionAI/common repo, in the file _/cai_common/data/parallel_tmx_loader.py_.

Code sample:

```python
# You need a local Dask cluster for all CompassionAI datasets
from dask.distributed import Client, LocalCluster
dask_cluster = LocalCluster(n_workers=10, threads_per_worker=1)
dask_client = Client(dask_cluster)

# Data location comes from the CAI_DATA_BASE_PATH environment variable
from cai_common.data import ParallelTMXLoader
tmx_df = ParallelTMXLoader().dataframe
```

## CompassionAI comments (optional)

There is a lot of anglicized Sanskrit named entities in this dataset, many with long and esoteric names. 84,000 used to publish a glossary for mapping these names to their English meanings but the latest version appears to no longer be public.

The Tibetan sentences are grammatically ambiguous, especially gender, singular/plural, etc.

The sentences are mostly, but not always, in order. Concatenating consecutive sentences will usually, but not always, result in longer snippets from the original text.
