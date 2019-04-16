import uuid
import socket
import netifaces
import ipaddress

ips=['0.0.0.0','255.255.255.255','169.254.1.200','239.18.1.5','224.0.0.18','8.8.8.8']
print(uuid.uuid4().hex)
print(socket.gethostname())
# print(netifaces.interfaces())
for face in netifaces.interfaces():
    x = netifaces.ifaddresses(face)
    ipv4s = x.get(2,[])
    for ipv4 in ipv4s:
        ips.append(ipv4['addr'])

print(ips)

for ip in ips:
    # print(ip)
    ip = ipaddress.ip_address(ip)
    # print(ip,type(ip))
    # print(1,ip.is_global)
    # print(2,ip.is_link_local) # 链路本地地址
    # print(3,ip.is_private)
    # print(4,ip.is_loopback)  # 换回地址
    # print(5,ip.is_multicast) # 组播地址
    # print(6,ip.is_reserved)  # 保留地址
    if ip.version != 4:
        continue
    if ip.is_multicast or ip.is_reserved or ip.is_link_local or ip.is_loopback or ip.is_unspecified:
        continue
    print(ip)
