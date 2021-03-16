from operation import Operation

'''
Operation 加减乘除-减法类
'''
class OperationSub(Operation):
    def GetResult(self):
        return self.GetNumberA() - self.GetNumberB()