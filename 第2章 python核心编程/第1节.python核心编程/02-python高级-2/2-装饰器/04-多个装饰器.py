#定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold    #test3 = makeBold(test3)
@makeItalic  #test3 = makeItalic(test3)
def test3():
    return "hello world-3"

ret = test3()
print(ret)
