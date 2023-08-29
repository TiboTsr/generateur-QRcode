import qrcode
from PIL import Image
import os

colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "rebeccapurple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]

data1=input("Que voulez vous partager avec le QRcode ('Mot ou texte, lien vers un site, numéro de téléphone ou SMS') : ")

if data1=='Mot ou texte' or data1=='Mot' or data1=='mot' or data1=='texte' or data1=='Texte' or data1=='Textes' or data1=='textes' or data1=='mot ou texte':
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
while versionQR < 1 or versionQR > 40:
    print("Merci d'entrer un nombre entre 1 et 40 :")
    versionQR=int(input("Saisissez la version du QRcode (De 1 à 40) : "))
box_sizeQR=int(input("Saisissez la taille du QRcode (De 1 à 50) : "))
while box_sizeQR < 1 or box_sizeQR > 50:
    print("Merci d'entrer un nombre entre 1 et 50 :")
    box_sizeQR=int(input("Saisissez la taille du QRcode (De 1 à 50) : "))
borderQR=int(input("Saisissez la taille de la bordure du QR code (De 1 à 20) : "))
while borderQR < 1 or borderQR > 20 : 
    print("Merci d'entrer un nombre entre 1 et 20 : ")
    borderQR=int(input("Saisissez la taille de la bordure du QR code (De 1 à 20) : "))

qr=qrcode.QRCode(version=versionQR, box_size=box_sizeQR, border=borderQR)

qr.add_data(data)

qr.make(fit=True)

color1=input("Saisissez la couleur de votre choix pour le QRcode (En anglais) : ")
while color1 not in colors :
    print("Couleur invalide. Veuillez réessayer.")
    color1=input("Saisissez la couleur de votre choix pour le QRcode (En anglais) : ")
color2=input("Saisissez la couleur de votre choix pour le fond du QRcode (En anglais) : ")
while color2 not in colors : 
    print("Couleur invalide. Veuillez réessayer.")
    color2=input("Saisissez la couleur de votre choix pour le fond du QRcode (En anglais) : ")
if color2 == color1 : 
    print("Vous avez choisis 2 fois les mêmes couleurs, cela risque de ne pas être visible")
    choix=input("Voulez vous changer : (oui ou non) :")
    if choix=='oui':
        color2=input("Saisissez la couleur de votre choix pour le fond du QRcode (En anglais) : ")
        img=qr.make_image(fill_color=color1,back_color=color2)
    else :
        img=qr.make_image(fill_color=color1,back_color=color2)
else : 
    img=qr.make_image(fill_color=color1,back_color=color2)

download_dir = os.path.expanduser('~') + '/Downloads/'

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

img.save(os.path.join(download_dir, 'qrcode.png'))

print("Votre QRcode vers", data, "a bien été enregistré dans le dossier téléchargement")

image = Image.open((os.path.join(download_dir, 'qrcode.png')))
image.show()
