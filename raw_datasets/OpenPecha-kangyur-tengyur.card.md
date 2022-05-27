# Card: OpenPecha-kangyur-tengyur

## Summary

The Derge editions of the Kangyur and Tengyur, with annotated proofreader comments. Documentation of the comments is [here](https://github.com/OpenPecha/P000001/blob/master/docs/README.md).

## Source

<https://github.com/OpenPecha/P000001>

## Ingestion tools

Use the classes KangyurLoader and TengyurLoader in the CompassionAI/common repo, in the file _/cai_common/data/open_pecha_loaders.py_.

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

There may be a newer version of this dataset: <https://github.com/Esukhia/derge-tengyur>. There are some differences in the annotations, it may not be worth it to redo the cleaning code.
