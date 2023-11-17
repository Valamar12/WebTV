import mysql.connector
from CPT_Temp import CPT_TEMP


class BDD:
     
    def read_txt(self):
      txt = open("Info_connexion.txt", "r")
      liste_txt = txt.readlines()
      IP = liste_txt[9].replace('IP_BDD : ','')
      user = liste_txt[10].replace('user : ','')
      pswd = liste_txt[11].replace('password : ','')
      DB = liste_txt[12].replace('DB : ','')
      return IP,user,pswd,DB
      
    def ConnectToBDD(self): 
	    b = BDD()
	    retr_values = b.read_txt()
	    liste = list(retr_values)
	    IP_BDD = retr_values[0]
	    User_BDD = retr_values[1]
	    pswd_BDD = str(retr_values[2])
	    print(pswd_BDD)
	    DB_BDD = retr_values[3]
	    bdd = mysql.connector.connect(host=IP_BDD,user=User_BDD,password="WebTV",database=DB_BDD)
	    return bdd

    def EnvoiBDD(Temp):
      b = BDD()
      bdd = b.ConnectToBDD()
      curseur = bdd.cursor()
      curseur.execute("INSERT INTO meteo (id, temperature, vent, humidite) VALUES (NULL,"+Temp+",0,0);")
      bdd.commit()
      bdd.close()  


