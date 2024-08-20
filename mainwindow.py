# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from Database import Database
from Items import Items
from Kiosks import Kiosks
from ui_form import Ui_MainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from User import User


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database("test.db")
        self.items_table = Items(self.db)
        self.user_table = User(self.db)
        self.kiosks_table = Kiosks(self.db)

    def __del__(self):
        self.db.commit()
        self.db.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
