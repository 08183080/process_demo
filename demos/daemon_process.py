import multiprocessing

'''
[warning] daemonic processes are not allowed to have children
what is dameonic process? processes run in the background and in the darkness
'''

class P1:
    def __init__(self):
        self.start()
    
    def hello(self):
        print('hello')
        p3 = multiprocessing.Process(target=self.hi)

        p3.start()
        p3.join()
    
    def hi(self):
        print('hi')

    def start(self):
        p1 = multiprocessing.Process(target=self.hello)
        p2 = multiprocessing.Process(target=self.hi)

        p1.start()
        p1.join()

        p2.start()
        p2.join()

if __name__ == "__main__":
    p11 = P1()
