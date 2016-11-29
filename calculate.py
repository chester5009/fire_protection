# -*- coding: utf-8 -*-
import os
import math
class Engine():
    def __init__(self):
        self.number=0;
        pass

    def bySquare(self,square,sizeOfOne):
        self.number=int(square/25.0/sizeOfOne)
        return int(round((square/25.0/sizeOfOne)+0.45,0))
        pass

    def byDistance(self,category,square):
        distance=[20,30,40,70]
        d=distance[category]
        minimal=0
        maximum=0
        S=d*d/2
        side=math.sqrt(S)
        self.number= int(round(square/(3.14*pow(distance[category],2))+0.45,0))
        return self.number
        pass
    pass
