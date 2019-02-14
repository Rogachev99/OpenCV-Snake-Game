#!/usr/bin/env python3
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import menu_design
#import setting_detecting_color
import detecting_color
import setting_color
#import test_HSV


class ExampleApp(QtWidgets.QMainWindow, menu_design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.color_lower = [136, 87, 111]
        self.color_upper = [179, 255, 255]
        self.btStartGame.clicked.connect(self.start_game)
        self.btSettings.clicked.connect(self.open_settings)
        self.btAbout.clicked.connect(self.open_about)

    def start_game(self):
        super().hide()
        # print(self.color_lower)
        # print(self.color_upper)
        self.game = detecting_color
        self.game.DETECT_COLOR_LOWER = self.color_lower
        self.game.DETECT_COLOR_UPPER = self.color_upper
        self.game.start_game()
        #while True:
            #detecting_color.start_game()
        super().show()

    def open_settings(self):
        super().hide()
        self.detect = setting_color
        self.color_lower, self.color_upper = self.detect.settings()
        super().show()

    def open_about(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
