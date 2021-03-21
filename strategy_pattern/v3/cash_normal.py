import cash_super


# 正常收费子类
class CashNormal(cash_super.CashSuper):
    '''
    正常收费吗，原价返回
    '''

    def accept_cash(self, money: float) -> float:
        return money
