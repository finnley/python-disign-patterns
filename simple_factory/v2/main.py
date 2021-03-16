class Program:
    # add
    def add(self, numberA, numberB):
        return str(float(numberA) + float(numberB))

    # subtract
    def subtract(self, numberA, numberB):
        return str(float(numberA) - float(numberB))

    # multiply
    def multiply(self, numberA, numberB):
        return str(float(numberA) * float(numberB))

    # divide
    def divide(self, numberA, numberB):
        if numberB != '0':
            return str(float(numberA) / float(numberB))
        else:
            return "除数不能为0"

    def switch(self, operate, numberA, numberB):
        switcher = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
        method = switcher.get(operate, "wrong operate")
        return method(numberA, numberB)

    def main(self):
        try:
            strNumberA = input("请输入数字A: ")
            print("strNumberA: ", strNumberA)

            strOperate = input("请选择运算符号(+、-、*、/): ")
            print("strOperate: ", strOperate)

            strNumberB = input("请输入数字B: ")
            print("strNumberB: ", strNumberB)

            print("Expression: strResult = strNumberA %s strNumberB = %s %s %s" % (
                strOperate, strNumberA, strOperate, strNumberB))
            strResult = self.switch(operate=strOperate, numberA=strNumberA, numberB=strNumberB)
            print("结果是: %s" % strResult)
        except BaseException as e:
            print("结果有误: ", e)


if __name__ == "__main__":
    run = Program()
    run.main()

'''
result-1:
请输入数字A: 10
strNumberA:  10
请选择运算符号(+、-、*、、): *
strOperate:  *
请输入数字B: 3
strNumberB 3
Expression: strResult = A * B = 10 * 3
结果: 30.0

result-2:
请输入数字A: 10
strNumberA:  10
请选择运算符号(+、-、*、、): /
strOperate:  /
请输入数字B: 0
strNumberB 0
Expression: strResult = A / B = 10 / 0
结果: 除数不能为0

总结：
该程序只能满足当前需求，程序不容易维护，不容易扩展，更不容易复用，从而达不到高质量代码要求
'''