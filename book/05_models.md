# Models

Within (AC)³ a host of different models are used on all scales.

## libRadtran

[libRadtran](http://www.libradtran.org/) is a freely available *library for radiative transfer* calculations [@mayer2005; @emde2016]. Its main tool, `uvspec`, solves the radiative transfer equation through a user-defined atmosphere and returns spectral or broadband solar and thermal irradiances and radiances. It is widely used within (AC)³ to provide the **cloud-free reference** needed to derive cloud radiative effects from airborne and ground-based irradiance observations — for example in the seasonal Fram-Strait study of @becker2023.

The example notebook [](#libradtran-cre-example) shows how to drive libRadtran from Python with [`pyRadtran`](https://github.com/FranzFlink/pyRadtran) to reproduce the solar cloud radiative effect over Arctic sea ice and open ocean.
