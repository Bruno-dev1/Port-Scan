import socket
import sys

host = "google.com"
ports = range(100)

def scan(host,ports):
    for port in ports:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.settimeout(0.5)
        code = client.connect_ex((host,int(port)))
        if code == 0 :
            print("[+] {} open".format(port))
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3 :
            ports = sys.argv[2].split(",")
        scan(host,ports)
    
    else:
        scan(host,ports)