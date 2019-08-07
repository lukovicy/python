# Python skripta za skidanje fotografija sa bilo kog kupujemprodajem.com oglasa u folder sa ID oglasa na 'Documents'
# Alternativa za ubacivanje vise oglasa odjednom je ARRAY ili inputi da se povuku u ARRAY

#neophodni python moduli za funkcionisanje skripte
import requests
import re
import urllib.request
import os
import getpass

# definisanje variable korisnik
korisnik = getpass.getuser()

# definisanje ID oglasa kroz input sa tastature
id_oglasa = input("Upisi ID oglasa: ")
print("\n")

# sendString je variabla koja od ID oglasa sastavlja URL link koji preuzmerava na stranicu gde su fotografije u punoj rezoluciji
sendString = 'https://www.kupujemprodajem.com/big-photo-' + id_oglasa + '-1.htm'
print("Traze se fotografije za weblink: {}\n".format(sendString))

# varijabla data salje GET request za URL koji je definisan
data = requests.get(sendString)

# definisanje variable linkovi sluzi za filtriranje putem regex expression-a
linkovi = re.findall(r'(\/photos\/oglasi\/.*jpg\")', data.text)

# path = input("Gde zelis da se cuvaju slike? ")
path = "/home/" + korisnik + "/Downloads/" + str(id_oglasa) + "/"

# postavljanje count brojaca na 1!
count = 1

#uslov ako postoje linkovi (varijabla)
if linkovi:
	# odstampaj da si nasao linkove i da ces kreirati foldere
	print("Pronasao sam linkove, sledi kreiranje foldera \n")
	# pokusaj da napravis direktorijum na lokaciji variable path pod nazivom ID oglasa
	try:
		os.mkdir(path)
	# osim ako postoji OS Error, onda odstampaj poruku kako kreiranje foldera nije uspelo
	except OSError:
		print("Kreiranje foldera nije uspelo!\n")

	# ako uslov za OS Error nije istinit, obavesti da je folder kreiran i da sledi lista skidanja
	else:
		print("Kreiranje foldera je uspelo, sledi lista skidanja: \n")

	# uslov gde se za brojac (i) u variabli (linkovi):
	for i in linkovi:
		# definise variabla (x) koja splituje i sa "
		x = i.split('"')
		# definise variabla kp koja spaja URL sajta sa x argumentom brojaca i koji izdvaja linkove iz varijable linkovi
		kp = "https://www.kupujemprodajem.com" + x[0]
		# print("Uspesan scrap: " + kp)
		# definisanje variable koja u kreirani folder ubacuje fotografije spajanjem variajbli za dobijanje punog patha
		retrive_name = path + str(id_oglasa) + "-" + str(count) + ".jpg"
		# request za skidanje fotografija
		urllib.request.urlretrieve(kp, retrive_name)
		# uvecavanje brojaca za 1
		count = count + 1

	# poruka o uspesnom preuzimanju fotografija
	print("Fotografije su uspesno preuzete!")

# ako linkovi ne postoje
else:
	# stampanje poruke da uneti ID oglasa nije validan
	print("Uneti ID nije validan!")