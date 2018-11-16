class ShortInputException(Exception):
    def __init__(self,length,atleast):
        print("1")
        self.length = length
        self.atleast = atleast
def main():
    print("2")
    try:
        s = input("Please input:")
        if len(s)<3:
            raise ShortInputException(len(s),3) #创建一个对象，把len(s),3分别传入__init__方法的length,atleast
    except ShortInputException as result: #变量result指向了抛出异常raise ShortInputException(len(s),3)这个对象的引用
        print("ShortInputException:您输入的长度为 %d,长度至少应该是 %d"%(result.length,result.atleast))
    else:
        print("没有异常")
main()