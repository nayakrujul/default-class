# default-class
The default_class library in Python

## Installation

```
$ pip install default-class
```

## Usage

### default_class.StrAndRepr

The StrAndRepr class gives better `__str__` and `__repr__` methods:

```python
from default_class import StrAndRepr

class Foo(StrAndRepr):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
obj = Foo(1, 'a', True)
print(obj)
```

Output:

```python
Foo(a=1, b='a', c=True)
```

### default_class.Comparisons

```python
from default_class import StrAndRepr, Comparisons

class String(StrAndRepr, Comparisons):
    def __init__(self, s):
        self.s = s
    def __eq__(self, x):
        return self.s == x
    def __lt__(self, x):
        return self.s in x

obj = String('abc')
print(obj <= 'bc') # False
print(obj > 'abcd') # False
print(obj >= 'bc') # True
print(obj != 'abcd') # True
```

### default_class.Numeric

The `Numeric` class in the `default_class` library uses arithmatic rules to define magic methods.

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

## Magic methods filled in

**StrAndRepr methods have no dependencies**

|Method|
|-|
|`__str__`|
|`__repr__`|

**Comparison methods have two sets of dependencies: either can be used**

|Method|Option 1|Option 2|
|-|-|-|
|`__eq__`|`__ne__`|`__gt__`, `__lt__`|
|`__ne__`|`__eq__`|`__gt__`, `__lt__`|
|`__gt__`|`__le__`|`__ge__`, `__eq__`|
|`__ge__`|`__lt__`|`__gt__`, `__eq__`|
|`__lt__`|`__ge__`|`__le__`, `__eq__`|
|`__le__`|`__gt__`|`__lt__`, `__eq__`|

**Numeric methods have one set of dependencies**

|Method|Dependencies|
|-|-|
|`__add__`|`__sub__`, `__neg__`|
|`__radd__`|`__add__`|
|`__sub__`|`__neg__`, `__rsub__`|
|`__rsub__`|`__neg__`, `__sub__`|
|`__mul__`|`__rmul__`|
|`__rmul__`|`__mul__`|
|`__truediv__`|`__rtruediv__`|
|`__floordiv__`|`__int__`, `__truediv__`|
|`__rfloordiv__`|`__int__`, `__rtruediv__`|
|`__mod__`|`__sub__`, `__floordiv__`, `__mul__`|
|`__rmod__`|`__rsub__`, `__rfloordiv__`, `__rmul__`|
|`__divmod__`|`__floordiv__`, `__mod__`|
|`__rdivmod__`|`__rfloordiv__`, `__rmod__`|
|`__pos__`|None|
|`__neg__`|`__sub__`|

**Warning: if not enough methods are filled in already, this could result in a `RecursionError`**

Note: `Numeric` inherits from both `StrAndRepr` and `Comparisons`
