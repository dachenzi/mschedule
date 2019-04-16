import zerorpc

class MyRPC(object):
    def hello(self,string):
        print('hello {}'.format(string))

if __name__ == '__main__':
    s = zerorpc.Server(MyRPC())
    s.bind("tcp://0.0.0.0:9000")
    s.run()