import datetime
import socket
import uuid
import os.path
import netifaces
import ipaddress
from .conf import MYID_PATH


class Message(object):
    # uuid用于标示主机，而不是标示实例

    def __init__(self, myidpath: str = MYID_PATH):
        # id应该从文件中读取，一个agent一个id，一旦生成不可改变，除非删除myid文件
        self.id = ''

        # 文件是否存在
        if os.path.exists(myidpath):
            with open(myidpath, encoding='UTF-8') as f:
                id = f.readline().strip()
                if len(id) == 32:
                    self.id = id
            self.id = id

        # 不存在新建
        if not self.id:
            with open(myidpath, 'w', encoding='UTF-8') as f:
                self.id = uuid.uuid4().hex
                f.write(self.id)

    # 获取主机IP地址
    def _get_addr(self):
        ips = []
        for iface in netifaces.interfaces():
            info = netifaces.ifaddresses(iface)
            ipv4s = info.get(2, [])
            for ipv4 in ipv4s:
                ip = ipv4['addr']
                ip = ipaddress.ip_address(ip)
                if ip.version != 4:
                    continue
                if ip.is_multicast or ip.is_reserved or ip.is_link_local or ip.is_loopback or ip.is_unspecified:
                    continue
                ips.append(str(ip))
        return ips

    # 注册消息
    def register(self):
        return {
            'id': self.id,
            'hostname': socket.gethostname(),
            'timestamp': datetime.datetime.now().timestamp(),
            'ips': self._get_addr()
        }

    # 心跳消息
    def heartbeat(self):
        return {
            'id': self.id,
            'timestamp': datetime.datetime.now().timestamp(),
        }

    def result(self, task_id, code, text):
        return {
            'id': self.id,
            'task_id': task_id,
            'code': code,
            'output': text
        }
