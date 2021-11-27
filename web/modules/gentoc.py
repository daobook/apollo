from pathlib import Path

template = r'''# NAME

```{toctree}
:maxdepth: 3
:glob:

../../modules/NAME/*
../../modules/NAME/**/*
```
'''


def ctx(name):
    return template.replace('NAME', name)


for path in Path('.').glob('*.md'):
    with open(path, 'w') as f:
        name = path.name[:-3]
        if name == 'index':
            continue
        else:
            f.write(ctx(name))
