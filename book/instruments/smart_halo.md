---
kernelspec:
    name: python
    display_name: Python 3
---
# SMART-HALO

Instrument paper: [](https://doi.org/c8jtzv)

:::: {grid} 3
:::{card}
:footer: Photo: Johannes Röttenbacher (CC BY 4.0)
![Top view image of the SMART irradiance inlet](../figures/HALO_SMART_top.JPG)
:::


::::

## Platforms

::::{grid} 3

![](#halo-card)

::::

## Campaigns

::::{grid} 3

![](#haloac3-card)

::::

## Data sets

```{code-cell} python
:tag: [remove-input]
from pathlib import Path
from pangaeapy import PanQuery 

keywords = ['project:AC3', 'SMART', 'HALO', 'project:SPP1294']
query = ', '.join(keywords)
result = PanQuery(query)
dois = result.get_dois()

source = Path().resolve().parent
text = "\n".join(f"- []({doi})" for doi in dois)
build_folder = source / "_build/tmp"
build_folder.mkdir(exist_ok=True, parents=True)
_ = (build_folder / "smart_halo.txt").write_text(text)
```

```{include} ../_build/tmp/smart_halo.txt
```

## Example notebooks

@smart1

@smart2