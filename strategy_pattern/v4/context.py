import strategy


# 上下文Context，用一个ConcreteStrategy来配置，维护一个对Strategy对象的引用
class Context:
    # 初始化时，传入具体的策略对象
    def __init__(self, strategy=None):
        self._strategy = strategy

    # 上下文接口
    # 根据具体的策略对象，调用其算法的方法
    def context_interface(self):
        self._strategy.algorithm_interface()
