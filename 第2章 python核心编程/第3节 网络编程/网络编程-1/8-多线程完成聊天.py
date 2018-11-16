from socket import *
from threading import Thread


def recvData(udpSocket):
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        content,destInfo = recvInfo
        print(">>%s:%s"%(destInfo[0],content.decode("gb2312")))

def sendData(udpSocket,destIp,destPort):
    while True:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode("gb2312"),(destIp,destPort))



def main():
    destIp = input("对方的IP:")
    destPort = int(input("对方的Port:"))

    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",4567))

    tr = Thread(target = recvData,args = (udpSocket,))
    ts = Thread(target = sendData,args = (udpSocket,destIp,destPort))
    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == "__main__":
    main()
