#-------------------------------------------------------------------------------
# Name:        feasible_region.py
# Purpose:     draw feasible_region
#
# Author:      Kyle Katarn
#
# Created:     01/20/2019
# Copyright:   (c)  Kyle Katarn 2019
#-------------------------------------------------------------------------------

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
x,y=sym.symbols("x y")
class model:
    print("おまじない   :import sympy as sym")
    print("             x,y=sym.symbols(x y)")
    print(".model      :feasoble_resion.model()")
    print(".linspace   :x始まり座標、x終わり座標、左二つの分割")
    print(".spacelimit :x始まり座標、x終わり座標、y始まり座標、y終わり座標")
    print(".addConstr  :例 -1*x+2*y-88 など、x-4,y-6などの式も可")
    print("             変数はx、yのみ")
    print("             等号は判定できないのですべて左辺へ移行すること")
    print(".show       :plt.show()と同じ")

    plt.figure(figsize=(6, 6))
    def __init__(self):
        self.objvar = y
        self.objvar2= x
        self.space = np.array([])
        self.ys=0
        self.ye=0
        
    def linspace(self,start,end,split):
        self.space = np.linspace(start, end, split)
        
    def spacelimit(self,xstart,xend,ystart,yend):
        plt.xlim([xstart,xend])
        plt.ylim([ystart,yend])
        self.ys=ystart
        self.ye=yend
    
    def addConstr(self,function):
        try:
            func = str( sym.solve(function, self.objvar)[0] )
        except:
            func = str( sym.solve(function, self.objvar2)[0] )
        
        x=self.space
        var=list(sym.sympify(function).atoms(sym.Symbol))
        if len(var)==1:
            if var[0]==y:
                plt.plot(int(func) + x*0)
            else :
                plt.plot([int(func),int(func)],[self.ys,self.ye])
        else:
            plt.plot(eval( func ))
    
    def show(self):
        plt.show()