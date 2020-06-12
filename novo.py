import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class New(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.open_image)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open image',
            # Add the path of images in your computer:
            'C:\\Users\\luisf\\Pictures',
            # if the system is presenting errors, try add this line:
            # options=QFileDialog.DontUseNativeDialog
        )
        self.inputOpenFile.setText(image)
        self.originalImg = QPixmap(image)
        self.labelImg.setPixmap(self.originalImg)
        self.inputWidth.setText(str(self.originalImg.width()))
        self.inputHeight.setText(str(self.originalImg.height()))
        self.btnResize.clicked.connect(self.resizeImg)
        self.btnSave.clicked.connect(self.saveImg)

    def resizeImg(self):
        width = int(self.inputWidth.text())
        self.newImage = self.originalImg.scaledToWidth(width)
        self.labelImg.setPixmap(self.newImage)
        self.inputWidth.setText(str(self.newImage.width()))
        self.inputHeight.setText(str(self.newImage.height()))

    def saveImg(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Save image',
            # Add the path of where to save in your computer:
            'C:\\Users\\luisf\\Desktop',
            # if the system is presenting errors, try add this line:
            # options=QFileDialog.DontUseNativeDialog
        )
        self.newImage.save(image, 'PNG')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    new = New()
    new.show()
    qt.exec_()
