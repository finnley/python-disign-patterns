from operation import Operation

'''
Operation 加减乘除-除法类
'''
class OperationDiv(Operation):
    def GetResult(self):
        if self.GetNumberB == 0:
            print("除数不能为0")
        return self.GetNumberA() / self.GetNumberB()