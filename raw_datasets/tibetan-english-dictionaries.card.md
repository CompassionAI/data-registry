# Card: tibetan-english-dictionaries

## Summary

Several Tibetan-English dictionaries.

## Source

Obtained from <https://github.com/christiansteinert/tibetan-dictionary/tree/master/_input/dictionaries/public> on 07/19/2020.

## Ingestion tools

Use the class TibetanDict in the CompassionAI/common repo, in the file _/cai_common/dict/dict.py_.

Code sample:

```python
# You need a local Dask cluster for all CompassionAI datasets
from dask.distributed import Client, LocalCluster
dask_cluster = LocalCluster(n_workers=10, threads_per_worker=1)
dask_client = Client(dask_cluster)

# Data location comes from the CAI_DATA_BASE_PATH environment variable
from cai_common.dict import TibetanDict, TibetanEncoding
dict_ = TibetanDict(default_encoding=TibetanEncoding.UNICODE)
dict_["ཆུང་བ"]
```

## CompassionAI comments

This dataset is very dirty:

- Many dictionaries have many English candidates for a Tibetan word, potentially very many, especially for particles.
- Some dictionaries include long explanations of esoteric Tibetan terms.
- Some dictionaries are very short, probably are not really dictionaries.

There is no obvious universal part-of-speech tagging.
