import socket
import naoqi

def make_proxy(proxy_type):
    try:
        proxy = naoqi.ALProxy(proxy_type, "127.0.0.1", 9559)
        return proxy

    except Exception, e:
        print("Error creating ", proxy_type, " proxy:", str(e))
        exit(1)

mem = make_proxy("ALMemory")

addr = socket.gethostbyname("raspberrypi")
mem.insertData("raspi_ip", addr)
