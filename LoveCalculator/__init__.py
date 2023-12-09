from .Calculator import LoveCalc, ChangeToInteger, WhichIsGreater

__version__ = "1.0.1"
def BestLoveCalc(input1, input2):
    value1 = LoveCalc(input1, input2)
    value2 = LoveCalc(input2, input1)
    return WhichIsGreater(ChangeToInteger(value1), ChangeToInteger(value2))

def NormalLoveCalc(input1, input2):
    return LoveCalc(input1, input2)