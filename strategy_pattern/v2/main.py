# 在 v1 的基础上增加打折
class Program:
    discountMessage = {
        "a": '正常收费',
        "b": "打八折",
        "c": "打七折",
        "d": "打五折"
    }

    # 相当于一个下拉框，可供用户选择
    discount = {
        "a": 1,
        "b": 0.8,
        "c": 0.7,
        "d": 0.5
    }

    # 折扣
    def getDiscountMessage(self, index="a"):
        return self.discountMessage.get(index)

    def main(self):
        print("please input 'a'", self.getDiscountMessage("a"))
        print("please input 'b'", self.getDiscountMessage("b"))
        print("please input 'c'", self.getDiscountMessage("c"))
        print("please input 'd'", self.getDiscountMessage("d"))

        index = input("请选择对应折扣: ")
        print("您选择的是: ", index)

        total_prices = 0
        total = 0

        price = input("请输入商品单价: ")
        print("price: ", price)

        num = input("请输入商品数量: ")
        print("num: ", num)

        if index == "a":
            total_prices = float(price) * int(num)
        elif index == "b":
            total_prices = float(price) * int(num) * 0.8
        elif index == "c":
            total_prices = float(price) * int(num) * 0.7
        elif index == "d":
            total_prices = float(price) * int(num) * 0.5

        total = total + total_prices

        print("单价：" + price + " 数量：" + num + " 折扣: " + self.getDiscountMessage(index) + " 合计：" + str(total))


if __name__ == "__main__":
    run = Program()
    run.main()

'''
结果：
please input 'a' 正常收费
please input 'b' 打八折
please input 'c' 打七折
please input 'd' 打五折
请选择对应折扣: a
您选择的是:  a
请输入商品单价: 10
price:  10
请输入商品数量: 3
num:  3
单价：10 数量：3 折扣: 正常收费 合计：30.0

总结：
该方法重复代码太多，比如 float(price)；
而且4个分支要执行的语句除了打折多少以外几乎没有什么不同，可以考虑重构；
如果添加需求，商场活动加大，需要有满300返100的促销算法，怎么办？
'''
