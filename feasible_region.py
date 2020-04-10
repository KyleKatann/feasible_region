#-------------------------------------------------------------------------------
# Name:        feasible_region.py
# Purpose:     draw feasible_region
#
# Author:      Kyle Katarn
#
# Created:     04/26/2019
# Copyright:   (c)  Kyle Katarn 2019
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
x,y=sym.symbols("x y")

class model:
    print(".spacelimit :x始まり座標、x終わり座標、y始まり座標、y終わり座標、マスの細かさ(細かいほど正確)")
    print(".addConstr  :例 -1*x+2*y-88<0 など、変数はx、yのみ、math入り関数も可")
    print(".show       :plt.show()と同じ")
    
    def __init__(self):
        self.space = np.array([])
        self.xzone = np.array([])
        self.xzone = np.array([])
        self.xstart=0
        self.ystart=0
        self.xend=0
        self.yend=0
        
    def spacelimit(self,xstart,xend,ystart,yend,fineness_of_scale):
        xscale=int((xend-xstart)//fineness_of_scale)
        yscale=int((yend-ystart)//fineness_of_scale)
        self.space = np.ones((xscale,yscale))
        self.xzone = xstart+np.array([i*fineness_of_scale for i in range(xscale)])
        self.yzone = ystart+np.array([i*fineness_of_scale for i in range(yscale)])
        self.xstart= xstart
        self.ystart= ystart
        self.xend  = xend
        self.yend  = yend
        
    def addConstr(self,function):
        function=str(function)
        for i,x in enumerate(self.xzone):
            for j,y in enumerate(self.yzone):
                if not eval(function):
                    self.space[j][i]=0
        
    def show(self):
        self.space=self.space[::-1]
        plt.figure(figsize=(6, 6))
        plt.imshow(self.space,interpolation='nearest',vmin=0,vmax=1,cmap='gray',extent=[self.xstart,self.xend,self.ystart,self.yend])