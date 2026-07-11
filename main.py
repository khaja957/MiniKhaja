import sys

from PySide6.QtWidgets import QApplication

from desktop.desktop_window import DesktopWindow


def main():

    app = QApplication(sys.argv)

    window = DesktopWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()