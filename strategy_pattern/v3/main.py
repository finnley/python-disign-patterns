import cash_factory


# 在 v1 的基础上增加打折
class Program:
    discountMessage = {
        "a": '正常收费',
        "b": "满 300 返 100",
        "c": "打 8 折",
    }

    # 折扣
    def get_discount_message(self, index="a"):
        return self.discountMessage.get(index)

    def main(self):
        print("please input 'a'", self.get_discount_message("a"))
        print("please input 'b'", self.get_discount_message("b"))
        print("please input 'c'", self.get_discount_message("c"))

        index = input("请选择对应折扣: ")
        print("您选择的是: ", index)

        csuper = cash_factory.CashFactory.create_cash_factory(self.get_discount_message(index))

        total = 0

        price = input("请输入商品单价: ")
        print("price: ", price)

        num = input("请输入商品数量: ")
        print("num: ", num)

        total_prices = csuper.accept_cash(float(price) * int(num))
        total = total + total_prices

        print("单价：" + price + " 数量：" + num + " 折扣: " + self.get_discount_message(index) + " 合计：" + str(total))


if __name__ == "__main__":
    run = Program()
    run.main()

'''
结果：
please input 'a' 正常收费
please input 'b' 满 300 返 100
please input 'c' 打八折
请选择对应折扣: a
您选择的是:  a
请输入商品单价: 100
price:  100
请输入商品数量: 2
num:  2
单价：100 数量：2 折扣: 正常收费 合计：200.0

please input 'a' 正常收费
please input 'b' 满 300 返 100
please input 'c' 打 8 折
请选择对应折扣: c
您选择的是:  c
请输入商品单价: 100
price:  100
请输入商品数量: 1
num:  1
单价：100 数量：1 折扣: 打 8 折 合计：80.0

总结：
如果增加需求，需要打五折并且满500送200的促销活动？
如果再增加需求，满100积分10点，以后积分到一定时候可以领取奖品？

简单工厂虽然可以解决上面问题，但这个模式只是解决对象的创建问题，而且工厂本身包括了所有的收费方式，
商场时可能进场性的更改很糟糕的处理方式，所以它不是最好的办法，面对算法的市场变动，需要有更好的办法

比如策略模式(Strategy):
定义算法家族，分别封装起来，让它们之间可以相互替换，此模式让算法的变化，不会影响到使用算法的客户
'''
