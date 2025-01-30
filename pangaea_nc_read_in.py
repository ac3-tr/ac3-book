#!/usr/bin/env python
"""
| *author*: Johannes Röttenbacher
| *created*: 24.01.2025

Query the PANGAEA server for all AC3 datasets
"""
import fsspec
import pandas as pd
import pangaeapy
import xarray as xr

CACHE_DIR = "E:/tmp/pangaea-cache"

caching_fs = fsspec.filesystem(
    "filecache",
    target_protocol="https",  # The protocol for the URL
    cache_storage=CACHE_DIR,  # Local cache directory
    same_names=True,
    expiry_time=False,
)


ac3_datasets = pangaeapy.PanQuery('project:label:AC3, CCP')
# the maximum number of datasets returned per query is 500
#TODO: loop over totalcount with 500 step size
dataset_id = 956151
#TODO: Handle Collections
# dataset_id = 963771
ds = pangaeapy.PanDataSet(dataset_id, enable_cache=True)
if ds.isCollection:
    print('We have a dataset collection\nUse first dataset in collection')
    ds = pangaeapy.PanDataSet(ds.collection_members[0])
if 'Binary' in ds.data:
    print('NetCDF found')
    # generate download link for each dataset
    filenames = ds.data['Binary']
    urls = list()
    for fn in filenames:
        url = f'https://download.pangaea.de/dataset/{dataset_id}/files/{fn}'
        urls.append(url)
    ds.data['url'] = urls

time_sel = ds.data['Date/Time'].dt.date == pd.to_datetime('2022-04-11').date()
ds_sel = ds.data[time_sel]

# Open the remote file (will cache it locally)
cached_file_path = caching_fs.open(ds_sel.url.iloc[0]).name

print(f"File downloaded and cached locally: {cached_file_path}")

data = xr.open_dataset(cached_file_path)


