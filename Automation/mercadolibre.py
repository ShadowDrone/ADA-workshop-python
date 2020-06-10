from helium import *
import xml.etree.ElementTree
import datetime
import subprocess
import os
import logging
import sys
import importlib.util
import traceback
import time
from selenium.common.exceptions import TimeoutException
import csv
import xlrd
import urllib.request

ahora = datetime.datetime.now()
Fecha = ahora.strftime('%Y-%m-%d_%H%M')
		

start_chrome()

print ("Comienzo Ejecucion Robot que descarga info de productos de ML")

		#va a la pagina
go_to("mercadolibre.com.ar")




time.sleep(3) 
		
producto = "Computadora" #input('Ingrese el producto a buscar:')
print ('Buscando productos')
#click(S("#idEelement"))
buscador =S(".nav-search-input")
write(producto, into=buscador)
time.sleep(2)
click(S(".nav-icon-search"))
#press(ENTER)
print('Bus Productos')


wait_until(S("#searchResults").exists,10)

productosFile= "productos\ML_" + Fecha  + ".txt"

sProductos=u"" #inicializo archivo	


mlProductos = find_all(S(".results-item"))
losPrimeros10 = mlProductos[0:10]
for mlProducto in losPrimeros10:
    
    highlight(mlProducto)
    we =  mlProducto.web_element.find_element_by_xpath(".//span[@class='main-title']")
    nombreProducto = we.text
    print("Descargando Producto  " + nombreProducto)
    we =  mlProducto.web_element.find_element_by_xpath(".//span[@class='price__fraction']")
    importeProducto = we.text
    
    we =  mlProducto.web_element.find_element_by_xpath(".//a[@class='item__info-title']")
    linkProducto = we.get_attribute("href")
    
    
    sProductos += nombreProducto + "\t" + importeProducto + "\t" + linkProducto + "\n"
    time.sleep(2) 
    scroll_down(250)



print('Generando archivo de datos ' + productosFile)
f = open(productosFile, 'w')
f.write(sProductos)
f.close()
						
kill_browser()
