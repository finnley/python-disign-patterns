# 声明一个 CashSuper 对象
class CashContext:
    # 通过构造方法，传入具体收费策略
    def __init__(self, csuper=None):
        self._cs = csuper

    # 根据收费策略的不同，获得计算结果
    def get_result(self, money):
        return self._cs.accept_cash(money)
