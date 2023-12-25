from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget, QFormLayout, QLabel, QSpinBox, QLineEdit, QPushButton, QCheckBox, QApplication


class SetParamsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.console_ch_box = None
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
        # Разрешить отображать консоль
        concole_lbl = QLabel("Вывод в консоль")
        self.common_box.addRow(concole_lbl)
        #
        self.console_ch_box = QCheckBox("Разрешить", clicked=self.disable_console)
        self.common_box.addRow(self.console_ch_box)
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

    def disable_console(self):
        for widget in QApplication.instance().allWidgets():

            if widget.objectName() == 'action_widget':
                print(self.console_ch_box.isChecked())
                if self.console_ch_box.isChecked():
                    widget.console.show()
                else:
                    widget.console.hide()
