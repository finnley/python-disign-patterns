import cash_super


# 打折收费子类
class CashRebate(cash_super.CashSuper):
    def __init__(self, money_rebate):
        self._money_rebate = money_rebate

    # 打折手给，初始化时，必须输入折扣率，如八折，就是 0.8
    def accept_cash(self, money: float) -> float:
        return money * self._money_rebate
