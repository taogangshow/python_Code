from multiprocessing import *

import socket

import  re

HTML_ROOT_DIR = "./HTML"

def handel_client(client_socket):
    request_data = client_socket.recv(1024)
    if len(request_data)>0:
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)
        request_start_line = request_lines[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        try:
            file = open(HTML_ROOT_DIR+file_name,"rb")
        except IOError:
            error_file = open(HTML_ROOT_DIR + "/404error.html","rb")
            error_file_data = error_file.read()
            error_file.close()
            response_start_line = "HTTP/:1.1 404 Not Found\r\n"
            response_hander_line = "Server: My Fiest Server\r\n"
            response_body = error_file_data.decode("utf-8")
        else:

            file_data = file.read()
            file.close()
            response_start_line = "HTTP/:1.1 200 OK\r\n"
            response_hander_line = "Server: My Fiest Server\r\n"
            response_body = file_data.decode("utf-8")
        response_data = response_start_line + response_hander_line + "\r\n" + response_body
        client_socket.send(bytes(response_data,"utf-8"))
        client_socket.close()
def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(("",7788))
    server_socket.listen(128)
    while True:
        client_socket,client_addr = server_socket.accept()
        handel_client_process = Process(target=handel_client,args=(client_socket,))
        handel_client_process.start()
        client_socket.close()

if __name__ == "__main__":
    main()
