import random
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIntValidator
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpinBox, QFrame, QSplitter, QFormLayout,
    QPushButton
)
from drone import Drone
from gps import GPS


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


class SetParamsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.common_box = QFormLayout(self)
        self.init_ui()

    def init_ui(self):
        # Валидация целочисленного ввода
        int_val = QIntValidator()
        int_val.setRange(0, 50)
        # Название виджета
        label = QLabel("Параметры полета")
        self.common_box.addRow(label)
        # Установка скорости полета
        velocity = QSpinBox(minimum=1, maximum=10, value=0)
        velocity.setFixedSize(50, 25)
        self.common_box.addRow("Скорость (м/с):", velocity)
        # Установка высоты полета
        height = QSpinBox(minimum=0, maximum=1000, value=5)
        height.setFixedSize(50, 25)
        self.common_box.addRow("Высота (м):", height)
        # Начальные координаты миссии
        start_label = QLabel("Точка старта")
        self.common_box.addRow(start_label)
        set_x_1 = QLineEdit()
        set_x_1.setFixedSize(50, 25)
        set_x_1.setValidator(int_val)
        self.common_box.addRow('x:', set_x_1)
        set_y_1 = QLineEdit()
        set_y_1.setFixedSize(50, 25)
        set_y_1.setValidator(int_val)
        self.common_box.addRow('y', set_y_1)
        # Конечные координаты миссии
        end_label = QLabel("Точка назначения")
        self.common_box.addRow(end_label)
        set_x_2 = QLineEdit()
        set_x_2.setFixedSize(50, 25)
        set_x_2.setValidator(int_val)
        self.common_box.addRow("x:", set_x_2)
        set_y_2 = QLineEdit()
        set_y_2.setFixedSize(50, 25)
        set_y_2.setValidator(int_val)
        self.common_box.addRow("y:", set_y_2)
        # Закинем кнопку, которая задизеблит все поля для ввода в виджете
        load_btn = QPushButton("Загрузить миссию", clicked=self.set_disable_param)
        self.common_box.addRow(load_btn)
        # Кнопка Старт
        start_btn = QPushButton("Взлететь")
        start_btn.setDisabled(True)
        self.common_box.addRow(start_btn)
        # Кнопка Посадка
        landing_btn = QPushButton("Приземлиться")
        landing_btn.setDisabled(True)
        self.common_box.addRow(landing_btn)
        #
        self.setLayout(self.common_box)
        self.show()

    def set_disable_param(self):
        for i in range(self.layout().count()):
            if (str(self.layout().itemAt(i).widget().objectName).find("QLabel") > -1 or
                    str(self.layout().itemAt(i).widget().objectName).find("QPushButton") > -1):
                self.layout().itemAt(i).widget().setDisabled(False)
            else:
                self.layout().itemAt(i).widget().setDisabled(True)


class ActionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.common_box = QHBoxLayout()
        self.gps_lbl = QLabel("GPS: ")
        self.coord_lbl = QLabel("x=0; y=0; z=0")
        self.btn_gps = QPushButton("↻")
        self.init_ui()

    def init_ui(self):
        self.btn_gps.clicked.connect(self.update_gps)
        self.common_box.addWidget(self.gps_lbl)
        self.common_box.addWidget(self.coord_lbl)
        self.common_box.addWidget(self.btn_gps)
        #
        self.setLayout(self.common_box)
        self.show()

    def update_gps(self):
        # Тут имитация апдейта координат Дрона.
        # В реальности наддо опрашивать Дрон и выводить его текущие координаты
        print("GPS updeted")
        self.coord_lbl.setText(f'x={random.randint(0, 30)}; y={random.randint(0, 30)};' \
                               f' z={random.randint(0, 30)}')


class DroneUI(QWidget):
    def __init__(self):
        super().__init__()
        # Инициируем Дрон с координатами
        self.start_position = GPS(x=0, y=0, z=0)
        self.destination = GPS(x=100, y=100, z=0)
        self.drone = Drone(self.start_position, "MyDrone")
        self.h_box = QHBoxLayout(self)
        self.init_ui()

    def init_ui(self):
        frame_left = QFrame(self)
        frame_left.setFrameShape(QFrame.Shape.StyledPanel)
        frame_left.setFixedSize(640, 500)
        #
        layout_map = QHBoxLayout()
        interactive_map = MapWidget()
        layout_map.addWidget(interactive_map)
        frame_left.setLayout(layout_map)
        #
        frame_right = QFrame(self)
        frame_right.setFrameShape(QFrame.Shape.StyledPanel)
        frame_right.setFixedSize(200, 500)
        #
        layout_set_params = QHBoxLayout()
        #
        set_params_widget = SetParamsWidget()
        layout_set_params.addWidget(set_params_widget)
        frame_right.setLayout(layout_set_params)
        layout_set_params.addLayout(layout_set_params)
        #
        frame_bottom = QFrame(self)
        frame_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        frame_bottom.setFixedSize(840, 150)
        #
        layout_set_action = QVBoxLayout()
        set_action = ActionWidget()
        layout_set_action.addWidget(set_action)
        frame_bottom.setLayout(layout_set_action)
        #
        splitter_1 = QSplitter(Qt.Orientation.Horizontal)
        splitter_1.addWidget(frame_left)
        splitter_1.addWidget(frame_right)
        #
        splitter_2 = QSplitter(Qt.Orientation.Vertical)
        splitter_2.addWidget(splitter_1)
        splitter_2.addWidget(frame_bottom)
        #
        self.h_box.addWidget(splitter_2)
        self.setLayout(self.h_box)
        self.setWindowTitle('Управление квадрокоптером')
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = DroneUI()
    window.show()
    sys.exit(app.exec())
