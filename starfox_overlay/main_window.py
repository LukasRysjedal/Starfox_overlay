
import os
from PySide6 import QtCore, QtWidgets, QtGui
from starfox_overlay.constants import SCREEN_WIDTH_RATIO, SCREEN_HEIGHT_RATIO , IMAGE_CONTAINER_RATIO, IMAGE_CONTAINER_X_POS_RATIO, IMAGE_CONTAINER_Y_POS_RATIO, TEXT_CONTAINER_WIDTH_RATIO, TEXT_CONTAINER_HEIGHT_RATIO, TEXT_CONTAINER_X_POS_OFFSET, TEXT_CONTAINER_Y_POS_OFFSET_RATIO, TEXT_CONTAINER_BACKGORUNDCOLOR, TEXT_CONTAINER_START_ANIMATION_Y_POS_OFFSET_RATIO, TEXT_CONTAINER_START_ANIMATION_HEIGHT_RATIO, TEXT_CONTAINER_TEXT_Y_OVERFLOW_TRESHHOLD


class Main_window(QtWidgets.QWidget):
    show_requested = QtCore.Signal()
    hide_requested = QtCore.Signal()
    text_request = QtCore.Signal(str)

    def __init__(self, Qapplication):
        super().__init__()
        self.screen_size = Qapplication.primaryScreen().availableGeometry()
        self.window_width = self.screen_size.width() * SCREEN_WIDTH_RATIO
        self.window_height = self.screen_size.height() * SCREEN_HEIGHT_RATIO

        self.image_container_size = self.window_height * IMAGE_CONTAINER_RATIO
        self.image_container_x_pos = self.window_width * IMAGE_CONTAINER_X_POS_RATIO
        self.image_container_y_pos = self.window_height * IMAGE_CONTAINER_Y_POS_RATIO
        self.image_container_final_animation_rect = QtCore.QRect(
            int(self.image_container_x_pos),
            int(self.image_container_y_pos),
            int(self.image_container_size),
            int(self.image_container_size)
        )
        self.image_container_starter_animation_y_pos = self.image_container_y_pos + self.image_container_size * 0.5
        self.image_container_starter_animation_rect = QtCore.QRect(
            int(self.image_container_x_pos),
            int(self.image_container_starter_animation_y_pos),
            int(self.image_container_size),
            int(0)
        )

        self.text_container_width = self.window_width * TEXT_CONTAINER_WIDTH_RATIO
        self.text_container_height = self.window_height * TEXT_CONTAINER_HEIGHT_RATIO
        self.text_container_x_pos = self.image_container_x_pos + self.image_container_size + TEXT_CONTAINER_X_POS_OFFSET
        self.text_container_y_pos = self.image_container_y_pos + self.image_container_size * TEXT_CONTAINER_Y_POS_OFFSET_RATIO
        self.text_container_final_animation_rect = QtCore.QRect(
            int(self.text_container_x_pos),
            int(self.text_container_y_pos),
            int(self.text_container_width),
            int(self.text_container_height)
        )
        #self.text_container_start_animation_y_pos = self.text_container_y_pos + self.text_container_height * TEXT_CONTAINER_START_ANIMATION_Y_POS_OFFSET_RATIO
        self.text_container_start_animation_y_pos = self.image_container_y_pos + self.image_container_size * 0.5
        self.text_container_start_animation_height = self.text_container_height * TEXT_CONTAINER_START_ANIMATION_HEIGHT_RATIO
        self.text_container_starting_animation_rect = QtCore.QRect(
            int(self.text_container_x_pos),
            int(self.text_container_start_animation_y_pos),
            int(self.text_container_width),
            int(0)
        )

        self.show_requested.connect(self.show_window)
        self.hide_requested.connect(self.hide_window)
        self.text_request.connect(self.show_window)

        self.initialise_window()
        self.initialise_image_container()
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

    def initialise_image_container(self):
        self.image_container = QtWidgets.QLabel(self)
        self.image_container.setGeometry(self.image_container_x_pos, self.image_container_y_pos, self.image_container_size, self.image_container_size)


    def switch_to_image_in_image_container(self, border_color):
        try:
            img_dir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(img_dir,"..", "img", "IMG_3302(1)(1).jpg")
            self.pixmap = QtGui.QPixmap(img_path)
        except Exception as e:
            print(f"Problem with loading img: {e}")
        self.scaled_img = self.pixmap.scaled(self.image_container_size, self.image_container_size, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image_container.setStyleSheet(f"border: 3px solid {border_color}")
        self.image_container.setPixmap(self.scaled_img)

    def swicth_to_loading_image_in_image_container(self):
        try:
            img_dir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(img_dir,"..", "img", "Loading_image", "loading_image.webp")
            self.pixmap = QtGui.QPixmap(img_path)
        except Exception as e:
            print(f"Problem with loading img: {e}")

        self.scaled_img = self.pixmap.scaled(self.image_container_size, self.image_container_size, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image_container.setStyleSheet(f"border: 3px solid white")
        self.image_container.setPixmap(self.scaled_img)


    def initialise_text_container(self):
        self.text_container = QtWidgets.QLabel(self)
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

    def open_text_container(self):
        self.text_container.show()
        self.text_container.setText("")
        self.open_text_animation = QtCore.QPropertyAnimation(self.text_container, b"geometry")
        self.open_text_animation.setDuration(500)
        self.open_text_animation.setStartValue(self.text_container_starting_animation_rect)
        self.open_text_animation.setEndValue(self.text_container_final_animation_rect)
        self.open_text_animation.finished.connect(lambda: self.start_typewriter(self.pending_text))
        self.open_text_animation.start()

    def close_text_container(self):
        self.close_text_animation = QtCore.QPropertyAnimation(self.text_container, b"geometry")
        self.close_text_animation.setDuration(500)
        self.close_text_animation.setStartValue(self.text_container_final_animation_rect)
        self.close_text_animation.setEndValue(self.text_container_starting_animation_rect)
        self.close_text_animation.finished.connect(self.on_close_text_container_closed)
        self.close_text_animation.start()
    def on_close_text_container_closed(self):
        self.text_container.hide()
        QtCore.QTimer.singleShot(600, self.close_image_container)

    def open_image_container(self):
        self.image_container.show()
        self.open_image_animation = QtCore.QPropertyAnimation(self.image_container, b"geometry")
        self.open_image_animation.setDuration(400)
        self.open_image_animation.setStartValue(self.image_container_starter_animation_rect)
        self.open_image_animation.setEndValue(self.image_container_final_animation_rect)
        self.swicth_to_loading_image_in_image_container()
        self.open_image_animation.finished.connect(self.on_image_container_opened)
        self.open_image_animation.start()

    def on_image_container_opened(self):
        QtCore.QTimer.singleShot(600, self.initialize_rest_of_open_animation)

    def initialize_rest_of_open_animation(self):
        self.switch_to_image_in_image_container("yellow")
        self.username_display.show()
        self.open_text_container()

    def close_image_container(self):
        self.close_image_animation = QtCore.QPropertyAnimation(self.image_container, b"geometry")
        self.close_image_animation.setDuration(400)
        self.close_image_animation.setStartValue(self.image_container_final_animation_rect)
        self.close_image_animation.setEndValue(self.image_container_starter_animation_rect)
        self.close_image_animation.finished.connect(self.on_close_image_container_closed)
        self.close_image_animation.start()
    
    def on_close_image_container_closed(self):
        self.image_container.hide()

    def start_typewriter(self, text):
        self.text_index = 0
        self.start_text_index = 0
        self.text = text
        self.text_container.setText("")
        self.typewriter_timer = QtCore.QTimer()
        self.typewriter_timer.timeout.connect(self.display_word)
        self.typewriter_timer.start(30)

    def display_word(self):
        self.text_index += 1
        current_text = self.text[self.start_text_index:self.text_index]
        if self.text_index >= len(self.text):
            self.typewriter_timer.stop()

        at_word_start = (
        self.text_index > self.start_text_index
        and self.text[self.text_index - 1] == " "
        )
        if at_word_start and self.next_word_overflows():
            self.typewriter_timer.stop()
            QtCore.QTimer.singleShot(1000, self.whipe_text_and_continue)
            return

        self.text_container.setText(current_text)

    def next_word_overflows(self):
        word_end = self.text.find(" ", self.text_index)
        if word_end == -1:
            word_end = len(self.text)

        lookahead = self.text[self.start_text_index:word_end]
        metrics = QtGui.QFontMetrics(self.text_container.font())
        width = self.text_container.contentsRect().width()
        rect = metrics.boundingRect(
            QtCore.QRect(0, 0, width, 10000),
            QtCore.Qt.TextWordWrap,
            lookahead
        )
        return rect.height() >= self.text_container_height * TEXT_CONTAINER_TEXT_Y_OVERFLOW_TRESHHOLD


    def whipe_text_and_continue(self):
        self.text_container.setText("")
        self.start_text_index = self.text_index
        self.typewriter_timer.start(30)

    def show_window(self, text):
        self.image_container.hide()
        self.username_display.hide()
        self.text_container.hide()
        self.show()

        self.pending_text = text
        self.open_image_container()


    def hide_window(self):
        self.swicth_to_loading_image_in_image_container()
        self.username_display.hide()
        self.text_container.setText("")
        self.close_text_container()







