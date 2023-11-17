#!/usr/bin/env python3

from BDD import BDD
from FTP import FTP
from CPT_Temp import CPT_TEMP
#from CPT_Humidite import CPT_HUMIDITE


class Acquisition: 
	
 def GetValeurTemp():
  Temp = t.read_temp()
  return Temp
  
 #def GetValeurHumidite():
  #h = CPT_HUMIDITE
  #humidite = h.readChannel(0)
  #return humidite
  
 def EnvoiBDD(Temp):
      b = BDD()
      bdd = b.ConnectToBDD()
      curseur = bdd.cursor()
      curseur.execute("INSERT INTO meteo (temperature, vent, humidite) VALUES ("+Temp+",0,0);")
      bdd.commit()
      bdd.close()  

t = CPT_TEMP() 
Acquisition.EnvoiBDD(Acquisition.GetValeurTemp())




