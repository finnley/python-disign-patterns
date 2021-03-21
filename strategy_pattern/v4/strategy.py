from abc import ABCMeta, abstractmethod


# 抽象算法类
# Strategy类，定义所有支持的算法公共接口
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def algorithm_interface(self):
        pass
