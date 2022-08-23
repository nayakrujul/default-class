class StrAndRepr:
    def __str__(self):
        ret = f'{type(self).__name__}('
        for i, (k, v) in enumerate(self.__dict__.items()):
            ret += f'{k}={v!r}'
            if i < len(self.__dict__) - 1:
                ret += ', '
        return ret + ')'
    def __repr__(self):
        return str(self)
    
class Comparisons:
    def __eq__(self, x):
        try:
            return not self != x
        except:
            return not (self < x or self > x)
    def __ne__(self, x):
        try:
            return not self == x
        except:
            return self < x or self > x
    def __gt__(self, x):
        try:
            return not self <= x
        except:
            return self >= x and not self == x
    def __ge__(self, x):
        try:
            return not self < x
        except:
            return self > x or self == x
    def __lt__(self, x):
        try:
            return not self >= x
        except:
            return self <= x and not self == x
    def __le__(self, x):
        try:
            return not self > x
        except:
            return self < x or self == x

class Numeric(StrAndRepr, Comparisons):
    def __add__(self, x):
        return self - (-x)
    def __radd__(self, x):
        return self + x
    def __sub__(self, x):
        return - (x - self)
    def __rsub__(self, x):
        return - (self - x)
    def __mul__(self, x):
        return x * self
    def __rmul__(self, x):
        return self * x
    def __truediv__(self, x):
        return 1 / (x / self)
    def __rtruediv__(self, x):
        return 1 / (self / x)
    def __floordiv__(self, x):
        return type(self)(int(self / x))
    def __rfloordiv__(self, x):
        return type(self)(int(x / self))
    def __mod__(self, x):
        return self - (self // x) * x
    def __rmod__(self, x):
        return x - (x // self) * self
    def __divmod__(self, x):
        return self // x, self % x
    def __rdivmod__(self, x):
        return x // self, x % self
    def __pos__(self):
        return self
    def __neg__(self):
        return 0 - self
