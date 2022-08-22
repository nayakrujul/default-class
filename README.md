# default-class
The default_class library in Python

## Installation

```
$ pip install default-class
```

## Usage

#### The `Numeric` class in the `default_class` library uses arithmatic rules to define magic methods.

See this example:

```python
from default_class import Numeric

class Number(Numeric):
    def __init__(self, n):
        self.n = n
        if isinstance(n, Number):
            self.n = n.n
    def __int__(self):
        return int(self.n)
    def __sub__(self, x):
        return Number(self.n - x)
    def __mul__(self, x):
        return Number(self.n * x)
    def __rtruediv__(self, x):
        return Number(x / self.n)
    def __neg__(self):
        return Number(-self.n)
```

Here, only 5 magic methods (`__int__`, `__sub__`, `__mul__`, `__rtruediv__` and `__neg__`) have been defined, but the Numeric class fills in 14 others. See below:

```python
num = Number(123)

print(num)
print(num + 5)
print(5 + num)
print(1000 - num)
print(5 * num)
print(num / 5)
print(num // 5)
print(1000 // num)
print(num % 5)
print(1000 % num)
print(divmod(num, 5))
print(divmod(1000, num))
print(+num)
```

Output:

```python
Number(n=123)
Number(n=128)
Number(n=128)
Number(n=877)
Number(n=615)
Number(n=24.6)
Number(n=24)
Number(n=8)
Number(n=3)
Number(n=16)
(Number(n=24), Number(n=3))
(Number(n=8), Number(n=16))
Number(n=123)
Number(n=-123)
```

#### The `Numeric` class can fill in these magic methods:

* `__str__` (no dependencies)
* `__repr__` (needs `__str__`)
* `__add__` (needs `__sub__` and `__neg__`)
* `__radd__` (needs `__add__`)
* `__sub__` (needs `__neg__` and `__rsub__`)
* `__rsub__` (needs `__neg__` and `__sub__`)
* `__mul__` (needs `__rmul__`)
* `__rmul__` (needs `__mul__`)
* `__truediv__` (needs `__rtruediv__`)
* `__floordiv__` (needs `__int__` and `__truediv__`)
* `__rfloordiv__` (needs `__int__` and `__rtruediv__`)
* `__mod__` (needs `__sub__`, `__floordiv__` and `__mul__`)
* `__rmod__` (needs `__rsub__`, `__rfloordiv__` and `__rmul__`)
* `__divmod__` (needs `__floordiv__` and `__mod__`)
* `__rdivmod__` (needs `__rfloordiv__` and `__rmod__`)
* `__pos__` (no dependencies)
* `__neg__` (needs `__sub__`)

#### Note: if not enough requirements are met, this could result in a `RecursionError`
