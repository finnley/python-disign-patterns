from operation_add import OperationAdd
from operation_sub import OperationSub
from operation_mul import OperationMul
from operation_div import OperationDiv

# 简单运算工厂类
class OperationFactory:
    @staticmethod
    def createOperate(operate):
        if operate == "+":
            return OperationAdd()
        if operate == "-":
            return OperationSub()
        if operate == "*":
            return OperationMul()
        if operate == "/":
            return OperationDiv()
