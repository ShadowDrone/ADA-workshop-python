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

print ('Comienzo Ejecucion Robot que busca una peli en particular')

		#va a la pagina
go_to("https://www.cinepolis.com.ar/")

select("Complejo", "Cinépolis Caballito")

time.sleep(2) 
click("Classic")
time.sleep(2) 
click("2D")

time.sleep(10)
click("Star Wars: El ascenso de Skywalker")


#kill_browser()
