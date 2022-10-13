#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Investiga sobre funciones matemáticas multivariables (dos variables) conocidas que describan situaciones comunes de la vida real. Considera un punto inicial  y encuentra el valor mínimo estimado para la que dicha función converge
import numpy as np
import numpy.linalg as npl
import sympy
from sympy import *
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


# In[16]:


def obtenerGradiente(funcion_entrada):
    f1x = funcion.diff(x)
    f1xLam = lambdify('x,y',f1x)
    f1y = funcion.diff(y)
    f1yLam = lambdify('x,y',f1y)
    f1 = [f1x,f1y]
    gradiente = lambdify('x,y',f1)
    return gradiente


# In[17]:


def gradienteDescendente(gradiente,punto_inicio,tamano_paso=0.090,precision=0.02, max_iter=2000,initError=10):
  x,y=punto_inicio.astype(float)
  currIter,iterCoords=0,[np.hstack([x,y])]
  error=initError
  currX=np.array([x,y])


  while npl.norm(error)>precision and currIter<max_iter:
    currIter+=1
    prevX=currX.copy()

    # Ecuacion de la gradiente
    currX -= tamano_paso*np.array(gradiente(x,y))
    x,y=currX[0].copy(), currX[1].copy()

    error=currX-prevX
    iterCoords.append(np.hstack([x,y]))
  return currIter,currX,np.vstack(iterCoords)


# In[18]:


def imprimirResultados(pasos_totales, coordenada_final):
  print('Los pasos totales fueron:')
  print(pasos_totales)
  print('El valor minimo es:')
  print(coordenada_final)


# In[20]:


# Main
x,y = symbols('x y')
# considerando un punto de inicio [-4, 2]
# k=5
punto_inicio = np.vstack([-4, 2])
funcion = x**2+y**2+5


gradiente = obtenerGradiente(funcion)
pasos_totales, coordenada_final, coordenadas_intermedias = gradienteDescendente(gradiente,punto_inicio)
inmprimirResultados(pasos_totales, coordenada_final)

