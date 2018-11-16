# -*- coding:utf-8 -*-
#需求让web服务器去运行python脚本
#localhost:7788/ctime.py
from multiprocessing import Process

import re,sys

from socket import *


#设置静态文件根目录
HTML_ROOT_DIR = "./HTML"
WSGI_PYTHON_DIR = "./wsgipython"
class HTTPServer(object):
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


    def start(self):
        self.server_socket.listen(15)
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print("[%s,%s]:用户连接上了..." % client_addr)
            handel_client_process = Process(target=self.handel_client, args=(client_socket,))
            handel_client_process.start()
            client_socket.close()
    def start_response(self,status,headers):
        """
                status = "200 OK"
           headers = [
               ("Content-Type", "text/plain")
           ]
               """
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s:%s\r\n" % header
        '''
        print(response_headers)
        HTTP / 1.1 200 OK
        Content - Type: text / plain
        '''
        self.response_headers = response_headers
    def handel_client(self,client_socket):
        request_data = client_socket.recv(1024)
        if len(request_data) > 0:
            print("request_data:", request_data)
            # Python splitlines() 按照行('\r', '\r\n', \n')分隔
            request_lines = request_data.splitlines()
            for line in request_lines:
                print(line)

            # 解析请求报文
            # 'GET / HTTP/1.1'
            request_start_line = request_lines[0]
            print("request_start_line",request_start_line)
            # 提取用户请求的文件名
            file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
            method = re.match(r"(\w+) +/[^ ]* ", request_start_line.decode("utf-8")).group(1)
            if file_name.endswith(".py"):
                try:
                    m = __import__(file_name[1:-3])
                except Exception:
                    error_file = open(HTML_ROOT_DIR + "/copy_404error.html", "rb")
                    error_file_data = error_file.read()
                    error_file.close()
                    self.response_headers = "HTTP/1.1 404 Not Found\r\n"
                    response_body = error_file_data.decode("utf-8")
                else:

                    evn = {
                        "PATH_INFO":file_name,
                        "METHOD":method
                    }
                    response_body = m.application(evn,self.start_response)
                response_data = self.response_headers + "\r\n" + response_body
            else:

                if "/" == file_name:
                    file_name = "/index.html"
                try:
                    file = open(HTML_ROOT_DIR + file_name, "rb")
                except IOError:
                    error_file = open(HTML_ROOT_DIR + "/copy_404error.html", "rb")
                    error_file_data = error_file.read()
                    error_file.close()
                    response_start_line = "HTTP/1.1 404 Not Found\r\n"
                    response_header_line = "Server: My Server\r\n"
                    response_body = error_file_data.decode("utf-8")
                else:
                    file_data = file.read()
                    file.close()
                    # 构造响应数据
                    response_start_line = "HTTP/1.1 200 OK\r\n"
                    response_header_line = "Server: My Server\r\n"
                    response_body = file_data.decode("utf-8")
                response_data = response_start_line + response_header_line + "\r\n" + response_body
                print("response_data:", response_data)
            # 向客户端返回响应数据
            client_socket.send(bytes(response_data, "utf-8"))
            # 关闭客户端连接
            client_socket.close()

    def bind(self,address):
        self.server_socket.bind(address)

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    http_server.bind(("",7788))
    http_server.start()


if __name__ == "__main__":
    main()