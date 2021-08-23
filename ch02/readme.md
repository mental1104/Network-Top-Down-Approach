# Chapter 2 Application Layer  

## Code  

### UDP

[UDPClient.py](./code/UDPClient.py)  
[UDPServer.py](./code/UDPServer.py)  

![](./code/pic/UDP_1.png)  

This time we close down the server, and there's no response to the following requests of the client:  

![](./code/pic/UDP_2.png)  

### TCP  

[TCPClient.py](./code/TCPClient.py)  
[TCPServer.py](./code/TCPServer.py)  

![](./code/pic/TCP_1.png)  

If we shut down the server, the client will panic:  

![](./code/pic/TCP_2.png)