from sympy import *
import numpy as np


a,b,c,t = symbols('a b c t',real=True,nonzero=True,positive=True)
#函数
y = symbols('y',real=True,nonzero=True,positive=True,cls=Function)


eq1 = Eq(y(t).diff(t),a*y(t)*(1-b*y(t)))
sol = dsolve(eq1)
#微分


y = trigsimp(sol.rhs)
print(y)
#化简


var('C1')  #和y相关
e1 = Eq(y.subs({t:0}),c)
#y(0)=c
l = solve([e1],[C1])
print(l)


y = y.subs(l)
print(y)
pprint(y)

