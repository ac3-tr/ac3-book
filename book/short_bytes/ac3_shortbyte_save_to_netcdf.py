# %% [markdown]
# ---
# authors:
#     - JR
# title: Short Byte - Saving to NetCDF
# label: shortbyte02
# downloads:
#   - file: ac3_shortbyte_save_to_netcdf.ipynb
#     title: Jupyter Notebook
#   - file: ac3_shortbyte_save_to_netcdf.py
#     title: Python Script
# ---
# 
# Author(s) of this notebook:
#  - *Johannes Röttenbacher*, [*Institute for Environmental Physics*](https://www.iup.uni-bremen.de/eng/), *Otto-Hahn-Allee 1, 28359 Bremen*, *jroettenbacher@iup.physik.uni-bremen.de*
# 
# This notebook is licensed under the [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/ "CC-BY-4.0")
# %% [markdown]
# ## Saving to netCDF in python
# 
# In meteorology and other earth sciences good data sets come with a wealth of metadata, which tells the story of the data set and gives meaningful insight in its properties.
# The most simple form of metadata is adding a unit to a measurement variable.
# One challenge is to keep data and metadata connected in a machine-readable format.
# The [Network common data format (NetCDF)](https://www.unidata.ucar.edu/software/netcdf) is designed just for this purpose.
# It is well established and all major programming languages have a good interface for it.
# In python the [xarray](https://docs.xarray.dev/en/stable/) module handles NetCDF files with ease and makes working with them fast and simple.
# 
# In this Short Byte we will show you how to save a data set to a netCDF file on disk, while keeping all the important metadata encoded in the file.
# %% [markdown]
# ### Import relevant modules
# 
# Let's start by importing the relevant modules.
# You should also install the `netcdf4` module in your environment, as this is needed for saving a NetCDF file to disk.
# %%
import datetime
import numpy as np
import xarray as xr
# %% [markdown]
# ## Creating some data
# 
# In [another Short Byte](./ac3_shortbyte_netcdf_metadata.ipynb) we created some data and added meaningful metadata to it.
# Here we are reusing this data set.
# Thus, we need to run the complete code of the other notebook first.
# %%
start_date = datetime.datetime(2025, 7, 1)
end_date = datetime.datetime(2025, 7, 2)
timesteps = xr.date_range(start_date, end_date, freq='s', inclusive='left')
n_time = len(timesteps)  # number of measurements
x = np.linspace(0, np.pi, n_time)
wavelengths = np.arange(350, 900, 2)
n_wavelengths = len(wavelengths)  # number of wavelengths
weighting = np.sin(np.linspace(0.2, 0.8 * np.pi,
                               n_wavelengths))  # weight each wavelength with a sine wave as the sun does not emit each wavelength equally
# initialize arrays
fdw = np.zeros((n_time, n_wavelengths))
fup = np.zeros((n_time, n_wavelengths))

for i in range(n_wavelengths):
    fdw[:, i] = np.sin(x) * 800 * weighting[i]  # we scale to a maximum of 800 W/m2
    fup[:, i] = np.sin(x) * 800 * 0.3 * weighting[i]  # we assume an average reflectance of 30%

fdw = xr.DataArray(data=fdw,
                   coords=(timesteps, wavelengths),
                   dims=('time', 'wavelength'),
                   )
fup = xr.DataArray(data=fup,
                   coords=(timesteps, wavelengths),
                   dims=('time', 'wavelength'),
                   )
ds = xr.Dataset(dict(fdw=fdw, fup=fup))
ds['wavelength'] = ds.wavelength * 10 ** -9

var_attrs = dict(
    fdw=dict(
        units="W m-2 m-1",
        standard_name="solar_irradiance_per_unit_wavelength",
        long_name="solar downward irradiance",
    ),
    fup=dict(
        units="W m-2 m-1",
        standard_name="solar_irradiance_per_unit_wavelength",
        long_name="solar upward irradiance",
    ),
    wavelength=dict(
        units='m',
        standard_name='radiation_wavelength',
        long_name='radiation wavelength',
    ),
    time=dict(
        standard_name='time',
        # xarray sets this automatically since we are using datetimes already
        # and throws an error if this is manually defined
        # If you want to define this manually you need to use float or int for your time variable
        # units=f'seconds since {start_date}',
        # calendar='standard',
    )
)

for var in ds.variables:
    ds[var].attrs = var_attrs[var]

global_attrs = dict(
    Convention=1.13,
    title='Solar irradiance at measurement site',
    description='One day of measurements of solar downward and upward spectral irradiance',
    source='Surface observations with a radiometer type xyz',
    contact='ORCID',
    license='CC-BY-4.0',
    authors='Firstname Lastname',
)

ds.attrs = global_attrs
lat, lon, height_above_msl, height_above_ground = 47.801274, 11.009044, 960, 2
ds['latitude'] = xr.DataArray(
    data=lat,
    attrs=dict(
        units='degree_north',
        standard_name='latitude',
        long_name='Station latitude', )
)
ds['longitude'] = xr.DataArray(
    data=lon,
    attrs=dict(
        units='degree_east',
        standard_name='longitude',
        long_name='Station longitude', )
)
ds['height_above_msl'] = xr.DataArray(
    data=height_above_ground,
    attrs=dict(
        units='m',
        standard_name='height_above_mean_sea_level', )
)
ds['height_above_ground'] = xr.DataArray(
    data=height_above_ground,
    attrs=dict(
        units='m',
        standard_name='height',
        long_name='Height of measurement device above ground', )
)
ds

# %% [markdown]
# Now that we have the data set, let's talk about how to write it to a file.
# We are using `xarray` again for this task, specifically the `to_netcdf()` function.
# Thus, we are going through the arguments of this function step by step.
# 
# The `path` argument is pretty self-explanatory, just chose a directory and name for your file.
# 
# If there already is a file there and you only want to update its content, setting `mode` to `a` is the way to go.
# Otherwise, just use the default and overwrite any existing files.
# 
# Now we need to decide which NetCDF version we are going to use. We set this with the `format` argument.
# 
# From the `xarray` [documentation](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.to_netcdf.html):
# > format ({"NETCDF4", "NETCDF4_CLASSIC", "NETCDF3_64BIT", "NETCDF3_CLASSIC"}, optional) – File format for the resulting netCDF file:
# >   - NETCDF4: Data is stored in an HDF5 file, using netCDF4 API features.
# >   - NETCDF4_CLASSIC: Data is stored in an HDF5 file, using only netCDF 3 compatible API features.
# >   - NETCDF3_64BIT: 64-bit offset version of the netCDF 3 file format, which fully supports 2+ GB files, but is only compatible with clients linked against netCDF version 3.6.0 or later.
# >   - NETCDF3_CLASSIC: The classic netCDF 3 file format. It does not handle 2+ GB files very well.
# >
# >   All formats are supported by the netCDF4-python library. scipy.io.netcdf only supports the last two formats.
# >
# >   The default format is NETCDF4 if you are saving a file to disk and have the netCDF4-python library available. Otherwise, xarray falls back to using scipy to write netCDF files and defaults to the NETCDF3_64BIT format (scipy does not support netCDF4).
# 
# If you do not have any specific reason to use an older format sticking with the default `NETCDF4` is the best choice here.
# %% [markdown]
# We skip the `group` argument.
# Just know that NetCDF-4 introduced support for multiple groups in one file, which is sort of like having multiple NetCDF files in one file.
# 
# `engine` is another argument where we can stick to the default.
# %% [markdown]
# The `encoding` argument is something we need to discuss in more detail.
# First of there are two ways to set encodings, either handing a dictionary to the `encoding` argument of the `to_netcdf()` function or by setting the encoding attribute on a `xarray.Dataset` and leaving the `encoding` argument empty.
# 
# Let's take a look at our data set and add some encodings to it via the second way.
# 
# The two most common things to set via the encoding is the `_FillValue` of a variable, which `xarray` sets to `nan` by default, and the `scale_factor` and `add_offset` used to reduce the size of data on disk.
# 
# Especially, for coordinate variables a `_FillValue` does not really make sense as these should always be continuous.
# %%
encoding = dict()
for coord in ds.coords:
    encoding[coord] = dict(_FillValue=None)
# %% [markdown]
# We can also reduce the size of our data (a little) by converting our variables to integers and defining the number of significant digits with the `scale_factor`.
# Let's say our instrument can measure a difference of 0.01 W m-2 m-1.
# Then we could scale our data with that precision. We also need to specify an integer to use as `_FillValue`, since xarray uses nan, which is a float.
# 
# Another way to save some space is to add an offset to our data with the keyword `add_offset`.
# This only makes sense for data with negative values, because we then save one bit for each number, which is used to represent the -.
# Our data does not have negative values, but some physical data does (such as temperature in °C).
# For the cause of this exercise we will add an offset anyway.
# 
# Finally, we can also use a compression algorithm to reduce the size of the data by providing `zlib=True` in the encoding dictionary. For other compression algorithms check out the [documentation](https://docs.xarray.dev/en/latest/generated/xarray.Dataset.to_netcdf.html#xarray.Dataset.to_netcdf).
# %%
for var in ['fdw', 'fup']:
    encoding[var] = dict(dtype='int16',
                         scale_factor=0.01,
                         add_offset=100,
                         _FillValue=9999,
                         zlib=True)
# %% [markdown]
# We can now save the data to a netCDF file and define the encoding while doing that.
# To see if the size differs after the compression we save the data once with encoding and once without.
# %%
ds.to_netcdf('data_small.nc', encoding=encoding)
ds.to_netcdf('data.nc')
# %% [markdown]
# The resulting size difference is about a factor of 10, so it is definitely worth thinking about these options.
# %% [markdown]
# ## Conclusion
# 
# This is it for this Short Byte.
# Hopefully you got a good overview of how to use xarray to write your data to disk and use the simple packaging tools available with netCDF to reduce the size of your data without loosing any precision.