import abc

'''
Operation 运算类
'''
class Operation(metaclass=abc.ABCMeta):
    def GetNumberA(self):
        return self._numberA

    def SetNumberA(self, numberA):
        self._numberA = numberA

    def GetNumberB(self):
        return self._numberB

    def SetNumberB(self, numberB):
        self._numberB = numberB

    '''
        类似.net中的虚方法(virtual)，需要在具体类中重写
    '''
    @abc.abstractmethod
    def GetResult(self):
        return 0

