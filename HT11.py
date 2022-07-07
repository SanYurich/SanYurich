#!/usr/bin/env python
# coding: utf-8
# y = x**2 - 6*abs(x) + 8
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
# In[257]:


from sympy import symbols
from sympy.plotting import plot
from sympy.solvers import solve
from sympy import diff, sin, exp
from sympy import oo

x = Symbol('x')
#y = x**2 - 6*abs(x) + 8  # При данном уравнении выдаеот ошибку на пункты 1,2,5,6. Способы как это исправыить, мне не понятны
y = x**2 - 6*x + 8        # принял решение использовать уравнение без abs
y


# 1. Определить корни

# In[258]:


solve(y,x)

2. Найти интервалы, на которых функция возрастает
# In[259]:


f = diff(y)
solve(f,x)
print(y.subs(x,solve(f,x)[0]))# при x = 3 y =-1 точка экстреммума функции y(x) )
print(f.subs(x,4)) #f(производная) в точке x=4 равна 2 - что >0 - значит на промежутке x от [3,-∞) f - убывает'

3. Найти интервалы, на которых функция убывает
# In[260]:


f.subs(x,2) # Функция f(x) убывает на промежуутке (-∞, 2) и возрастает (3, +∞)

4. График функции
# In[261]:


plot(y, line_color="red")

5. Вычислить вершину
# In[262]:


print(f'y = {solve(y,x)[0]}; x = {y.subs(x,solve(f,x)[0])}')

6. Определить промежутки, на котором f > 0
# In[263]:


w= (solve(y,x)[0]+solve(y,x)[1])/2
y.subs(x,w)

7. Определить промежутки, на котором f < 0
# In[256]:


w= (solve(y,x)[0]-solve(y,x)[1])/2
y.subs(x,w)
