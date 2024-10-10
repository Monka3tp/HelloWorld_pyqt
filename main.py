import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.okButton.clicked.connect(self.on_button_clicked) #BEZ NAWIASOW bo wywolalaby sie funkcja a nie dana wartosc
        self.show()
    def on_button_clicked(self):
        name = self.ui.nameEdit.text()
        self.ui.nameLabel.setText(f'Czesc {name}')


if __name__ == '__main__':
    app = QApplication(sys.argv) #stworzenie aplikacji
    window = MyWindow() #stworzenie okienka
    sys.exit(app.exec())