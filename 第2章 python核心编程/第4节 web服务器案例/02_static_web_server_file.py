# -*- coding:utf-8 -*-
#1.tcp socket 服务端
from multiprocessing import Process

import re

from socket import *


#设置静态文件根目录
HTML_ROOT_DIR = "./HTML"
def handel_client(client_socket):
    """处理客户端请求"""
    #获取客户端请求数据
    request_data = client_socket.recv(1024)
    if len(request_data)>0:
        print("request_data:",request_data)
        #Python splitlines() 按照行('\r', '\r\n', \n')分隔
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)

        # 解析请求报文
        # 'GET / HTTP/1.1'
        request_start_line = request_lines[0]
        # 提取用户请求的文件名
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        if "/" == file_name:#写了这句话当访问http://localhost:7788/不加index.html也不会出现异常了
            file_name = "\index.html"
        try:
            file = open(HTML_ROOT_DIR+file_name,"rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_header_line = "Server: My Server\r\n"
            response_body = "您访问的内容没有找到()..."
            print("1111111111111111")
            print(response_body.encode("utf-8"))
        else:
            file_data = file.read()
            file.close()
            #构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_header_line = "Server: My Server\r\n"
            response_body = file_data.decode("utf-8")
        response_data = response_start_line + response_header_line + "\r\n" +response_body
        print("response_data:",response_data)
        #向客户端返回响应数据
        client_socket.send(bytes(response_data,"utf-8"))
        #关闭客户端连接
        client_socket.close()

def main():
    server_socket = socket(AF_INET,SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("",7788))
    server_socket.listen(15)
    while True:
        client_socket,client_addr = server_socket.accept()
        print("[%s,%s]:用户连接上了..."%client_addr)
        handel_client_process = Process(target=handel_client,args=(client_socket,))
        handel_client_process.start()
        client_socket.close()

if __name__ == "__main__":#当01_static_web_server.py已执行的方式去使用的话__name__的值是__main__如果是以导入包的形式导入的话返回的值就不是__main__
    main()