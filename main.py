import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
from starfox_overlay.main_window import Main_window

from pynput import keyboard

def main():

    def on_press(key):
        if key == keyboard.Key.ctrl:
            widget.show_requested.emit()
        if key == keyboard.Key.shift:
            widget.hide_requested.emit()

    app = QtWidgets.QApplication([])
    timer = QtCore.QTimer()
    widget = Main_window(app)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    sys.exit(app.exec())




if __name__ == "__main__":
    main()


