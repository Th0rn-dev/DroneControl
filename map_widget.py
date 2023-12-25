from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QWidget


class MapWidget(QWidget):
    def __init__(self):
        super().__init__()
        # UI init
        self.common_box = QVBoxLayout()
        self.init_ui()

    def init_ui(self):
        # Лейбл
        lbl = QLabel("Карта местности")
        self.common_box.addWidget(lbl)
        # Карта
        pix_map = QLabel(self)
        pix_map.setPixmap(QPixmap("./images/region.png"))
        self.common_box.addWidget(pix_map)
        # Отображаем виджет
        self.setLayout(self.common_box)
        self.show()
