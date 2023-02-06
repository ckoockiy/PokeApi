from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QLabel
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import QSize
import sys
from fetch_pokemon import getPokemon
from random import randint


class Application(QWidget):
    def __init__(self):
        super(Application, self).__init__()
        self.setFixedSize(320, 250)
        self.setWindowTitle("POKEMON")
        self.setup_ui()


    def setup_ui(self):
        self.font_style_size = QFont('Arial Rounded MT', 10)

        # nombre
        self.nombre = QLabel(self)
        self.nombre.setFont(self.font_style_size)
        self.nombre.move(30, 20)

        # HP pokemon
        self.hp_pokemon = QLabel(self)
        self.hp_pokemon.setFont(self.font_style_size)
        self.hp_pokemon.move(30, 40)

        # attack pokemon
        self.attack_pokemon = QLabel(self)
        self.attack_pokemon.setFont(self.font_style_size)
        self.attack_pokemon.move(30, 60)

        # defense pokemon
        self.defense_pokemon = QLabel(self)
        self.defense_pokemon.setFont(self.font_style_size)
        self.defense_pokemon.move(30, 80)

        # special_attack pokemon
        self.special_attack_pokemon = QLabel(self)
        self.special_attack_pokemon.setFont(self.font_style_size)
        self.special_attack_pokemon.move(30, 100)

        # special_defense pokemon
        self.special_defense_pokemon = QLabel(self)
        self.special_defense_pokemon.setFont(self.font_style_size)
        self.special_defense_pokemon.move(30, 120)

        # speed pokemon
        self.speedpokemon = QLabel(self)
        self.speedpokemon.setFont(self.font_style_size)
        self.speedpokemon.move(30, 140)

        # imagen pokemon
        self.imagenlabel = QLabel(self)
        self.imagenlabel.move(200, 30)

        # self.emptyWindow()
        self.displayLabels()
        self.displayButtons()

    def displayLabels(self):

        number = randint(1, 899)

        pokemon = getPokemon(number)

        # nombre
        self.nombre.setText("NOMBRE: "+str(pokemon[0][0]).upper())
        self.nombre.adjustSize()

        # HP pokemon
        self.hp_pokemon.setText('HP: '+str(pokemon[0][2]))
        self.hp_pokemon.adjustSize()

        # attack pokemon
        self.attack_pokemon.setText('ATTACK: '+str(pokemon[0][3]))
        self.attack_pokemon.adjustSize()

        # defense pokemon
        self.defense_pokemon.setText('DEFENSE: '+str(pokemon[0][4]))
        self.defense_pokemon.adjustSize()

        # special_attack pokemon
        self.special_attack_pokemon.setText(
            'SPEACIAL ATTACK: '+str(pokemon[0][5]))
        self.special_attack_pokemon.adjustSize()

        # special_defense pokemon
        self.special_defense_pokemon.setText(
            'SPEACIAL DEFENSE: '+str(pokemon[0][6]))
        self.special_defense_pokemon.adjustSize()

        # speed pokemon
        self.speedpokemon.setText('SPEED: '+str(pokemon[0][7]))
        self.speedpokemon.adjustSize()

        # imagen pokemon
        foto = pokemon[0][1]
        pixmap = QPixmap()
        pixmap.loadFromData(foto)
        self.imagenlabel.setPixmap(pixmap)
        self.imagenlabel.adjustSize()

    def displayButtons(self):
        self.btn1 = QPushButton("Buscar Pokemon", self)
        self.btn1.move(100, 200)
        self.btn1.clicked.connect(self.displayLabels)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('ico-pokemon.png'))
    window = Application()
    window.show()
    sys.exit(app.exec())
