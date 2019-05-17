from tornado.websocket import WebSocketHandler
import tornado, os
import time, paramiko, threading


class Chat(WebSocketHandler):
    def open(self):
        pass

    def ssh(self):
        print('1231')
        hostname = '192.168.99.104'
        port = 22
        username = 'tarena'
        password = 'tarena'
        self.sshclient = paramiko.SSHClient()
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshclient.connect(hostname, port, username, password)

        # chan=sshclient.invoke_shell(term='xterm')
        self.chan = self.sshclient.invoke_shell()
        self.chan.timeout = 10
        self.chan.recv(1024).decode().strip()
        self.chan.recv(1024).decode().strip()

    def recvSH(self):
        while True:
            try:
                data = self.chan.recv(1024).decode().strip()
                print(data)
            except Exception as e:
                print(e)
                break
            if data.endswith("#"):
                self.write_message({"code": 0, "msg": data}, binary=False)
                self.chan.close()
                self.sshclient.close()
                break
            self.write_message({"code": 1, "msg": data}, binary=False)

    def on_message(self, message):
        if message == 'run':
            self.ssh()
            cmd = "python3 {}\r".format(os.path.join(self.settings['ROOT_PATH'], 'static', 'test.py'))
            self.chan.send(cmd)
            self.recvSH()
        else:
            self.chan.send(message + "\r")
            self.recvSH()
            pass

    def on_close(self):
        print('关闭')

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求
