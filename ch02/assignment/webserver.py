import sys
import _thread  
from socket import *
from time import *  

not_found_html = "<h1>404 NOT FOUND</h1>"  

def request_parser(request):
    lines = request.split('\n')
    request_line = lines[0].split()  
    header_lines = dict()
    for each in lines[1:]:
        if each.strip() != "":
            key = each[:each.find(':')]
            value = each[each.find(':')+1:].strip()
            header_lines[key] = value 
    return [request_line, header_lines]  

def generate_response(request_header):
    method, url, http_version = request_header[0]
    url = './static{}'.format(url)
    status = 200
    phase = {
        200: "OK",
        404: "NOT FOUND"
    }
    data = ''
    try:
        with open(url, 'rt') as fr:
            data = fr.read()
    except IOError:
        status = 404
        data = not_found_html
    return """HTTP/1.1 {} {}\r\nConnection: close\r\nContent-type: {}\r\n\r\n{}""".format(\
        status, phase[status], 'text/html', data)

def process_connection(conn_sock, addr):
    request = conn_sock.recv(1024).decode()
    request_header = request_parser(request)  
    response = generate_response(request_header)  
    conn_sock.send(response.encode('utf-8'))
    print('{} process has completed. \nClosing...'.format(addr))
    conn_sock.close()

if __name__ == '__main__':
    server_port = int(sys.argv[1])  
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1000) 
    while True:
        conn_sock, addr = server_socket.accept()
        _thread.start_new_thread(process_connection, (conn_sock, addr))
    
