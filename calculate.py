# -*- coding: utf-8 -*-
import os
import math


class Vector(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y
        pass

    pass




class Engine():
    def __init__(self):
        self.number=0
        pass

    def bySquare(self,square,sizeOfOne):
        self.number=int(square/25.0/sizeOfOne)
        res=int(round((square/25.0/sizeOfOne)+0.45,0))
        if(res==0):
            res=1
        return res
        pass

    def byDistance(self,category,square):
        distance=[20,30,40,70]
        d=distance[category]
        d=d*2
        minimal=0
        maximum=0
        S=d*d/2
        side=math.sqrt(S)
        a=-1
        b=-1

        #Maximum

        a=1
        b=square
        maximum=int(round((b/side)+0.45))

        #Minimum

        a=math.sqrt(square)
        b=math.sqrt(square)
        minimal=int(round((a/side)+0.45)*round((b/side)+0.45))
        result=Vector(minimal,maximum)
        #self.number= int(round(square/(3.14*pow(distance[category],2))+0.45,0))
        return result
        pass
    pass
