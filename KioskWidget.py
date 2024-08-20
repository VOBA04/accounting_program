from PySide6.QtWidgets import QWidget

from Database import Database
from Kiosks import Kiosks


class KioskWidget(QWidget):
    def __init__(self, kiosk_id: int, db: Database, parent=None):
        super().__init__(parent)
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM Kiosks WHERE id=?", (kiosk_id,))
        kiosk = Kiosks.db_to_dict(db, kiosk_id)
