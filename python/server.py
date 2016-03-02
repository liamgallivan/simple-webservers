import sys, os
import socket

PORT = 8888

def serve_file(client_conn, fileName):
    request = client_conn.recv(1024)
    print(request.decode())
    file = open(fileName, 'rb')
    read = file.read(1024)
    while read:
        client_conn.send(read)
        read = file.read(1024)
    print('Sent file')

def listen_forever(fileName=''):
    if not os.path.exists(fileName):
        print('Specified file not found')
        sys.exit(2)

    listen_socket = socket.socket()
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(('', PORT))
    listen_socket.listen(5)
    print('listening at port: {0}...'.format(PORT))

    while True:
        client_conn, client_addr = listen_socket.accept()
        serve_file(client_conn, fileName)
        client_conn.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No File Specified')
        sys.exit(2)
    listen_forever(sys.argv[1])

