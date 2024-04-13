import socket

client=socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("0C-DD-24-18-BE-9B",4))


try:
    while True:
        message=input("Enter message: ")
        client.send(message.encode("utf-8"))
        data=client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
except OSError as e:
    pass

client.close()
