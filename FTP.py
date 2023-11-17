import ftplib 
import time


class FTP:
     
    def read_txt(self):
      txt = open("Info_connexion.txt", "r")
      liste_txt = txt.readlines()
      IP = liste_txt[2].replace('IP_FTP : ','')
      user = liste_txt[3].replace('User : ','')
      pswd = liste_txt[4].replace('password : ','')
      DestFile = liste_txt[5].replace('Fichier Destination : ','')
      return IP,user,pswd,DestFile
      
    def ConnectToFTP(self):
	    retr_values = f.read_txt()
	    liste = list(retr_values)
	    IP_FTP = retr_values[0]
	    User_FTP = retr_values[1]
	    pswd_FTP = retr_values[2]
	    DestFile = retr_values[3]
	    print (IP_FTP)
	    #ftp = ftplib.FTP(IP_FTP)
	    #ftp.login(user=User_FTP, passwd=pswd_FTP)
	    #ftp.cwd(DestFile)
	    ftp = ftplib.FTP("10.0.134.14")
	    ftp.login(user="WebTV", passwd="WebTV")
	    ftp.cwd("Camera")
	    return ftp
	    
	    
    def GetImg(self,ftp):
        nb=0
        while True:
         nb = int(nb)   
         nb = nb+1
         nb = str(nb)
         #on définit le nom du fichier qu'on veut recuperer
         filename = 'img'+ nb +'.jpg'
         #envoi d'une trame au serveur FTP pour lui indiquer le fichier qu'on veut recuperer
         with open(filename, 'wb') as fp:
          ftp.retrbinary('RETR '+ filename, fp.write)
        ftp.quit()   

f = FTP()
ftp = f.ConnectToFTP()
f.GetImg(ftp)
 
