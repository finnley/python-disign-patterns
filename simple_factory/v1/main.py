class Program:
    '''
       1. A, B, C, D 命名不规范
       2. 判断分支每个条件都需要判断，意味着做了三次无用功
       3. 如果 C 的值为 0，结果会报错
   '''
    def main(self):
        A = input("请输入数字A: ")
        print("A: ", A)

        B = input("请选择运算符号(+、-、*、/): ")
        print("B: ", B)

        C = input("请输入数字B:")
        print("C: ", C)

        print("Expression: D = A %s C = %s %s %s" % (B, A, B, C))

        D = ""
        if B == "+":
            D = str(float(A) + float(C))
        if B == "-":
            D = str(float(A) - float(C))
        if C == "*":
            D = str(float(A) * float(C))
        if C == "/":
            D = str(float(A) / float(C))

        print("结果是: %s" % D)


if __name__ == "__main__":
    run = Program()
    run.main()

'''
Result-1:

请输入数字A: 10
A:  10
请选择运算符号(+、-、*、/): + 
B:  +
请输入数字B: 23
C:  23
Expression: D = A + C = 10 + 23
结果: 33.0

Result-2:
请输入数字A: 10
A:  10
请选择运算符号(+、-、*、、): /
B:  /
请输入数字B: 0
C:  0
Expression: D = A / C = 10 / 0
Traceback (most recent call last):
  File "/Users/finnley/Code/design-patterns/simple_factory/python2/v1/main.py", line 33, in <module>
    run.main()
  File "/Users/finnley/Code/design-patterns/simple_factory/python2/v1/main.py", line 27, in main
    D = str(float(A) / float(C))
ZeroDivisionError: float division by zero
'''
