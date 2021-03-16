from operation import Operation

'''
Operation 加减乘除-乘法类
'''
class OperationMul(Operation):
    def GetResult(self):
        return self.GetNumberA() * self.GetNumberB()