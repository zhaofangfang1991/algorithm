
import pygame
class Single(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance


s1 = Single()
print(s1)
s2 = Single()
print(s2)