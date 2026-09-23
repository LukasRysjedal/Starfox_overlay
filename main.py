
import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self, Qapplication, username_font, text_font):
        super().__init__()

        self.screen_size = Qapplication.primaryScreen().availableGeometry()
        self.screen_width = self.screen_size.width() * 0.7
        self.screen_height = self.screen_size.height() * 0.6
        self.resize(self.screen_width, self.screen_height)
        self.move(0, self.screen_size.height() - self.screen_height)

        img_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(img_dir, "img", "IMG_3302(1)(1).jpg")

        self.pixmap = QtGui.QPixmap(img_path)
        self.scaled_img = self.pixmap.scaled(self.screen_height/2, self.screen_height/2, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image_container = QtWidgets.QLabel(self)
        self.image_container.setStyleSheet("border: 3px solid yellow")
        self.image_container.setGeometry(self.screen_width/5, self.screen_height/2, self.screen_height/2, self.screen_height/2)
        self.image_container.setPixmap(self.scaled_img)
        #self.layout = QtWidgets.QVBoxLayout(self)

        self.text_container = QtWidgets.QLabel("Just shoot it fox!", self)
        self.text_container.setStyleSheet(f"background-color: rgba(20, 20, 80, 180); border: rgba(20, 20, 80, 180); font-size: 60px; font-family: {text_font};")
        self.text_container.setGeometry(self.screen_width/5 + self.screen_height/2 + 20, self.screen_height/2  + self.screen_height/2*0.05, self.screen_width/1.85, self.screen_height/2 - self.screen_height/2*0.1)
        #Alligne the text in the top left corner, and enable a new line downwards
        self.text_container.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text_container.setWordWrap(True)

        self.username_display = QtWidgets.QLabel("Lukas", self)
        self.username_display.setStyleSheet(f"border: none; color: yellow; font-size: 33px; font-family: {username_font};")
        self.username_display.move(self.screen_width/5 + self.screen_height/2 + 20, self.screen_height/2  + self.screen_height/2*0.05 - self.username_display.height())

        #Sets the attribute for the window/widget
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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
    Fontdatabase = QtGui.QFontDatabase
    #Loading the custom fonts
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        username_font_path = os.path.join(script_dir, "fonts", "Press_Start_2P", "PressStart2P-Regular.ttf")
        text_font_path = os.path.join(script_dir, "fonts", "VT323", "VT323-Regular.ttf")

        username_font_id = Fontdatabase.addApplicationFont(username_font_path)
        text_font_id = Fontdatabase.addApplicationFont(text_font_path)

        username_font = Fontdatabase.applicationFontFamilies(username_font_id)[0]
        text_font = Fontdatabase.applicationFontFamilies(text_font_id)[0]
    except Exception as e:
        print(f"Font loading failed: {e}")
        username_font = "Arial"
        text_font = "Arial"

    widget = MainWindow(app, username_font, text_font)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

