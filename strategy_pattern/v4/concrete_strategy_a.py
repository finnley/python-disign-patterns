import strategy


# ConcreteStrategy 创装了具体的算法或行为，继承与 Strategy
class ConcreteStrategyA(strategy.Strategy):
    # 算法A实现方法
    def algorithm_interface(self):
        print("算法A实现")
