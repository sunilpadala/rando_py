import math
import sys

class calc():

    def __init__(self):
        pass

    def add(self,*args):
        s=0
        for num in args:
            if type(num) == int or type(num) == float:
                s += num
            else:
                print('Invalid argument %s'%num)
                sys.exit(2)
        return s

    # def sub(self,*args):
    #     s=0
    #     for num in args:
    #         if type(num) == int or type(num) == float:
    #             s += num
    #         else:
    #             print('Invalid argument %s',%num)
    #             sys.exit(2)
    #     return s
