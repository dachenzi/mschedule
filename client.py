import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:9000")

print(c.hello('RPC'))