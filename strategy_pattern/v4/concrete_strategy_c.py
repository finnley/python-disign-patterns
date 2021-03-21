import strategy


# 具体算法C
class ConcreteStrategyC(strategy.Strategy):
    def algorithm_interface(self):
        print("算法C实现")
