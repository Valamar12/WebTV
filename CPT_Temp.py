#!/usr/bin/python
import os
import glob
import time

#execute les commandes dans le terminal 
os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')
  
class CPT_TEMP:
 
 def Selectfile():
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '*0*')[0]
    device_file = device_folder + '/w1_slave'
    return device_file
     
 def read_temp_raw(self):
    #on ouvre le fichier "w1_Slave" dont le chemin est defini dans la variable device_file 
    f = open(CPT_TEMP.Selectfile(), 'r')
    #on attribue le contenu du fichier a la variable "lines"
    lines = f.readlines()
    f.close()
    return lines

 def read_temp(self):
    l = CPT_TEMP() 
    lines = l.read_temp_raw()
    #si le CRC est incorrect on attend 0.2sec et on lit la prochaine trame jusqu'a que le CRC soit correct
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = CPT_TEMP.read_temp_raw()
        #on cherche dans la 2eme ligne l'endroit ou est marque "t=" 
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        #on convertit la valeur contenue dans la trame en float
        temp_c = float(temp_string) / 1000.0
        temp_s = str(temp_c)
        return temp_s
    


