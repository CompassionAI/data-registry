# Card: OpenPecha-kangyur-old

## Summary

The Derge edition of the Kangyur, with annotated proofreader comments. Documentation of the comments is [here](https://github.com/OpenPecha/P000001/blob/master/docs/README.md).

## Source

Unfortunately, it seems that Esukhia completely removed this version of the dataset.

## Ingestion tools

Use the KangyurLoader class in the CompassionAI/common repo, in the file _/cai_common/data/open_pecha_loaders.py_.

Code sample:

```python
# You need a local Dask cluster for all CompassionAI datasets
from dask.distributed import Client, LocalCluster
dask_cluster = LocalCluster(n_workers=10, threads_per_worker=1)
dask_client = Client(dask_cluster)

# Data location comes from the CAI_DATA_BASE_PATH environment variable
from cai_common.data import KangyurLoader
kangyur_df = KangyurLoader().dataframe
```

## CompassionAI comments

There is a newer version of this dataset: <https://github.com/Esukhia/derge-tengyur>. This was the original dataset we used for the monolingual AlBERT, so we archive it.
