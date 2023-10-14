import qrcode
import os
from PIL import Image

class QRCodeGenerator:
    def __init__(self):
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

    def input_validation_colorFR(self, prompt, language):
        """
        Valide et convertit une couleur entrée par l'utilisateur en français.

        Args:
            prompt (str): Message à afficher pour inviter l'utilisateur à entrer une couleur.
            language (str): Langue actuelle (français ou anglais).

        Returns:
            tuple: Un tuple représentant la couleur (RVB) valide ou None si la couleur est invalide.
        """
        while True:
            user_input = input(prompt).strip()
            validated_color = self.convert_color(user_input, language)
            if validated_color:
                return validated_color
            print("Couleur invalide. Merci de réessayer.")

    def input_validation_colorEN(self, prompt, language):
        """
        Valide et convertit une couleur entrée par l'utilisateur en anglais.

        Args:
            prompt (str): Message à afficher pour inviter l'utilisateur à entrer une couleur.
            language (str): Langue actuelle (français ou anglais).

        Returns:
            tuple: Un tuple représentant la couleur (RVB) valide ou None si la couleur est invalide.
        """
        while True:
            user_input = input(prompt).strip()
            validated_color = self.convert_color(user_input, language)
            if validated_color:
                return validated_color
            print("Invalid color. Please try again.")

    def input_validation_intFR(self, prompt, min_val, max_val):
        """
        Valide et convertit un entier entré par l'utilisateur en français.

        Args:
            prompt (str): Message à afficher pour inviter l'utilisateur à entrer un entier.
            min_val (int): Valeur minimale acceptée.
            max_val (int): Valeur maximale acceptée.

        Returns:
            int: L'entier valide.
        """
        while True:
            try:
                user_input = int(input(prompt))
                if min_val <= user_input <= max_val:
                    return user_input
                else:
                    print(f"La valeur doit être comprise entre {min_val} et {max_val}. Réessayez.")
            except ValueError:
                print("Erreur : Entrez un nombre entier valide.")

    def input_validation_intEN(self, prompt, min_val, max_val):
        """
        Valide et convertit un entier entré par l'utilisateur en anglais.

        Args:
            prompt (str): Message à afficher pour inviter l'utilisateur à entrer un entier.
            min_val (int): Valeur minimale acceptée.
            max_val (int): Valeur maximale acceptée.

        Returns:
            int: L'entier valide.
        """
        while True:
            try:
                user_input = int(input(prompt))
                if min_val <= user_input <= max_val:
                    return user_input
                else:
                    print(f"The value must be between {min_val} and {max_val}. Try again.")
            except ValueError:
                print("Error: Enter a valid integer.")

    def convert_color(self, color_name, language):
        """
        Convertit un nom de couleur dans la langue spécifiée en une valeur RVB.

        Args:
            color_name (str): Nom de la couleur à convertir.
            language (str): Langue actuelle (français ou anglais).

        Returns:
            tuple: Un tuple représentant la couleur (RVB) ou None si la couleur n'est pas reconnue.
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

    def language_select(self):
        """
        Permet à l'utilisateur de sélectionner une langue (français ou anglais).

        Returns:
            str: La langue sélectionnée (français ou anglais).
        """
        while True:
            selected_language = input("Select your language - Enter 'fr' for French or 'en' for English: ")
            if selected_language.lower() in ['fr', 'en']:
                return selected_language.lower()
            print("Invalid input. Please enter 'fr' for French or 'en' for English.")

    def generate_qrcode(self):
        selected_language = self.language_select()

        if selected_language == 'fr':
            self.generate_qrcodeFR(selected_language)
        elif selected_language == 'en':
            self.generate_qrcodeEN(selected_language)

    def input_validationFR(self, prompt, validation=None):
        """
        Valide une entrée de l'utilisateur en français.

        Args:
            prompt (str): Message à afficher pour inviter l'utilisateur à entrer une valeur.
            validation (list): Liste des valeurs valides (ou None pour accepter n'importe quelle valeur).

        Returns:
            str: L'entrée validée.
        """
        while True:
            user_input = input(prompt).strip()
            if validation is None or user_input in validation:
                return user_input
            print("Entrée invalide. Réessayez.")

    def input_validationEN(self, prompt, validation=None):
        """
        Valide une entrée de l'utilisateur en anglais.

        Args:
            prompt (str): Message à afficher pour inviter l'utilisateur à entrer une valeur.
            validation (list): Liste des valeurs valides (ou None pour accepter n'importe quelle valeur).

        Returns:
            str: L'entrée validée.
        """
        while True:
            user_input = input(prompt).strip()
            if validation is None or user_input in validation:
                return user_input
            print("Invalid entry. Please try again.")

    def generate_qrcodeFR(self, selected_language):
        """
        Génère un code QR en utilisant les préférences de l'utilisateur en français.

        Args:
            selected_language (str): Langue sélectionnée (français ou anglais).
        """
        data = self.input_validationFR("Que voulez-vous partager avec le QR code (Mot, lien, numéro de téléphone, SMS ou autre) : ", [
                                 "mot", "lien", "numéro de téléphone", "sms", "num", "num de tel", "numéro", "autre", "divers"])

        if data.lower() in ['mot', 'texte']:
            data = self.input_validationFR(
                "Entrez le mot ou le texte que vous voulez partager : ")
        elif data.lower() == 'lien':
            data = self.input_validationFR(
                "Entrez le lien que vous voulez partager (sous la forme https://www.exemple.com) : ")
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

        versionQR = self.input_validation_intFR("Saisissez la version du QR code (De 1 à 40) : ", 1, 40)
        box_sizeQR = self.input_validation_intFR("Saisissez la taille du QR code (De 1 à 50) : ", 1, 50)
        borderQR = self.input_validation_intFR("Saisissez la taille de la bordure du QR code (De 1 à 20) : ", 1, 20)

        qr = qrcode.QRCode(version=versionQR,
                           box_size=box_sizeQR, border=borderQR)
        qr.add_data(data)
        qr.make(fit=True)

        color1 = self.input_validation_colorFR(
            "Saisissez la couleur du QR code : ", selected_language)
        color2 = self.input_validation_colorFR(
            "Saisissez la couleur du fond du QR code : ", selected_language)

        while color1 == color2:
            print(
                "Vous avez choisi deux fois la même couleur, cela risque de ne pas être visible.")
            choice = input("Voulez vous changer : (oui ou non) :")
            if choice == 'oui':
                color1 = self.input_validation_colorFR(
                    "Saisissez la couleur du QR code : ", selected_language)
                color2 = self.input_validation_colorFR(
                    "Saisissez la couleur du fond du QR code : ", selected_language)
                img = qr.make_image(fill_color=color1, back_color=color2)
            else:
                img = qr.make_image(fill_color=color1, back_color=color2)
        else:
            img = qr.make_image(fill_color=color1, back_color=color2)

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        img_path = os.path.join(self.download_dir, "qrcode.png")
        img.save(img_path)

        print(
            f"Votre QR code vers {data} a bien été enregistré dans le dossier de téléchargement.")

        img.show(img_path)

    def generate_qrcodeEN(self, selected_language):
        """
        Génère un code QR en utilisant les préférences de l'utilisateur en anglais.

        Args:
            selected_language (str): Langue sélectionnée (français ou anglais).
        """
        data = self.input_validationEN("What do you want to share with the QR code (Word, link, phone number, SMS, or other) : ", [
                                "word", "link", "phone number", "sms", "number", "phone num", "numeric", "other", "miscellaneous"])

        if data.lower() in ['word', 'text']:
            data = self.input_validationEN(
                "Enter the word or text you want to share : ")
        elif data.lower() == 'link':
            data = self.input_validationEN(
                "Enter the link you want to share (in the format https://www.example.com) : ")
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

        versionQR = self.input_validationEN(
            "Enter the QR code version (1 to 40) : ", 1, 40)
        box_sizeQR = self.input_validationEN(
            "Enter the QR code size (1 to 50) : ", 1, 50)
        borderQR = self.input_validationEN(
            "Enter the QR code border size (1 to 20) : ", 1, 20)

        qr = qrcode.QRCode(version=versionQR, box_size=box_sizeQR, border=borderQR)
        qr.add_data(data)
        qr.make(fit=True)

        color1 = self.input_validation_colorEN(
            "Enter the QR code color : ", selected_language)
        color2 = self.input_validation_colorEN(
            "Enter the background color of the QR code : ", selected_language)

        while color1 == color2:
            print("You have chosen the same color twice, which may not be visible.")
            choice = input("Do you want to change it (yes or no) : ")
            if choice == 'yes':
                color1 = self.input_validation_colorEN(
                    "Enter the QR code color : ", selected_language)
                color2 = self.input_validation_colorEN(
                    "Enter the background color of the QR code : ", selected_language)
                img = qr.make_image(fill_color=color1, back_color=color2)
            else:
                img = qr.make_image(fill_color=color1, back_color=color2)

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        img_path = os.path.join(self.download_dir, "qrcode.png")
        img.save(img_path)

        print(
            f"Your QR code for {data} has been successfully saved in the download folder.")

        img.show(img_path)

if __name__ == '__main__':
    QRcodeGenerator().generate_qrcode()
