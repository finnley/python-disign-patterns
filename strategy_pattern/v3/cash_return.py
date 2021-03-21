import cash_super


# 返利收费子类
# 返利收费，初始化时必须要输入返利条件和返利值，比如满300返100，则 money_condition = 300, money_return =  100
class CashReturn(cash_super.CashSuper):
    def __init__(self, money_condition, money_return):
        self._money_condition = money_condition
        self._money_return = money_return

    def accept_cash(self, money: float) -> float:
        result = money

        # 如果大于返利条件，则需要减去返利值
        if money >= self._money_condition:
            result = money - float(money) / float(self._money_condition) * self._money_return

        return result
