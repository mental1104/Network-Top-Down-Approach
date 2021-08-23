from socket import *
from time import *

if __name__ == '__main__':
    port = 12000
    server_addr = 'localhost'  
    client_sock = socket(AF_INET, SOCK_DGRAM)  
    client_sock.settimeout(1)
    for i in range(1,11):
        begin_time = time()
        try:
            send_data = 's' * 64
            client_sock.sendto(send_data.encode(), (server_addr, port))
            message, address = client_sock.recvfrom(2048)
            rrt = '%.3f' % (1000 * (time() - begin_time))
            print('{} bytes from {}: udp_seq={} time={}ms'.format(len(message),address, i, rrt))
        except timeout:
            print('time out: udp_seq={}'.format(i))