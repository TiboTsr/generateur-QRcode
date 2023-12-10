import qrcode
import os
from PIL import Image
from urllib.parse import urlparse


class QRCodeGenerator:
    def __init__(self):
        """
        Initialise le générateur de codes QR avec les couleurs et le répertoire de téléchargement par défaut.
        """
        self.colors = {
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "red": (255, 0, 0),
            "green": (0, 128, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "pink": (255, 182, 193),
            "purple": (128, 0, 128),
            "orange": (255, 165, 0),
            "brown": (139, 69, 19),
            "gray": (128, 128, 128),
            "cyan": (0, 255, 255)
        }
        self.download_dir = os.path.expanduser('~') + '/Downloads/'

    def input_validation_color(self, prompt, language):
        """
        Valide la saisie de la couleur fournie par l'utilisateur.
        
        :param prompt: Le message de saisie pour l'utilisateur.
        :param language: La langue dans laquelle afficher les messages d'erreur.
        :return: La couleur validée.
        """
        while True:
            user_input = input(prompt).strip()
            validated_color = self.convert_color(user_input, language)
            if validated_color:
                return validated_color
            else:
                if language == 'fr':
                    print("Couleur invalide. Merci de réessayer.")
                else:
                    print("Invalid color. Please try again.")

    def input_validation_int(self, prompt, min_val, max_val, language):
        """
        Valide la saisie d'un entier dans une plage donnée.
        
        :param prompt: Le message de saisie pour l'utilisateur.
        :param min_val: La valeur minimale permise.
        :param max_val: La valeur maximale permise.
        :param language: La langue dans laquelle afficher les messages d'erreur.
        :return: L'entier validé.
        """
        while True:
            try:
                user_input = int(input(prompt))
                if min_val <= user_input <= max_val:
                    return user_input
                else:
                    if language == 'fr':
                        print(f"La valeur doit être comprise entre {min_val} et {max_val}. Réessayez.")
                    else:
                        print(f"The value must be between {min_val} and {max_val}. Try again.")
            except ValueError:
                if language == 'fr':
                    print("Erreur : Entrez un nombre entier valide.")
                else:
                    print("Error: Enter a valid integer.")


    def convert_color(self, color_name, language):
        """
        Convertit le nom de la couleur en une valeur RVB.
        
        :param color_name: Le nom de la couleur.
        :param language: La langue dans laquelle effectuer la conversion.
        :return: La valeur RVB de la couleur ou None si invalide.
        """
        if language == 'fr':
            translations = {
                "noir": "black", "blanc": "white", "rouge": "red", "vert": "green", "bleu": "blue",
                "jaune": "yellow", "rose": "pink", "violet": "purple", "orange": "orange", "marron": "brown",
                "gris": "gray", "cyan": "cyan"
            }
            translated_color = translations.get(color_name, color_name)
        else:
            translated_color = color_name

        return self.colors.get(translated_color)

    def input_validation_url(self, url, language):
        """
        Valide la saisie d'une URL.
        
        :param url: Le message de saisie pour l'utilisateur.
        :param language: La langue dans laquelle afficher les messages d'erreur.
        :return: L'URL validée.
        """
        while True:
            user_input = input(url).strip()
            parsed_url = urlparse(user_input)
            if parsed_url.scheme and parsed_url.netloc:
                return user_input
            else:
                if language == 'fr':
                    print("Lien invalide. Veuillez entrer un lien valide (par exemple, https://www.example.com).")
                else:
                    print("Invalid link. Please enter a valid link (for example, https://www.example.com).")

    def language_select(self):
        """
        Permet à l'utilisateur de sélectionner une langue (français ou anglais).
        
        :return: La langue sélectionnée.
        """
        while True:
            selected_language = input(
                "Select your language - Enter 'fr' for French or 'en' for English: \n"
                "Choisissez votre langue - Entrez 'fr' pour le Français et 'en' pour l'Anglais : ")

            if selected_language.lower() in ['fr', 'en']:
                return selected_language.lower()
            print("Invalid input. Please enter 'fr' for French or 'en' for English.")
            print("Entrée invalide. Merci d'entrer 'fr' pour le Français ou 'en' pour l'anglais")

    def input_validation_format(self, format, langue):
        """
        Valide la saisie du format de fichier.
        
        :param format: Le message de saisie pour l'utilisateur.
        :param langue: La langue dans laquelle afficher les messages d'erreur.
        :return: Le format validé.
        """
        formats_accept = ["JPG", "PNG", "ICO"]
        error_message = ("Invalid file format. Please choose from the following formats: "
                         "JPG, PNG, ICO" if langue == "en" else
                         "Format de fichier invalide. Veuillez choisir parmi les formats suivants : "
                         "JPG, PNG, ICO")

        while True:
            user_input = input(format).strip().upper()
            if user_input in formats_accept:
                return user_input
            else:
                print(error_message)

    def generate_qrcode(self):
        """
        Génère un code QR en fonction de la langue sélectionnée et du niveau de difficulté.
        """
        selected_language = self.language_select()

        if selected_language == 'fr':
            difficulty_levelFR = self.level_difficulty('fr')
            if difficulty_levelFR == 'facile':
                self.generate_qrcodeFR_f()
            elif difficulty_levelFR == 'difficile':
                self.generate_qrcodeFR_d()
        elif selected_language == 'en':
            difficulty_levelEN = self.level_difficulty('en')
            if difficulty_levelEN == 'easy':
                self.generate_qrcodeEN_f()
            elif difficulty_levelEN == 'hard':
                self.generate_qrcodeEN_d()

    def level_difficulty(self, language):
        """
        Permet à l'utilisateur de choisir le niveau de difficulté.
        
        :param language: La langue dans laquelle afficher les options.
        :return: Le niveau de difficulté sélectionné.
        """
        difficulty_options = {
            'fr': {
                'facile': "Facile (Utilisation simplifiée, idéal pour les débutants)",
                'difficile': "Difficile (Personnalisation avancée)"
            },
            'en': {
                'easy': "Easy (Simplified usage, ideal for beginners)",
                'hard': "Hard (Advanced customization)"
            }
        }

        while True:
            print("Niveau de Difficulté (Choisissez le niveau de personnalisation) :")
            for option, description in difficulty_options[language].items():
                print(f"{option.capitalize()}. {description}")

            choice = input(f"Choisissez le niveau ({', '.join(difficulty_options[language].keys())}) : ").lower().strip()

            if choice in difficulty_options[language]:
                return choice
            else:
                if language == 'fr':
                    print("Choix invalide, merci de choisir parmi les options valides.")
                else:
                    print("Invalid choice, please choose from the valid options.")

    def input_validationFR(self, prompt, validation=None):
        """
        Valide la saisie d'un utilisateur en français.
        
        :param prompt: Le message de saisie pour l'utilisateur.
        :param validation: Une liste de valeurs valides (optionnelle).
        :return: La saisie validée.
        """
        while True:
            user_input = input(prompt).strip()
            if validation is None or user_input in validation:
                return user_input
            print("Entrée invalide. Réessayez.")

    def input_validationEN(self, prompt, validation=None):
        """
        Valide la saisie d'un utilisateur en anglais.
        
        :param prompt: Le message de saisie pour l'utilisateur.
        :param validation: Une liste de valeurs valides (optionnelle).
        :return: La saisie validée.
        """
        while True:
            user_input = input(prompt).strip()
            if validation is None or user_input in validation:
                return user_input
            print("Invalid entry. Please try again.")

    def generate_qrcodeFR_d(self):
        """
        Génère un code QR en français avec un niveau de personnalisation avancé.
        """
        data = self.input_validationFR("Que voulez-vous partager avec le QR code (Mot, lien, numéro de téléphone, SMS ou autre) : ", [
            "mot", "lien", "numéro de téléphone", "sms", "num", "num de tel", "numéro", "autre", "divers"])

        if data.lower() in ['mot', 'texte']:
            data = self.input_validationFR(
                "Entrez le mot ou le texte que vous voulez partager : ")
        elif data.lower() == 'lien':
            data = self.input_validation_url(
                "Entrez le lien que vous voulez partager (sous la forme https://www.exemple.com) : ", 'fr')
        elif data.lower() in ['numéro de téléphone', 'num de tel', 'numéro']:
            phone_number = self.input_validationFR(
                "Entrez le numéro de téléphone que vous voulez partager : ")
            data = f'tel:{phone_number}'
        elif data.lower() == 'sms':
            phone_number = self.input_validationFR(
                "Entrez le numéro de téléphone du destinataire : ")
            message = self.input_validationFR(
                "Entrez le contenu du message à envoyer : ")
            data = f'smsto:{phone_number}:{message}'
        elif data.lower() in ["autre", "divers"]:
            data = self.input_validationFR(
                "Entrez ce que vous voulez partager : ")

        versionQR = self.input_validation_int(
            "Saisissez la version du QR code (De 1 à 40) : ", 1, 40, 'fr')
        box_sizeQR = self.input_validation_int(
            "Saisissez la taille du QR code (De 1 à 50) : ", 1, 50, 'fr')
        borderQR = self.input_validation_int(
            "Saisissez la taille de la bordure du QR code (De 1 à 20) : ", 1, 20, 'fr')

        qr = qrcode.QRCode(version=versionQR,
                           box_size=box_sizeQR, border=borderQR)
        qr.add_data(data)
        qr.make(fit=True)

        color1 = self.input_validation_color(
            "Saisissez la couleur du QR code : ", 'fr')
        color2 = self.input_validation_color(
            "Saisissez la couleur du fond du QR code : ", 'fr')

        img = None

        while color1 == color2:
            print(
                "Vous avez choisi deux fois la même couleur, cela risque de ne pas être visible.")
            choice = input("Voulez vous changer : (oui ou non) :")
            if choice == 'oui':
                color1 = self.input_validation_color(
                    "Saisissez la couleur du QR code : ", 'fr')
                color2 = self.input_validation_color(
                    "Saisissez la couleur du fond du QR code : ", 'fr')
                img = qr.make_image(fill_color=color1, back_color=color2)
            else:
                img = qr.make_image(fill_color=color1, back_color=color2)
        else:
            img = qr.make_image(fill_color=color1, back_color=color2)

        if img is None:
            img = qr.make_image(fill_color=color1, back_color=color2)

        nom_fichier = input("Choisissez le nom du fichier (EX : 'qrcode') : ")

        format_input = self.input_validation_format(
            "Entrez le format du fichier : ", "fr")

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        img_path = os.path.join(self.download_dir, nom_fichier + "." + format_input)
        img.save(img_path)

        print(
            f"Votre QR code vers {data} a bien été enregistré dans le dossier de téléchargement.")

        img.show(img_path)

    def generate_qrcodeFR_f(self):
        """
        Génère un code QR en français avec une utilisation simplifiée.
        """
        data = self.input_validationFR("Que voulez-vous partager avec le QR code (Mot, lien, numéro de téléphone, ou autre) : ", [
            "mot", "lien", "numéro de téléphone", "num", "num de tel", "numéro", "autre", "divers"])

        if data.lower() in ['mot', 'texte']:
            data = self.input_validationFR(
                "Entrez le mot ou le texte que vous voulez partager : ")
        elif data.lower() == 'lien':
            data = self.input_validation_url(
                "Entrez le lien que vous voulez partager (sous la forme https://www.exemple.com) : ", 'fr')
        elif data.lower() in ['numéro de téléphone', 'num de tel', 'numéro']:
            phone_number = self.input_validationFR(
                "Entrez le numéro de téléphone que vous voulez partager : ")
            data = f'tel:{phone_number}'
        elif data.lower() in ["autre", "divers"]:
            data = self.input_validationFR(
                "Entrez ce que vous voulez partager : ")

        qr = qrcode.QRCode(version=10,
                           box_size=15, border=2)
        qr.add_data(data)
        qr.make(fit=True)

        nom_fichier = input("Choisissez le nom du fichier (EX : 'qrcode') : ")

        img = None

        if img is None:
            img = qr.make_image(fill_color="white", back_color="black")

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        img_path = os.path.join(self.download_dir, nom_fichier + '.png')
        img.save(img_path)

        print(
            f"Votre QR code vers {data} a bien été enregistré dans le dossier de téléchargement.")

        img.show(img_path)

    def generate_qrcodeEN_d(self):
        """
        Génère un code QR en anglais avec un niveau de personnalisation avancé.
        """
        data = self.input_validationEN("What do you want to share with the QR code (Word, link, phone number, SMS, or other) : ", [
            "word", "link", "phone number", "sms", "number", "phone num", "numeric", "other", "miscellaneous"])

        if data.lower() in ['word', 'text']:
            data = self.input_validationEN(
                "Enter the word or text you want to share : ")
        elif data.lower() == 'link':
            data = self.input_validation_url(
                "Enter the link you want to share (in the format https://www.example.com) : ", 'en')
        elif data.lower() in ['phone number', 'phone num', 'numeric']:
            phone_number = self.input_validationEN(
                "Enter the phone number you want to share : ")
            data = f'tel:{phone_number}'
        elif data.lower() == 'sms':
            phone_number = self.input_validationEN(
                "Enter the recipient's phone number : ")
            message = self.input_validationEN(
                "Enter the content of the message to send : ")
            data = f'smsto:{phone_number}:{message}'
        elif data.lower() in ["other", "miscellaneous"]:
            data = self.input_validationEN("Enter what you want to share : ")

        versionQR = self.input_validation_int(
            "Enter the QR code version (1 to 40) : ", 1, 40, 'en')
        box_sizeQR = self.input_validation_int(
            "Enter the QR code size (1 to 50) : ", 1, 50, 'en')
        borderQR = self.input_validation_int(
            "Enter the QR code border size (1 to 20) : ", 1, 20, 'en')

        qr = qrcode.QRCode(version=versionQR,
                           box_size=box_sizeQR, border=borderQR)
        qr.add_data(data)
        qr.make(fit=True)

        color1 = self.input_validation_color(
            "Enter the QR code color : ", 'en')
        color2 = self.input_validation_color(
            "Enter the background color of the QR code : ", 'en')

        img = None

        while color1 == color2:
            print("You have chosen the same color twice, which may not be visible.")
            choice = input("Do you want to change it (yes or no) : ")
            if choice == 'yes':
                color1 = self.input_validation_color(
                    "Enter the QR code color : ", 'en')
                color2 = self.input_validation_color(
                    "Enter the background color of the QR code : ", 'en')
                img = qr.make_image(fill_color=color1, back_color=color2)
            else:
                img = qr.make_image(fill_color=color1, back_color=color2)

        if img is None:
            img = qr.make_image(fill_color=color1, back_color=color2)

        file_name = input("Choose the file name (EX: 'qrcode') : ")

        format_input = self.input_validation_format(
            "Enter file format: ", "en")

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        img_path = os.path.join(self.download_dir, file_name + "." + format_input)
        img.save(img_path)

        print(
            f"Your QR code for {data} has been successfully saved in the download folder.")

        img.show(img_path)

    def generate_qrcodeEN_f(self):
        """
        Génère un code QR en anglais avec une utilisation simplifiée.
        """
        data = self.input_validationEN("What do you want to share with the QR code (Word, link, phone number, or other) : ", [
            "word", "link", "phone number", "numeric", "phone num", "numeric", "other", "miscellaneous"])

        if data.lower() in ['word', 'text']:
            data = self.input_validationEN(
                "Enter the word or text you want to share : ")
        elif data.lower() == 'link':
            data = self.input_validation_url(
                "Enter the link you want to share (in the format https://www.example.com) : ", 'en')
        elif data.lower() in ['phone number', 'phone num', 'numeric']:
            phone_number = self.input_validationEN(
                "Enter the phone number you want to share : ")
            data = f'tel:{phone_number}'
        elif data.lower() in ["other", "miscellaneous"]:
            data = self.input_validationEN(
                "Enter what you want to share : ")

        qr = qrcode.QRCode(version=10,
                           box_size=15, border=2)
        qr.add_data(data)
        qr.make(fit=True)

        img = None

        if img is None:
            img = qr.make_image(fill_color="white", back_color="black")

        file_name = input("Choose the file name (EX: 'qrcode') : ")

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        img_path = os.path.join(self.download_dir, file_name + ".png")
        img.save(img_path)

        print(
            f"Your QR code for {data} has been successfully saved in the download folder.")

        img.show(img_path)
        
