import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
from starfox_overlay.main_window import Main_window


def main():
    app = QtWidgets.QApplication([])
    widget = Main_window(app)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

