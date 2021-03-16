from operation import Operation

'''
Operation 加减乘除-加法类
'''
class OperationAdd(Operation):
    def GetResult(self):
        return self.GetNumberA() + self.GetNumberB()