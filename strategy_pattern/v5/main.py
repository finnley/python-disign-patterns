from cash_normal import CashNormal
from cash_rebate import CashRebate
from cash_return import CashReturn
from cash_context import CashContext


class Program(object):
    discountMessage = {
        'a': '正常收费',
        'b': '满 300 返 100',
        'c': '打 8 折',
    }

    # 折扣
    def get_discount_message(self, index='a'):
        return self.discountMessage.get(index)

    # normal
    def type_normal(self):
        return CashContext(CashNormal())

    # return
    def type_return(self):
        return CashContext(CashReturn(300, 100))

    # rebate
    def type_rebate(self):
        return CashContext(CashRebate(0.8))

    def main(self):
        print("please input 'a', 正常收费")
        print("please input 'b', 满 300 返 100")
        print("please input 'c', 打 8 折")

        index = input("请选择折扣: ")
        print("您选择的是: ", index)

        price = input("请输入商品单价: ")
        print("price: ", price)

        num = input("请输入商品数量: ")
        print("num: ", num)

        total = 0

        cc = self.switch(index)
        total_prices = cc.get_result(float(price) * int(num))
        total = total + total_prices

        print("单价：" + price + " 数量：" + num + " 折扣: " + self.get_discount_message(index) + " 合计：" + str(total))

    def switch(self, operate):
        switcher = {
            'a': self.type_normal,
            'b': self.type_return,
            'c': self.type_rebate
        }
        method = switcher.get(operate, 'wrong operate')
        if method:
            return method()


if __name__ == "__main__":
    run = Program()
    run.main()

'''
please input 'a', 正常收费
please input 'b', 满 300 返 100
please input 'c', 打 8 折
请选择折扣: a
您选择的是:  a
请输入商品单价: 200
price:  200
请输入商品数量: 2
num:  2
单价：200 数量：2 折扣: 正常收费 合计：400.0

please input 'a', 正常收费
please input 'b', 满 300 返 100
please input 'c', 打 8 折
请选择折扣: b
您选择的是:  b
请输入商品单价: 400
price:  400
请输入商品数量: 1
num:  1
单价：400 数量：1 折扣: 满 300 返 100 合计：0.0

please input 'a', 正常收费
please input 'b', 满 300 返 100
please input 'c', 打 8 折
请选择折扣: c
您选择的是:  c
请输入商品单价: 100
price:  100
请输入商品数量: 1
num:  1
单价：100 数量：1 折扣: 打 8 折 合计：80.0
'''