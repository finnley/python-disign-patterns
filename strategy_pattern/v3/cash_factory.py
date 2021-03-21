import cash_normal, cash_rebate, cash_return


# 现金收费工厂类
class CashFactory:
    @staticmethod
    def create_cash_factory(type):
        if type == "正常收费":
            return cash_normal.CashNormal()
        elif type == "满 300 返 100":
            return cash_return.CashReturn(300, 100)
        elif type == "打 8 折":
            return cash_rebate.CashRebate(0.8)
