# Class - 28

## Today's Topic
- Built-in modules (math, random, datetime), pip
  - (math)[https://docs.python.org/3/library/math.html]
  - (random)[https://docs.python.org/3/library/random.html]
  - (datetime)[https://docs.python.org/3/library/datetime.html]
- (pip)[https://pip.pypa.io/en/stable/]

## Notes
- Module, Package, Library

## Import
1. import <module>
2. import <module> as <alias>
3. from <module> import <function>
4. from <module> import <function> as <alias>
5. from <module> import * 

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
- Command to uninstall a package: `pip uninstall package_name`
- List installed packages: `pip list`
