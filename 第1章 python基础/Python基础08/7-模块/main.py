import sendmsg
import recvmsg
sendmsg.test1()
sendmsg.test2()
recvmsg.test1()

#from sendmsg import test1,test2
#from sendmsg import test2
#尽量不要使用import * 当出现相同的方法时候,后者的recvmsg模块中的test1()方法会覆盖前者senmsg中的test1()方法
#from sendmsg import *
#from recvmsg import *
#test1()
#test2()

