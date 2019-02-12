# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-11 23:23
__author__ = 'f1renze'
__time__ = '2019-02-11 23:23'


from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass

    def __contains__(self, item):
        for i in range(len(self)):
            if self[i] == item:
                return True
        return False

    def index(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError('val not in sequence')

    def count(self, val):
        j = 0
        for i in range(len(self)):
            if self[i] == val:
                j += 1
        return j

    
if __name__ == '__main__':
    pass
