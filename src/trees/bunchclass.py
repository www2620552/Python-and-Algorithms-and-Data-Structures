#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

class BunchClass(dict):
    def __init__(self, *args, **kwds):
        super(BunchClass, self).__init__(*args, **kwds)
        self.__dict__ = self


def main():
    ''' {'right': {'right': 'Xander', 'left': 'Willow'}, 'left': {'right': 'Angel', 'left': 'Buffy'}}'''
    bc = BunchClass     # notice the absence of ()
    tree = bc(left = bc(left="Buffy", right="Angel"), right = bc(left="Willow", right="Xander"))
    print(tree)

if __name__ == '__main__':
     main()




