'''
    业务逻辑和界面逻辑分开
    Operation 运算类
'''
class Operation:
    # add
    def add(self, numberA, numberB):
        return str(float(numberA) + float(numberB))

    # subtract
    def subtract(self, numberA, numberB):
        return str(float(numberA) - float(numberB))

    # multiply
    def multiply(self, numberA, numberB):
        return str(float(numberA) * float(numberB))

    # divide
    def divide(self, numberA, numberB):
        if numberB != '0':
            return str(float(numberA) / float(numberB))
        else:
            return "除数不能为0"

    def switch(self, operate: str, numberA: float, numberB: float):
        switcher = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
        method = switcher.get(operate, "wrong operate")
        return method(numberA, numberB)

    @staticmethod
    def GetResult(numberA: float, numberB: float, operate: str) -> float:
        o = Operation()
        return o.switch(operate, numberA, numberB)
