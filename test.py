Python 3.7.2 (default, Jan  2 2019, 17:07:39) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import PyqT5
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import PyqT5
ModuleNotFoundError: No module named 'PyqT5'
>>> import PyQt5
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import PyQt5
ModuleNotFoundError: No module named 'PyQt5'
>>> from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QFileDialog
import sys

# Fonction pour créer un contact (ici une fonction simple qui renvoie un dictionnaire)
def creer_contact(nom, prenom, adresse):
    return {'nom': nom, 'prenom': prenom, 'adresse': adresse}

# Fonction pour ajouter un contact à la liste
def ajouter_carnet(liste_contact, nom, prenom, adresse):
    return liste_contact.append(creer_contact(nom, prenom, adresse))

# Fonction pour enregistrer les contacts dans un fichier .txt
def enregistrer_carnet(fichier, carnet):
    with open(fichier, 'w') as f:
        for contact in carnet:
            nom = contact["nom"]
            prenom = contact["prenom"]
            adresse = contact["adresse"]
            ligne = f"{nom}///STOP///{prenom}///STOP///{adresse}\n"
            f.write(ligne)
          time.sleep()
            
def trier_carnet(carnet):
    return sort(carnet)

# Fonction pour charger un carnet à partir d'un fichier .txt
def charger_carnet(fichier):
    carnet = []
    with open(fichier, 'r') as f:
        for ligne in f:
            nom, prenom, adresse = ligne.strip().split("///STOP///")
            carnet.append(creer_contact(nom, prenom, adresse))
    return carnet

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 300, 1000, 400)
        self.setWindowTitle("Ajouter/Charger Contact")

        # Création des widgets
        self.ajouter_contact = QPushButton('Ajouter le contact', self)
        self.nom = QLineEdit(self)
        self.prenom = QLineEdit(self)
        self.adresse = QLineEdit(self)

        # Table widget pour afficher les contacts ajoutés
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['Nom', 'Prénom', 'Adresse'])

        # Connexion du bouton au slot
        self.ajouter_contact.clicked.connect(self.on_ajouter_contact)

        # Zone de texte et bouton pour enregistrer le carnet
        self.nom_fichier = QLineEdit(self)
        self.enregistrer_carnet_btn = QPushButton('Enregistrer carnet', self)
        self.enregistrer_carnet_btn.clicked.connect(self.on_enregistrer_carnet)

        # Zone de texte et bouton pour charger un carnet
        self.charger_fichier = QLineEdit(self)
        self.charger_carnet_btn = QPushButton('Charger carnet', self)
        self.charger_carnet_btn.clicked.connect(self.on_charger_carnet)

        # Table widget pour afficher les contacts chargés
        self.table_charger_widget = QTableWidget(self)
        self.table_charger_widget.setColumnCount(3)
        self.table_charger_widget.setHorizontalHeaderLabels(['Nom', 'Prénom', 'Adresse'])

        # Configuration des layouts
        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel('Nom:', self))
        form_layout.addWidget(self.nom)
        form_layout.addWidget(QLabel('Prénom:', self))
        form_layout.addWidget(self.prenom)
        form_layout.addWidget(QLabel('Adresse:', self))
        form_layout.addWidget(self.adresse)
        form_layout.addWidget(self.ajouter_contact)

        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table_widget)

        # Ajout du champ pour le nom du fichier et du bouton "Enregistrer"
        save_layout = QVBoxLayout()
        save_layout.addWidget(QLabel('Nom du fichier:', self))
        save_layout.addWidget(self.nom_fichier)
        save_layout.addWidget(self.enregistrer_carnet_btn)

        # Ajout du champ pour le nom du fichier à charger et du bouton "Charger"
        load_layout = QVBoxLayout()
        load_layout.addWidget(QLabel('Nom du fichier à charger:', self))
        load_layout.addWidget(self.charger_fichier)
        load_layout.addWidget(self.charger_carnet_btn)
        load_layout.addWidget(self.table_charger_widget)

        main_layout = QHBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(table_layout)
        main_layout.addLayout(save_layout)
        main_layout.addLayout(load_layout)

        self.setLayout(main_layout)
        
        # Liste pour stocker les contacts ajoutés
        self.liste_contact = []

    def on_ajouter_contact(self):
        # Récupération des valeurs des QLineEdit
        nom = self.nom.text()
        prenom = self.prenom.text()
        adresse = self.adresse.text()
        
        # Appel de la fonction ajouter_carnet
        ajouter_carnet(self.liste_contact, nom, prenom, adresse)
        
        # Afficher les contacts dans la console pour vérification
        print(self.liste_contact)
        
        # Vider les zones de texte
        self.nom.clear()
        self.prenom.clear()
        self.adresse.clear()
        
        # Mettre à jour le tableau
        self.update_table()

    def update_table(self):
        # Mise à jour du nombre de lignes dans le tableau
        self.table_widget.setRowCount(len(self.liste_contact))
        
        # Remplissage du tableau avec les contacts
        for row, contact in enumerate(self.liste_contact):
            self.table_widget.setItem(row, 0, QTableWidgetItem(contact['nom']))
            self.table_widget.setItem(row, 1, QTableWidgetItem(contact['prenom']))
            self.table_widget.setItem(row, 2, QTableWidgetItem(contact['adresse']))

    def on_enregistrer_carnet(self):
        # Récupération du nom du fichier depuis la zone de texte
        nom_fichier = self.nom_fichier.text()
        
        if not nom_fichier.endswith('.txt'):
            nom_fichier += '.txt'  # Ajoute l'extension .txt si elle n'est pas présente
        
        # Appel de la fonction enregistrer_carnet
        enregistrer_carnet(nom_fichier, self.liste_contact)

    def on_charger_carnet(self):
        # Récupération du nom du fichier depuis la zone de texte
        nom_fichier = self.charger_fichier.text()
        
        if not nom_fichier.endswith('.txt'):
            nom_fichier += '.txt'  # Ajoute l'extension .txt si elle n'est pas présente
        
        # Charger le carnet depuis le fichier
        carnet_charge = charger_carnet(nom_fichier)
        
        # Afficher les contacts chargés dans le tableau
        self.table_charger_widget.setRowCount(len(carnet_charge))
        for row, contact in enumerate(carnet_charge):
            self.table_charger_widget.setItem(row, 0, QTableWidgetItem(contact['nom']))
            self.table_charger_widget.setItem(row, 1, QTableWidgetItem(contact['prenom']))
            self.table_charger_widget.setItem(row, 2, QTableWidgetItem(contact['adresse']))

# Code pour exécuter l'application PyQt
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

