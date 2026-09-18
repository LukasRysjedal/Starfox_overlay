import random
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self, Qapplication):
        super().__init__()

        self.screen_size = Qapplication.primaryScreen().availableGeometry()
        self.screen_width = self.screen_size.width() * 0.7
        self.screen_height = self.screen_size.height() * 0.6
        self.resize(self.screen_width, self.screen_height)
        self.move(0, self.screen_size.height() - self.screen_height)

        self.image_container = QtWidgets.QLabel(self)
        self.image_container.setStyleSheet("border: 3px solid yellow")
        self.image_container.setGeometry(self.screen_width/5, self.screen_height/2,self.screen_height/2, self.screen_height/2)
        self.layout = QtWidgets.QVBoxLayout(self)



        #Sets the attribute for the window/widget
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #The setstyleSheet controls the style
        self.setStyleSheet("border: 2px solid white")

        #Setwindowflag controls the windows behaviour
        #I think i need Qt.WindowActive in the appering logic, or maybe this one Qt.Popup
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.WindowTransparentForInput
        )


def main():
    app = QtWidgets.QApplication([])
    widget = MainWindow(app)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

