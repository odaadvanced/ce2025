Jupyter QtConsole 5.4.0
Python 3.11.2 (main, Nov 30 2024, 21:22:50) [GCC 12.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.5.0 -- An enhanced Interactive Python. Type '?' for help.

# 05_03_converters_final
class ScaleConverter:

    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def description(self):
        return "Convert " + self.units_from + " to " + self.units_to

    def convert(self, value):
        return value * self.factor


class ScaleAndOffsetConverter(ScaleConverter):

    def __init__(self, units_from, units_to, factor, offset):
        ScaleConverter.__init__(self, units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):
        return value * self.factor + self.offset


c1 = ScaleConverter("inches", "mm", 25)
print(c1.description())
print("converting 2 inches")
print(str(c1.convert(2)) + c1.units_to)

c2 = ScaleAndOffsetConverter("C", "F", 1.8, 32)
print(c2.description())
print("converting 20C")
print(str(c2.convert(20)) + c2.units_to)
Convert inches to mm
converting 2 inches
50mm
Convert C to F
converting 20C
68.0F

c2 = ScaleConverter('feet', 'yards', 0.333)



c2 = ScaleConverter('feet', 'yards', 0.333)

print(strc2.convert3)) + c2.units_to)
  Cell In [4], line 1
    print(strc2.convert3)) + c2.units_to)
                         ^
SyntaxError: unmatched ')'


print(str(c2.convert3)) + c2.units_to)
  Cell In [5], line 1
    print(str(c2.convert3)) + c2.units_to)
                                         ^
SyntaxError: unmatched ')'


print(str(c2.convert(3)) + c2.units_to)
0.9990000000000001yards

print(str(c2.convert(10)) + c2.units_to)
3.33yards
