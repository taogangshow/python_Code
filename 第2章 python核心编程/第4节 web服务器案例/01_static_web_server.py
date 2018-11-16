# -*- coding:utf-8 -*-
#1.tcp socket 服务端
from multiprocessing import Process

from socket import *

def handel_client(client_socket):
    """处理客户端请求"""
    HTML_ROOT_DIR = "./HTML"
    while True:
        #获取客户端请求数据
        request_data = client_socket.recv(1024)
        if len(request_data)>0:
            print("request_data:",request_data)
            #构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_header_line = "Server: My Server\r\n"
            response_body = "Hello World"
            response_data = response_start_line + response_header_line + "\r\n" +response_body
            print("response_data:",response_data)
            #向客户端返回响应数据
            client_socket.send(bytes(response_data,"utf-8"))
            #关闭客户端连接
            client_socket.close()

            try:
                file = open(HTML_ROOT_DIR+"/index.html")
                data = file.read()
                file.close()
            except IOError:
                client_socket.send("HTTP/1.1 404 NOT FOUND\r\n"
                                  "\r\n"
                                  "您访问的页面不存在~")
        else:
            break





def main():
    server_socket = socket(AF_INET,SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("", 7788))
    server_socket.listen(15)
    while True:
        client_socket,client_addr = server_socket.accept()
        print("[%s,%s]:用户连接上了..."%client_addr)
        handel_client_process = Process(target=handel_client,args=(client_socket,))
        handel_client_process.start()
        client_socket.close()

if __name__ == "__main__":#当01_static_web_server.py已执行的方式去使用的话__name__的值是__main__如果是以导入包的形式导入的话返回的值就不是__main__
    main()