#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

from datetime import datetime, date, time, timedelta
import calendar

class App(QtGui.QWidget):

	def __init__(self):
		super(App, self).__init__()

		self.initUI()

	def initUI(self): 

		#Agregamos los nombres de los personajes
		p1 = QtGui.QLabel("Miguel Hidalgo y Costilla (1753-1811)", self)
		p1.move(15,10)

		p2 = QtGui.QLabel("Ignacio Allende (1769-1811)", self)
		p2.move(15,40)

		p3 = QtGui.QLabel("Jose Maria Morelos (1765-1815)", self)
		p3.move(15,70)

		#Creamos el boton 
		boton = QtGui.QPushButton("Aprietame", self)
		boton.move(150,150)
		self.connect(boton, QtCore.SIGNAL("clicked()"), self.fecha)

		#Agregamos los atributos de la ventana principal
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Viva Mexico')
		self.setWindowIcon(QtGui.QIcon('bandera.jpg'))
		self.show()

	#Calcular los dias que faltan
	def fecha(self):
		hoy = date.today()
		prox = date(2017, 9, 15)
		faltan = prox - hoy
		print("Faltan", faltan.days, "dias")
	
def main():
	
	app = QtGui.QApplication(sys.argv)
	aa = App()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()