#!/usr/bin/env python
# coding: utf-8

# ---
# authors:
#     - MB
#     - JR
# title: Short Byte - Adding metadata to a netCDF file
# label: shortbyte
# downloads:
#   - file: ac3_shortbyte_netcdf_metadata.ipynb
#     title: Source File
# ---
# 
# 
# Author(s) of this notebook:
#  - *Johannes Röttenbacher*, [*Institute for Environmental Physics*](https://www.iup.uni-bremen.de/eng/), *Otto-Hahn-Allee 1, 28359 Bremen*, *jroettenbacher@iup.physik.uni-bremen.de*
# 
# This notebook is licensed under the [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/ "CC-BY-4.0")

# ## Adding metadata to a netCDF file
# 
# In meteorology and other earth sciences good data sets come with a wealth of metadata, which tells the story of the data set and gives meaningful insight in its properties.
# The most simple form of metadata is adding a unit to a measurement variable.
# One challenge is to keep data and metadata connected in a machine-readable format.
# The [network common data format (netCDF)](https://www.unidata.ucar.edu/software/netcdf) is designed just for this purpose.
# It is well established and all major programming languages have a good interface for it.
# In python the [xarray](https://docs.xarray.dev/en/stable/) module handles netCDF files with ease and makes working with them fast and simple.
# 
# In this Short Byte we will show you how to add meaningful metadata to a data set and give you a few global attributes, which you should always add to your data sets.

# ### Import relevant modules
# 
# Let's start by importing the relevant modules.

# In[12]:


import datetime
import numpy as np
import xarray as xr


# ## Creating some data
# 
# Let's mock up a data set with two variables one for the spectral solar downward irradiance and one for the spectral solar upward irradiance.
# Say the data was recorded at 1 Hz frequency at a ground station somewhere in Germany.
# Thus, we have a time dimension and, since we assume spectral measurements, a wavelength dimension.
# Our instrument can measure from 350nm to 900nm in 2nm steps.
# We assume 24 hours of measurements and simulate a clear sky day with half of a sine wave.

# In[13]:


start_date = datetime.datetime(2025, 7, 1)
end_date = datetime.datetime(2025, 7, 2)
timesteps = xr.date_range(start_date, end_date, freq='s', inclusive='left')
n_time = len(timesteps)  # number of measurements
# create x values for sine function
x = np.linspace(0, np.pi, n_time)

# create wavelength dimension
wavelengths = np.arange(350, 900, 2)
n_wavelengths = len(wavelengths)  # number of wavelengths

# weight each wavelength with a sine wave as the sun does not emit each wavelength equally
weighting = np.sin(np.linspace(0.2, 0.8 * np.pi, n_wavelengths))

# initialize arrays
fdw = np.zeros((n_time, n_wavelengths))
fup = np.zeros((n_time, n_wavelengths))

for i in range(n_wavelengths):
    fdw[:, i] = np.sin(x) * 800 * weighting[i]  # we scale to a maximum of 800 W/m2
    fup[:, i] = np.sin(x) * 800 * 0.3 * weighting[i]  # we assume an average reflectance of 30%


# Now that we have the basic arrays set up we can combine them in a xarray data array.
# For this we need to define the dimensions of our data and add a coordinate to each dimension.

# In[14]:


fdw = xr.DataArray(data=fdw,
                   coords=(timesteps, wavelengths),
                   dims=('time', 'wavelength'),
                   )
fup = xr.DataArray(data=fup,
                   coords=(timesteps, wavelengths),
                   dims=('time', 'wavelength'),
                   )


# Let's take a look at our data array and think about what metadata we would need to add still

# In[15]:


fdw


# ## Adding metadata
# 
# We already chose "talking" coordinate names but a reader would have now idea what unit our variables and coordinates are in.
# The easiest way to add metadata, so-called attributes in netCDF, to our Data Arrays is by creating a data set from them and using dictionaries with the variable names.
# 
# Each variable should at least have a `units` attribute and either or both a `standard_name` and a `long_name`.
# Standard names are defined in the Climate Forecast (CF) Conventions Standard Name Table (https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html), which you can search for `solar irradiance`.
# 
# Be aware that not every variable has a `standard_name`.
# In that case use a descriptive `long_name`.
# 
# Since we are dealing with spectral data, we can use the standard name `solar_irradiance_per_unit_wavelength`, which has a canonical unit of `W m-2 m-1`.
# Thus, we need to convert our nanometer wavelength to meter.

# In[16]:


ds = xr.Dataset(dict(fdw=fdw, fup=fup))
ds['wavelength'] = ds.wavelength * 10**-9
ds


# Although coordinates and variables are named differently in the view above we can still think of coordinates as variables and add their metadata in the same dictionary.

# In[17]:


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
        units=f'seconds since {start_date}',
        calendar='standard',
    )
)


# You notice that the units attribute of the time coordinate is not an SI unit but rather a reference time.
# We use the start of day as a reference time so we don't need to worry about leap seconds here.
# The `calendar` attribute is another important piece of metadata.
# You can read more about it here: https://cfconventions.org/cf-conventions/cf-conventions#calendar
# 
# Let's add those attributes to the variables in the data set.

# In[18]:


for var in ds.variables:
    ds[var].attrs = var_attrs[var]

ds


# ## Global metadata
# 
# We added the variable attributes but there is also an option to add global attributes, and you should use that to tell the user more about the data set itself.
# Who made it? How was it made? What license is it under?
# 
# Here is a selection of attributes you can use.
# Most importantly the `Conventions` attribute should always be present telling the user, which version of the CF conventions are used for the data set.
# Currently (2026-01-12) we are at version 1.13, which did a lot of clarification when it comes to calendars and time.

# - `Conventions: CF-1.13`
#   Check https://cfconventions.org/ for the current version.
# - `title:`
#   Short description of the data set contents.
# - `description:`
#    Long or short description of the data set.
# - `comment:`
#    Miscellaneous information about the data or methods used to produce it (can be replaced by description).
# - `source:`
#   The method of production of the original data. If it was model-generated, **`source`** should name the model and its version, as specifically as could be useful. If it is observational, **`source`** should characterize it (e.g., "**`surface observation`**" or "**`radiosonde`**").
# - `references:`
#   Published or web-based references that describe the data or methods used to produce it.
# - `license: CC-BY-4.0`
#   Recommended, chose other if you need.
# - `project:`
#    If you work within a project make sure to name it here and also the funding.
# - `institution:`
#   Where the original data was produced.
# - `author(s): `
#   Who contributed and/or created the data set.
# - `contact: Your ORCID`
#   ORCID should be the best place to find your current e-mail address.
# - `version:`
#   Optional, as Zenodo and other publishers also keep track of your version. Make sure it is the same as the one given to you by the repository (Zenodo starts with v1) where you publish the data
# - `history: yyyy-mm-dd HH:MM python created file for publishing` Provides an audit trail for modifications to the original data. Well-behaved generic netCDF filters will automatically append their name and the parameters with which they were invoked to the global history attribute of an input netCDF file. We recommend that each line begin by indicating the date and time of day that the program was executed.
# - `featureType: profile`
#   Specifies the type of discrete sampling geometry to which the data in the scope of this attribute belongs, and implies that all data variables in the scope of this attribute contain collections of features of that type. (See https://cfconventions.org/cf-conventions/cf-conventions#discrete-sampling-geometries)

# For our data set we stick to a minimum.

# In[19]:


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
ds


# ## Attributes as variables
# 
# Up till now we only added metadata as attributes.
# However, we haven't specified the location of our measurement site yet.
# We can do this with attributes, but it makes more sense to use variables for this in case we want to merge our data set with another stations data in the future.
# So let's add latitude, longitude and altitude.

# In[20]:


lat, lon, height_above_msl, height_above_ground = 47.801274, 11.009044, 960, 2
ds['latitude'] = xr.DataArray(data=lat,
                              attrs=dict(
                                  units='degree_north',
                                  standard_name='latitude',
                                  long_name='Station latitude',)
                              )
ds['longitude'] = xr.DataArray(data=lon,
                               attrs=dict(
                                   units='degree_east',
                                   standard_name='longitude',
                                   long_name='Station longitude',)
                               )
ds['height_above_msl'] = xr.DataArray(data=height_above_ground,
                                      attrs=dict(
                                          units='m',
                                          standard_name='height_above_mean_sea_level',)
                                      )
ds['height_above_ground'] = xr.DataArray(data=height_above_ground,
                                         attrs=dict(
                                             units='m',
                                             standard_name='height',
                                             long_name='Height of measurement device above ground',)
                                         )
ds


# As you can see, we did not add any dimension to these variables as they are not dependent on any.

# ## Conclusion
# 
# This is it for this Short Byte. Comparing our initial data with the final data set, which one would you prefer to work with?
# Surely, the added metadata makes it easier to understand the data set and make sense of it.
# 
# You should now have a few more ideas and tools on how to enrich your data set with essential metadata and make use of the netCDF data format.
# In another Short Byte we will look at saving this data set to disk, such that it can be easily read in again.
