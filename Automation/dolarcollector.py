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

print ('Comienzo Ejecucion Robot que descarga cotizaciones de BNA y de Banco Piano')

		#va a la pagina
go_to("www.bna.com.ar")


#oculto cosas de la pagina para mostrar mejor la demo

time.sleep(5) 
		
if S(".ADDUChome").exists():
	S(".ADDUChome").style = "display:none";	

print('Descargando Cotizaciones')

p = 1
fin = 10
			
cotizacionesFile= "D:\ADA\code\Python\Workshop\Automation\cotizaciones\BNA_" + Fecha  + ".txt"

sCotizaciones=u"" #inicializo archivo						
while p < fin:
    
    if S("//*[@id=\"billetes\"]/table/tbody/tr["+str(p)+"]/td[1]").exists():
        highlight(S("//*[@id=\"billetes\"]/table/tbody/tr["+str(p)+"]/td[1]"))
        time.sleep(2) 
        
        moneda = S("//*[@id=\"billetes\"]/table/tbody/tr["+str(p)+"]/td[1]").web_element.text 
        print("Descargando Cotizacion para " + moneda)
            
        compra = S("//*[@id=\"billetes\"]/table/tbody/tr["+str(p)+"]/td[2]").web_element.text
        venta = S("//*[@id=\"billetes\"]/table/tbody/tr["+str(p)+"]/td[3]").web_element.text
        sCotizaciones += moneda + "\t" + compra + "\t" + venta + "\n"
                
        p = p+1
    else:
        break

print('Generando archivo de datos ' + cotizacionesFile)
f = open(cotizacionesFile, 'w')
f.write(sCotizaciones)
f.close()
						
kill_browser()
