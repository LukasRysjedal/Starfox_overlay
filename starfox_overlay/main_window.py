
import os
from PySide6 import QtCore, QtWidgets, QtGui
from starfox_overlay.constants import SCREEN_WIDTH_RATIO, SCREEN_HEIGHT_RATIO , IMAGE_CONTAINER_RATIO, IMAGE_CONTAINER_X_POS_RATIO, IMAGE_CONTAINER_Y_POS_RATIO, TEXT_CONTAINER_WIDTH_RATIO, TEXT_CONTAINER_HEIGHT_RATIO, TEXT_CONTAINER_X_POS_OFFSET, TEXT_CONTAINER_Y_POS_OFFSET_RATIO, TEXT_CONTAINER_BACKGORUNDCOLOR


class Main_window(QtWidgets.QWidget):
    def __init__(self, Qapplication):
        super().__init__()
        self.screen_size = Qapplication.primaryScreen().availableGeometry()
        self.window_width = self.screen_size.width() * SCREEN_WIDTH_RATIO
        self.window_height = self.screen_size.height() * SCREEN_HEIGHT_RATIO

        self.image_container_size = self.window_height * IMAGE_CONTAINER_RATIO
        self.image_container_x_pos = self.window_width * IMAGE_CONTAINER_X_POS_RATIO
        self.image_container_y_pos = self.window_height * IMAGE_CONTAINER_Y_POS_RATIO

        self.text_container_width = self.window_width * TEXT_CONTAINER_WIDTH_RATIO
        self.text_container_height = self.window_height * TEXT_CONTAINER_HEIGHT_RATIO
        self.text_container_x_pos = self.image_container_x_pos + self.image_container_size + TEXT_CONTAINER_X_POS_OFFSET
        self.text_container_y_pos = self.image_container_y_pos + self.image_container_size * TEXT_CONTAINER_Y_POS_OFFSET_RATIO

        self.initialise_window()
        self.initialise_image_container("yellow")
        self.load_custom_fonts()
        self.initialise_text_container()
        self.initialise_username_display()


    def initialise_window(self):
        self.setGeometry(0, self.screen_size.height() - self.window_height, self.window_width, self.window_height)

        #Sets the attribute for the window/widget
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Setwindowflag controls the windows behaviour
        #I think i need Qt.WindowActive in the appering logic, or maybe this one Qt.Popup
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.WindowTransparentForInput
        )

    def initialise_image_container(self, border_color):
        try:
            img_dir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(img_dir,"..", "img", "IMG_3302(1)(1).jpg")
            self.pixmap = QtGui.QPixmap(img_path)
        except Exception as e:
            print(f"Problem with loading img: {e}")

        self.image_container = QtWidgets.QLabel(self)
        self.scaled_img = self.pixmap.scaled(self.image_container_size, self.image_container_size, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image_container.setStyleSheet(f"border: 3px solid {border_color}")
        self.image_container.setGeometry(self.image_container_x_pos,  self.image_container_y_pos, self.image_container_size, self.image_container_size)
        self.image_container.setPixmap(self.scaled_img)

    def initialise_text_container(self):
        self.text_container = QtWidgets.QLabel("Just shoot it fox!", self)
        self.text_container.setStyleSheet(f"background-color: {TEXT_CONTAINER_BACKGORUNDCOLOR}; border: {TEXT_CONTAINER_BACKGORUNDCOLOR}; font-size: 60px; font-family: {self.text_font};")
        self.text_container.setGeometry(self.text_container_x_pos,  self.text_container_y_pos, self.text_container_width, self.text_container_height)

        #Alligne the text in the top left corner, and enable a new line downwards
        self.text_container.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text_container.setWordWrap(True)

    def initialise_username_display(self):
        self.username_display = QtWidgets.QLabel("Lukas", self)
        self.username_display.setStyleSheet(f"border: none; color: yellow; font-size: 33px; font-family: {self.username_font};")

        self.username_display_x_pos = self.text_container_x_pos
        self.username_display_y_pos = self.text_container_y_pos - self.username_display.height()
        self.username_display.move(self.username_display_x_pos,self.username_display_y_pos)


    def load_custom_fonts(self):
        Fontdatabase = QtGui.QFontDatabase
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            username_font_path = os.path.join(script_dir,"..", "fonts", "Press_Start_2P", "PressStart2P-Regular.ttf")
            text_font_path = os.path.join(script_dir,"..", "fonts", "VT323", "VT323-Regular.ttf")

            username_font_id = Fontdatabase.addApplicationFont(username_font_path)
            text_font_id = Fontdatabase.addApplicationFont(text_font_path)

            self.username_font = Fontdatabase.applicationFontFamilies(username_font_id)[0]
            self.text_font = Fontdatabase.applicationFontFamilies(text_font_id)[0]
        except Exception as e:
            print(f"Font loading failed: {e}")
            self.username_font = "Arial"
            self.text_font = "Arial"


