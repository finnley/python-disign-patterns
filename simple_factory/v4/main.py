from operation_factory import OperationFactory

class Program:
    def main(self):
        op = OperationFactory.createOperate("-")
        op.SetNumberA(10)
        op.SetNumberB(2)
        strResult = op.GetResult()
        print("结果是: %s" % strResult)


if __name__ == "__main__":
    run = Program()
    run.main()
