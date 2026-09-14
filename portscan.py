import socket
import sys

host = "127.0.0.1"#sys.argv[1]
ports = range(100)

def scan(host,port):
    for port in ports:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.settimeout(0.5)
        code = client.connect_ex((host,port))
        if code == 0 :
            print("[+] {} open".format(port))

