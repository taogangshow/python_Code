from socket import *
updSocket = socket(AF_INET,SOCK_DGRAM)
updSocket.bind(("",7789))
recvData = updSocket.recvfrom(1024)

content,destInfo = recvData

print("content is %s"%content)
print("content is %s"%content.decode("gb2312"))
info = []
for i in destInfo:
    info.append(i)
print("发送方IP:%s ,端口:%d"%(info[0],info[1]))
