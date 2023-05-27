import qrcode
from PIL import Image

data1=input("Que voulez vous partager avec le QRcode ('Mot ou texte, lien vers un site, numéro de téléphone ou SMS') : ")

if data1=='Mot ou texte' or data1=='Mot' or data1=='mot' or data1=='texte' or data1=='Texte' or data1=='Textes' or data1=='textes':
    data2=input("Quel est le mot ou le texte que vous voulez partagez avec le QRcode : ")
    data=data2
elif data1=='lien vers un site' or data1=='lien' or data1=='site' or data1=='Lien' or data1=='Site' or data1=='Lien vers un site':
    data2=input("Entrez le lien que vous voulez partager avec le QRcode (Sous la forme https://www.exemple.com) : ")
    data=data2
elif data1=='Numéro de téléphone' or data1=='Numero de telephone' or data1=='numero de telephone' or data1=='numéro de téléphone' or data1=='num de tel' or data1=='Numéro' or data1=='numéro':
    data2=input("Entrez le numéro de téléphone que vous voulez partager avec le QRcode : ")
    data='tel:' + data2
elif data1=='SMS' or data1=='sms' :
    data3=input("Entrez le numéro de téléphone qui doit recevoir le message : ")
    data4=input("Entrez le contenu du message à envoyer : ")
    data='smsto:'+data3+':'+data4


#data=input("Saisissez le lien ou le texte('mot, phrases, date, numéro de tel...') que doit rediriger le QRcode :")

versionQR=int(input("Saisissez la version du QRcode (De 1 à 40) : "))
box_sizeQR=int(input("Saisissez la taille du QRcode (De 1 à 100) : "))
borderQR=int(input("Saisissez la taille de la bordure du QR code (De 1 à 20) : "))

qr=qrcode.QRCode(version=versionQR, box_size=box_sizeQR, border=borderQR)

qr.add_data(data)

qr.make(fit=True)

color1=input("Saisissez la couleur de votre choix pour le QRcode (En anglais) : ")
color2=input("Saisissez la couleur de votre choix pour le fond du QRcode (En anglais) : ")

img=qr.make_image(fill_color=color1,back_color=color2)

img.save('C:/Users/TTESSIER/Downloads/qrcode.png')

print("Votre QRcode vers", data, "a bien été enregistré dans le dossier téléchargement")

image = Image.open('C:/Users/TTESSIER/Downloads/qrcode.png')
image.show()
