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

    def sub(self,*args):
        s,c=0,0
        for num in args:
            if type(num) == int or type(num) == float:
                if c > 0:
                    num *= -1
                s += num
                c +=1
            else:
                print('Invalid argument %s'%num)
                sys.exit(2)
        return s
