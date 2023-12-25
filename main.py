import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpinBox, QFrame, QSplitter, QFormLayout,
    QPushButton
)
from drone import Drone
from gps import GPS
from action_widget import ActionWidget
from map_widget import MapWidget
from set_widget import SetParamsWidget


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
        frame_left = QFrame()
        frame_left.setFrameShape(QFrame.Shape.StyledPanel)
        frame_left.setFixedSize(640, 500)
        #
        layout_map = QHBoxLayout()
        interactive_map = MapWidget()
        layout_map.addWidget(interactive_map)
        frame_left.setLayout(layout_map)
        #
        frame_right = QFrame()
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
        frame_bottom = QFrame()
        frame_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        frame_bottom.setFixedSize(844, 150)
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
