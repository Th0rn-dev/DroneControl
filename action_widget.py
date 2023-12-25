import random

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QPushButton, QPlainTextEdit
)


class ActionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.console = None
        self.setObjectName('action_widget')
        self.set_console_enabled = False
        self.common_box = QHBoxLayout()
        self.gps_lbl = QLabel("GPS: ")
        self.coord_lbl = QLabel("x=0; y=0; z=0")
        self.btn_gps = QPushButton("↻")
        self.btn_gps.clicked.connect(self.update_gps)
        self.common_box.addWidget(self.gps_lbl)
        self.common_box.addWidget(self.coord_lbl)
        self.common_box.addWidget(self.btn_gps)
        # Отображаем консоль
        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)
        self.console.setStyleSheet("QPlainTextEdit{background-color: black; color: white;}")
        self.console.setVisible(self.set_console_enabled)
        #
        self.common_box.addWidget(self.console)
        self.setLayout(self.common_box)
        self.show()

    def update_gps(self):
        # Тут имитация апдейта координат Дрона.
        # В реальности наддо опрашивать Дрон и выводить его текущие координаты
        print("GPS updeted")
        self.coord_lbl.setText(f'x={random.randint(0, 30)}; y={random.randint(0, 30)};' \
                               f' z={random.randint(0, 30)}')
        self.console.appendPlainText(f'GPS {{x: {random.randint(0, 30)}, y: {random.randint(0, 30)},' \
                                     f' z: {random.randint(0, 30)}}}')
