---
kernelspec:
    name: python
    display_name: Python 3
---
# SMART-HALO

*Platform link*

*Campaign links*

## Data sets

```{code-cell} python
:tag: [remove-input]
from pathlib import Path
from pangaeapy import PanQuery 

keywords = ['project:AC3', 'SMART', 'HALO', 'project:SPP1294']
query = ', '.join(keywords)
result = PanQuery(query)
dois = result.get_doi()

source = Path().parent
text = "\n".join(f"- []({doi})" for doi in dois)
build_folder = source / "_build/tmp"
build_folder.mkdir(exist_ok=True, parents=True)
_ = (build_folder / "smart_halo.txt").write_text(text)
```

```{include} ../_build/tmp/smart_halo.txt
```

## Example notebooks

@smart1