from socket import *

def main():
    udpSocket = socket(AF_INET,SOCK_DGRAM)

    udpSocket.bind(("",7788))
    while True:
        recvData = udpSocket.recvfrom(1024)
        content,destInfo = recvData
        print("[%s]:%s"%(str(destInfo[0]),content.decode("gb2312")))

    udpSocket.close()

if __name__ == "__main__":
    main()
