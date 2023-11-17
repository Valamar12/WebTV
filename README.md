# WebTV

## I – Matériel et logiciels requis

Entités matérielles :

- Un raspberry PI 
- Un capteur de température DS1822+, marque Maxim Integrated
- Un capteur d’humidité SEN0114, marque DF Robot
- Un convertisseur Analogique – Numérique MCP3008
  
Entités logicielles :
- Exécutable Acquisitions
- Classes : BDD.py, FTP, CPT_Temp.py, CPT_Humidite.py
- un Fichier texte nommé «infos_connexion.txt » avec les informations de connexion au serveur 
FTP et à la base de données
- La base de données « npy »
- Le site web embarqué
- Python 3
  
## II – Configuration de la raspberry
Ouvrir la Configuration du Raspberry PI et activer les interfaces 1-Wire, SPI et SSH
 
Les exécutables FTP et Acquisitions doivent être présents être dans le répertoire 
home/pi/Desktop/WebTV afin que la tâche Cron fonctionne

## III – Installation des logiciels et librairies
Avant l’installation des logiciels, il faut mettre à jour le Rapspberry à l’aide des commandes suivantes à entrer 
sue le terminal de linux

```Bash
sudo apt-get update
sudo apt-get upgrade
```

Python est installé de base avec linux Debian, il suffit juste d’installer la base de données.

### 1. Installation de LAMP
   
Ouvrir le terminal de linux et entrer les commandes suivantes pour installer Apache : 

```Bash
sudo apt install apache2
sudo chown -R pi:www-data /var/www/html/
sudo chmod -R 770 /var/www/html/
```

Toujours dans le terminal entrer la commande suivante pour installer PHP

```Bash
sudo apt install php php-mbstring
```

Entrer la commande suivante pour installer MySQL

```Bash
sudo apt install mariadb-server php-mysql
```

Puis créer un utilisateur avec les commandes:

```SQL
CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT 
OPTION;
```

Afin que le programme d’acquisitions fonctionne, il faudra modifier le fichier “Infos_Connexion.txt” 
et remplacer les champs « user » et « password » avec l’utilisateur et le mot de passe définis avec la 
commande précédente

 
Pour finir, installer PHPmyAdmin avec la commande : 

```Bash
sudo apt install phpmyadmin
```

### 2. Installation des librairies

La librairie « ftplib » pour la partie ftp est présente de base sur la raspberry, il faut installer les 
autres :

« Mysql connector » pour la base de données : 

```
Sudo pip install mysql-connector-python
```

« Spidev » pour le support du protocole SPI pour le capteur de température

```
Sudo pip install spidev
```

« Glob » afin de sélectionner le fichier ou est contenu la trame du capteur de température

```
pip install glob2
```
Puis « os » afin d’activer des commandes sur le terminal depuis python

```
pip install os-sys
```

### Installation de la base de données
   
Afin d’installer la base de données, il faut accéder a PHPmyAdmin en utilisant l’URL « http://localhost/phpmyadmin/ » sur le navigateur de la raspberry et se connecter avec l’utilisateur et 
l’identifiant définis lors de la création de l’utilisateur lors de l’installation de MySQL.
Appuyer sur choisir un fichier et sélectionner la base de données « npy.sql » qui est fournie avec les exécutables d’acquisition puis appuyer sur exécuter en bas de la page.
