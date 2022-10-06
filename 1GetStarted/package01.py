class A:
    def __init__(self,a=2):
        self.a=a
        print('你好，我是模块A __main__……')
        print(__name__)
if __name__=='__main__':
    AClass=A(30)
    print(AClass.a)


