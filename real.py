class Real:
    PRECISION = 60
    MAX_MANTISS = 10000
    MIN_MANTISS = -100

    def __init__(self, intFrom):
        # check int
        if not isinstance(intFrom, int):
            raise TypeError("Real cannot be created from non-int")
        # set sign
        self.sign = (1 if intFrom > 0 else -1)
        intFrom = abs(intFrom)
        # check mantiss
        self.mantiss = len(str(intFrom))
        if self.mantiss > Real.MAX_MANTISS:
            raise OverflowError("Real: Creation overflow")
        # check zero
        if intFrom == 0 or self.mantiss < Real.MIN_MANTISS:
            self.zero = True
            return
        self.zero = False
        # set value
        self.val = int(str(intFrom)[:Real.PRECISION])
        while len(str(self.val)) < Real.PRECISION:
            self.val *= 10

    def copy(self):
        if self.zero:
            return Real(0)
        res = Real(1)
        res.val = self.val
        res.sign = self.sign
        res.mantiss = self.mantiss
        res.zero = self.zero
        return res

    def get_proper_zero(self):
        if self.val == 0 or self.mantiss < Real.MIN_MANTISS:
            return Real(0)
        return self.copy()

    def __truediv__(self, other):
        # check zero
        if self.zero:
            return Real(0)
        if other.zero:
            raise ZeroDivisionError("Real: Division by zero")
        # set sign and mantiss
        res = Real(1)
        res.sign = self.sign * other.sign
        res.mantiss = self.mantiss - other.mantiss + 1
        # move until first is bigger
        val1, val2 = self.val, other.val
        while val1 < val2:
            res.mantiss -= 1
            val1 *= 10
        # divide
        res.val = 0
        while len(str(res.val)) < Real.PRECISION:
            res.val = res.val * 10 + val1 // val2
            val1 = (val1 - val2 * (val1 // val2)) * 10
        return res.get_proper_zero()

    def __add__(self, other):
        # check zero
        if self.zero:
            return other.copy()
        if other.zero:
            return self.copy()
        # calculate result
        minMantiss = min(self.mantiss, other.mantiss)
        res = Real(self.sign * self.val * (10 ** (self.mantiss - minMantiss)) + other.sign * other.val * (10 ** (other.mantiss - minMantiss)))
        if res.zero:
            return res
        res.mantiss -= Real.PRECISION
        res.mantiss += minMantiss
        return res.get_proper_zero()

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        # check zero
        if self.zero or other.zero:
            return Real(0)
        # calculate result
        res = Real(self.val * other.val)
        res.sign = self.sign * other.sign
        res.mantiss -= Real.PRECISION * 2
        res.mantiss += self.mantiss + other.mantiss
        return res.get_proper_zero()

    def sqrt(self):
        # check zero
        if self.zero:
            return Real(0)
        # check negative
        if self.sign == -1:
            raise Exception("Real: Sqrt(negative)")
        # iterate until get result
        guess = Real(1)
        lastVal = Real(0)
        while lastVal != guess:
            lastVal = guess.copy()
            guess = (self / guess + guess) / Real(2)
        return guess

    def atan(self):
        # check zero
        if self.zero:
            return self.copy()
        # some cases
        if self.sign == -1:
            return -(-self).atan()
        if self > Real(1):
            return Real.PI / Real(2) - (Real(1) / self).atan()
        if self > Real(1) / Real(2):
            b = Real(1) / Real(3).sqrt()
            return ((self - b) / (Real(1) + self * b)).atan() + Real.PI / Real(6)
        # iterate until get result
        res = self.copy()
        self_squared = self * self
        current_power_of_self = self.copy()
        b = 1
        for i in range(1, 100):
            current_power_of_self *= self_squared
            res = res + Real(-1 if i%2 else 1) * current_power_of_self / Real(2 * i + 1)
        return res

    def asin(self):
        # some cases
        if self >= Real(1):
            return Real.PI / Real(2)
        if self <= Real(-1):
            return -Real.PI / Real(2)
        # calculate from atan
        return (self / (Real(1) - self * self).sqrt()).atan()

    def acos(self):
        return Real.PI / Real(2) - self.asin()

    def __neg__(self):
        if self.zero:
            return Real(0)
        res = self.copy()
        res.sign = -self.sign
        return res

    def abs(self):
        if self.zero or self.sign == 1:
            return self.copy()
        return -self

    def __repr__(self):
        if self.zero:
            return "0." + "0" * Real.PRECISION
        res = ("" if self.sign > 0 else "-")
        if self.mantiss <= 0:
            res += "0."
            res += "0" * (-self.mantiss) + str(self.val)
        elif self.mantiss > len(str(self.val)):
            res += str(self.val)
            res += "0" * (self.mantiss - len(str(self.val)))
        else:
            res += str(self.val)[:self.mantiss]
            res += "."
            res += str(self.val)[self.mantiss:]
        return res

    def __eq__(self, other):
        return self.zero == other.zero and self.mantiss == other.mantiss and self.val == other.val and self.sign == other.sign

    def __neq__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self != other and (self - other).sign == -1

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return not(self > other)

    def __ge__(self, other):
        return not(self < other)

Real.PI = ((Real(5).sqrt() - Real(1)) / Real(4)).asin() * Real(10)

if __name__ == "__main__":
    import math
    print(123 / 9977)
    print(Real(123) / Real(9977))

    print(-445 + 440)
    print(Real(-445) + Real(440))

    print(1334 * 23)
    print(Real(1334) * Real(23))

    print(math.sqrt(1234))
    print(Real(1234).sqrt())

    print(math.acos(9999999999998/10000000000000))
    print((Real(9999999999998)/Real(10000000000000)).acos())

