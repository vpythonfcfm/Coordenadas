from vpython import *
from math import *


def es_numero(valor):
    """ Indica si un valor es numérico o no. """
    return isinstance(valor, (int, float, long, complex) )

class Punto(object):

	def __init__(self, x=0, y=0, z=0):
	""" Constructor de Punto, x e y deben ser numéricos,
	    de no ser así, se levanta una excepción TypeError """
		if es_numero(x) and es_numero(y) and es_numero(z):
		    self.x=x
		    self.y=y
		    self.z=z
		else:
		    raise TypeError("x e y deben ser valores numéricos")

	""" Devuelve la norma del vector que va desde el origen
	    hasta el punto. """
	def norma(self):
	return (self.x*self.x + self.y*self.y + self.z*self.z)**0.5

	def __str__(self):
    """ Muestra el punto como un par ordenado. """
    return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __add__(self, otro):
    	return Punto(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self,otro):
    	return Punto(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def distancia(self, otro):
	""" Devuelve la distancia entre ambos puntos. """
		r = Punto(self.x - otro.x, self.y - otro.y, self.z - otro.z)
		return r.norma()


class Cilindricas:
	def __init__(self, radio = 0, azimutal = 0, altura = 0):
		if es_numero(radio) and es_numero(azimutal) and es_numero(altura):
		    self.radio=radio
		    self.azimutal=azimutal
		    self.altura=altura
		else:
		    raise TypeError("no son numeros")

	def Pasar_A_Cilindricas_A_Cartesianas(self):
		radio = self.radio
		azimutal = self.azimutal
		altura = self.altura
		punto = Punto()
		punto.x = radio*cos(azimutal)
		punto.y = radio*sin(azimutal)
		punto.z = altura
		return punto
