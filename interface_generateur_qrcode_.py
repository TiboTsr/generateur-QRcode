from CreateurdeQRcode import QRCodeGenerator

def generate_qrcode_interface():
    """
    Lance l'interface de génération de QR Code.

    Cette fonction initialise un générateur de QR Code et lance son interface utilisateur en ligne de commande.
    Les utilisateurs pourront personnaliser les QR Codes en choisissant la langue, le niveau de personnalisation,
    les données à partager, la version du QR Code, la taille, les couleurs, et bien plus encore.

    Usage :
    1. Importez cette fonction depuis le module CreateurdeQRcode.
    2. Appelez la fonction pour lancer l'interface utilisateur.

    Exemple :
    ```
    from CreateurdeQRcode import QRCodeGenerator
    from CreateurdeQRcode import generate_qrcode_interface

    generate_qrcode_interface()
    ```

    Remarque :
    - Assurez-vous d'avoir installé toutes les dépendances nécessaires, y compris qrcode et Pillow (PIL).
    - Cette interface permet de générer des QR Codes personnalisés pour diverses utilisations, telles que la diffusion de liens,
      de numéros de téléphone, l'affichage de données, et bien plus encore.
    """
    qrcode_generator = QRCodeGenerator()
    qrcode_generator.generate_qrcode() 

generate_qrcode_interface()
