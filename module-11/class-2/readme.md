# Class - 28

## Today's Topic
- Built-in modules (math, random, datetime), pip

## Relevant Notes with code examples in English

### Built-in Modules
Python standard library comes with built-in utility modules.

#### Math and Random
```python
import math
import random

print(math.sqrt(16))      # 4.0
print(random.randint(1, 10)) # Random integer between 1 and 10
```

#### Datetime
```python
from datetime import datetime
print(datetime.now()) # Current date and time
```

### PIP (Package Installer for Python)
`pip` is the package manager for Python modules.
- Command to install a package: `pip install package_name`
- List installed packages: `pip list`
