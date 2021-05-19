# 4 classes that can be used for unique sets of names: Enum, IntEnum, Flag, IntFlag
# Enum = base class for creating enumerated constants
# IntEnum = subclasses of Int
# IntFlag = can be combined using bitwise operations without losing IntFlag membership. Subclass of Int
# Flag = combined without losing Flag membership

from enum import Enum, auto


class Colors (Enum):  # Color = enumeration
    RED = 'red'  # RED = enumeration member
    GREEN = 'green'  # GREEN has name=GREEN and value='green'
    BLUE = 'blue'


class CustomValue (Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name[-1]

    TEST = auto()
    BAM = auto()
    BIM = auto()  # BIM gets the same value as BAM and so it becomes a reference to it. BIM is not present when
    # iterating but it will be there as an alias to BAM


# Functional API way of defining enums at runtime
Flower = Enum('Flower', 'ROSE TULIP')
print(Flower.ROSE)

print(Colors.RED.name)
print(Colors.RED.value)

for flower in Flower:
    print(flower)

print(Flower)

for custom in CustomValue:
    print(custom.value)

print(CustomValue.BIM)
print(CustomValue.BAM)
