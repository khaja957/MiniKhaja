import sys

from PySide6.QtWidgets import QApplication

from studio.window import StudioWindow


def main():

    app = QApplication(sys.argv)

    window = StudioWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()