# Card: Esukhia-derge-tengyur

## Summary

The Derge edition of the Tengyur with proofread corrections, compiled by Esukhia. Documentation of the comments is [here](https://github.com/Esukhia/derge-tengyur/blob/master/README.md).

## Source

From the main branch in the [Esukhia Derge Tengyur GitHub repo](https://github.com/Esukhia/derge-tengyur).

## Ingestion tools

Use the TengyurLoader class in the CompassionAI/common repo, in the file _/cai_common/data/open_pecha_loaders.py_.

Code sample:

```python
# You need a local Dask cluster for all CompassionAI datasets
from dask.distributed import Client, LocalCluster
dask_cluster = LocalCluster(n_workers=10, threads_per_worker=1)
dask_client = Client(dask_cluster)

# Data location comes from the CAI_DATA_BASE_PATH environment variable
from cai_common.data import TengyurLoader
tengyur_df = TengyurLoader().dataframe
```

## CompassionAI comments

The release in the GitHub repo is in TEI format, which we have not yet converted to.
